import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import glob
import gc
import numpy as np
import os
import sys
import shutil
from scipy.signal import savgol_filter
from collections import namedtuple
from lmfit import minimize, Parameters, report_fit

def linear(x, a, b):
    return a * x + b

def residual(params, x, dataset):
    return dataset - linear(x, params['a'], params['b'])

def exp(x, a, b, c):
    return a * np.e ** (x / b) + c

def residual_exp(params, x, dataset):
    return dataset - exp(x, params['a'], params['b'], params['c'])

files = glob.glob('*.txt')
res_aj = namedtuple('Ajuste', ['nome', 'R2', 'ponto', 
                               'a', 'aerr',
                               'b', 'berr', 
                               'c', 'cerr', 
                               'numfits'])

log = open('erros.dat', 'w')
resultados1 = open('paramsg1_0,8hz.dat', 'w')
resultados2 = open('paramsg2_0,8hz.dat', 'w')
resultados_tot = open('resultados_ajustes_0,8hz.dat', 'w')

resultados1.write(f'nome;sobrenome;hora_coleta;hora_medida;data;num1;'
                  f'a_exp1;aerr_exp1;b_exp1;berr_exp1;c_exp1;cerr_exp1;R2_exp1;media1;std1;G0,8hzHz\n')
resultados2.write(f'nome;sobrenome;hora_coleta;hora_medida;data;num2;'
                  f'a_exp2;aerr_exp2;b_exp2;berr_exp2;c_exp2;cerr_exp2;R2_exp2;media2;std2;G0,8hzHz\n')
resultados_tot.write(f'nome;sobrenome;hora_coleta;hora_medida;data;num1;num2;'
                     f'a_exp1;aerr_exp1;b_exp1;berr_exp1;c_exp1;cerr_exp1;R2_exp1;media1;std1;'
                     f'a_exp2;aerr_exp2;b_exp2;berr_exp2;c_exp2;cerr_exp2;R2_exp2;media2;std2;G1_0,8hzHz;G2_0,8hzHz\n')

