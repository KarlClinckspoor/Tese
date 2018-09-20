import matplotlib.pyplot as plt
import pandas as pd
import glob
import gc
import numpy as np
from collections import namedtuple
from lmfit import minimize, Parameters, report_fit

files = glob.glob('*.txt')
res_aj = namedtuple('Ajuste', ['nome', 'R2', 'ponto', 
                               'a', 'aerr',
                               'b', 'berr', 
                               'c', 'cerr', 
                               'numfits'])

log = open('erros.dat', 'w')
resultados1 = open('paramsg1.dat', 'w')
resultados2 = open('paramsg2.dat', 'w')
resultados_tot = open('resultados_ajustes.dat', 'w')

resultados1.write(f'nome;sobrenome;hora_coleta;hora_medida;data;num1;'
                  f'a_exp1;aerr_exp1;b_exp1;berr_exp1;c_exp1;cerr_exp1;R2_exp1;media1;std1;G1Hz\n')
resultados2.write(f'nome;sobrenome;hora_coleta;hora_medida;data;num2;'
                  f'a_exp2;aerr_exp2;b_exp2;berr_exp2;c_exp2;cerr_exp2;R2_exp2;media2;std2;G1Hz\n')
resultados_tot.write(f'nome;sobrenome;hora_coleta;hora_medida;data;num1;num2;'
                     f'a_exp1;aerr_exp1;b_exp1;berr_exp1;c_exp1;cerr_exp1;R2_exp1;media1;std1;'
                     f'a_exp2;aerr_exp2;b_exp2;berr_exp2;c_exp2;cerr_exp2;R2_exp2;media2;std2;G1_1Hz;G2_1Hz\n')

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