for j, file in enumerate(files[:]):
    g1fitsmade = 0
    g2fitsmade = 0
    
    try:
        df = pd.read_csv(file, header=linhas[file] - 1, sep=';', encoding='latin1', decimal=',', na_values=' ' )
    except Exception as e:
        print('Failed to open file', file, 'Exception {}'.format(e))
        continue
    
    if len(df['f / Hz']) == 0:
        continue

    df = df.iloc[:, :-1]  #
    df = df.dropna()      #
    df = df.reset_index(drop=True)

    if all(df['Unnamed: 0'].str.startswith('1')):
        df = df
    else:
        df = df[df['Unnamed: 0'].str.startswith('2')]

    if (any(df["G' / Pa"] < 0) or any(df["G'' / Pa"] < 0)):
        print(f'{file} has negative G1, G2 values. Caution\n')
    
    x = np.log10(df["f / Hz"]).reset_index(drop=True)
    y1 = np.log10(df["G' / Pa"]).reset_index(drop=True)
    y2 = np.log10(df["G'' / Pa"]).reset_index(drop=True)

    ajustes_g1_exp = []
    ajustes_g2_exp = []
    ajustes_g1_lin = []
    ajustes_g2_lin = []
    
    if (len(y1) != len(y2)):
        print(f'Comprimentos diferentes: {file}')
    
    for i, val in enumerate(y1):
        if i < 4:
            continue
        
        ############ Exponencial ##################
        params_e = Parameters()
        params_e.add('a', 10., vary=True)
        params_e.add('b', 1. , vary=True)
        params_e.add('c', 0. , vary=True)
        
        try:
            fit1e = minimize(residual_exp, params_e, args=(x[:i], y1[:i]))
            g1fitsmade += 1
        except Exception as e:
            print(file, 'error on fit G1: {}'.format(e))
            #print(y1.hasnans, i, '\n\n', y1[:i])
            continue
        try:
            fit2e = minimize(residual_exp, params_e, args=(x[:i], y2[:i]))
            g2fitsmade += 1
        except Exception as e:
            print(file, 'error on fit G2: {}'.format(e))
            #print(y2.hasnans, i, '\n\n', y2[:i])
            continue
        
        ############### Linear #########################
        
        params_l = Parameters()
        params_l.add('a', 10., vary=True)
        params_l.add('b', 1. , vary=True)
        
        try:
            fit1l = minimize(residual, params_l, args=(x[:i], y1[:i]))
        except Exception as e:
            print(file, 'error on linear fit G1: {}'.format(e))
            #print(y1.hasnans, i, '\n\n', y1[:i])
            continue
        try:
            fit2l = minimize(residual, params_l, args=(x[:i], y2[:i]))
        except Exception as e:
            print(file, 'error on linear fit G2: {}'.format(e))
            #print(y2.hasnans, i, '\n\n', y2[:i])
            continue
        
        ################################################
        a1e = fit1e.params['a'].value
        aerr1e = fit1e.params['a'].stderr
        b1e = fit1e.params['b'].value
        berr1e = fit1e.params['b'].stderr
        c1e = fit1e.params['c'].value
        cerr1e = fit1e.params['c'].stderr

        a2e = fit2e.params['a'].value
        aerr2e = fit2e.params['a'].stderr
        b2e = fit2e.params['b'].value
        berr2e = fit2e.params['b'].stderr
        c2e = fit2e.params['c'].value
        cerr2e = fit2e.params['c'].stderr

        SSres1e = fit1e.chisqr
        SSres2e = fit2e.chisqr
        SStot1e = sum((y1[:i] - np.mean(y1[:i])) ** 2)
        SStot2e = sum((y2[:i] - np.mean(y2[:i])) ** 2)
        R21e = 1 - SSres1e / SStot1e
        R22e = 1 - SSres2e / SStot2e

        r1e = res_aj(file, R21e, i, a1e, aerr1e, b1e, berr1e, c1e, cerr1e, g1fitsmade)
        r2e = res_aj(file, R22e, i, a2e, aerr2e, b2e, berr2e, c2e, cerr2e, g2fitsmade)

        ajustes_g1_exp.append(r1e)
        ajustes_g2_exp.append(r2e)
        ###########################################################
        
        a1l = fit1l.params['a'].value
        aerr1l = fit1l.params['a'].stderr
        b1l = fit1l.params['b'].value
        berr1l = fit1l.params['b'].stderr

        a2l = fit2l.params['a'].value
        aerr2l = fit2l.params['a'].stderr
        b2l = fit2l.params['b'].value
        berr2l = fit2l.params['b'].stderr


        SSres1l = fit1l.chisqr
        SSres2l = fit2l.chisqr
        SStot1l = sum((y1[:i] - np.mean(y1[:i])) ** 2)
        SStot2l = sum((y2[:i] - np.mean(y2[:i])) ** 2)
        R21l = 1 - SSres1l / SStot1l
        R22l = 1 - SSres2l / SStot2l

        r1l = res_aj(file, R21l, i, a1l, aerr1l, b1l, berr1l, 0, 0, 0)
        r2l = res_aj(file, R22l, i, a2l, aerr2l, b2l, berr2l, 0, 0, 0)

        ajustes_g1_lin.append(r1l)
        ajustes_g2_lin.append(r2l)
        
        ###########################################################

    filtro1e = [i for i in ajustes_g1_exp if i.R2 > 0.90]
    filtro2e = [i for i in ajustes_g2_exp if i.R2 > 0.90]
    
    filtro1l = [i for i in ajustes_g1_lin if i.R2 > 0.90]
    filtro2l = [i for i in ajustes_g2_lin if i.R2 > 0.90]

    ###############################
    ## Exp ##
    if len(filtro1e) == 0:
        filtro1e = [i for i in ajustes_g1_exp if i.R2 > 0.85]
        filtro1e.sort(key = lambda x: x.R2, reverse=True)
        if len(filtro1e) == 0:
            filtro1e = ajustes_g1_exp[:]
            filtro1e.sort(key = lambda x: x.R2, reverse=True)
    else:
        filtro1e.sort(key = lambda x: x.ponto, reverse=True)

    if len(filtro2e) == 0:
        filtro2e = [i for i in ajustes_g2_exp if i.R2 > 0.85]
        filtro2e.sort(key = lambda x: x.R2, reverse=True)
        if len(filtro2e) == 0:
            filtro2e = ajustes_g2_exp[:]
            filtro2e.sort(key = lambda x: x.R2, reverse=True)
    else:
        filtro2e.sort(key = lambda x: x.ponto, reverse=True)
    #################################
    ## Linear ##
    if len(filtro1l) == 0:
        filtro1l = [i for i in ajustes_g1_lin if i.R2 > 0.85]
        filtro1l.sort(key = lambda x: x.R2, reverse=True)
        if len(filtro1l) == 0:
            filtro1l = ajustes_g1_lin[:]
            filtro1l.sort(key = lambda x: x.R2, reverse=True)
    else:
        filtro1l.sort(key = lambda x: x.ponto, reverse=True)

    if len(filtro2l) == 0:
        filtro2l = [i for i in ajustes_g2_lin if i.R2 > 0.85]
        filtro2l.sort(key = lambda x: x.R2, reverse=True)
        if len(filtro2l) == 0:
            filtro2l = ajustes_g2_lin[:]
            filtro2l.sort(key = lambda x: x.R2, reverse=True)
    else:
        filtro2l.sort(key = lambda x: x.ponto, reverse=True)
    #################################

    bom1 = filtro1e[0]
    bom2 = filtro2e[0]
    
    bom1l = filtro1l[0]
    bom2l = filtro2l[0]

    media1 = np.average(df["G' / Pa"][:bom1.ponto])
    media2 = np.average(df["G'' / Pa"][:bom2.ponto])
    stdmedia1 = np.std(df["G' / Pa"][:bom1.ponto])
    stdmedia2 = np.std(df["G'' / Pa"][:bom2.ponto])
    
    media1l = np.average(df["G' / Pa"][:bom1l.ponto])
    media2l = np.average(df["G'' / Pa"][:bom2l.ponto])
    stdmedia1l = np.std(df["G' / Pa"][:bom1l.ponto])
    stdmedia2l = np.std(df["G'' / Pa"][:bom2l.ponto])
    
    try:
        g1_1hz = df[df['f / Hz'] == 0.6813]["G' / Pa"].iloc[0]
        g2_1hz = df[df['f / Hz'] == 0.6813]["G'' / Pa"].iloc[0]
    except:
        print(f'File: {file} has no data at 1Hz')
    
    resultados1.write(f'{bom1.nome[:-4].replace(" ", ";")};{bom1.ponto};'
                      f'{bom1.a};{bom1.aerr};'
                      f'{bom1.b};{bom1.berr};'
                      f'{bom1.c};{bom1.cerr};'
                      f'{bom1.R2};{media1l};{stdmedia1l};{g1_1hz}\n')
    
    resultados2.write(f'{bom2.nome[:-4].replace(" ", ";")};{bom2.ponto};'
                      f'{bom2.a};{bom2.aerr};'
                      f'{bom2.b};{bom2.berr};'
                      f'{bom2.c};{bom2.cerr};'
                      f'{bom2.R2};{media2l};{stdmedia2l};{g2_1hz}\n')
    
    resultados_tot.write(f'{bom1.nome[:-4].replace(" ", ";")};{bom1.ponto};{bom2.ponto};'
                      f'{bom1.a};{bom1.aerr};'
                      f'{bom1.b};{bom1.berr};'
                      f'{bom1.c};{bom1.cerr};'
                      f'{bom1.R2};{media1l};{stdmedia1l};'
                      f'{bom2.a};{bom2.aerr};'
                      f'{bom2.b};{bom2.berr};'
                      f'{bom2.c};{bom2.cerr};'
                      f'{bom2.R2};{media2l};{stdmedia2l};{g1_1hz};{g2_1hz}\n')

    plt.gcf().clf()
    plt.close()
    del df
    gc.collect()
    
    print(f'Tratado arquivo {j+1} de {len(files)}\r', end='')
    
resultados1.close()
resultados2.close()
resultados_tot.close()
log.close()