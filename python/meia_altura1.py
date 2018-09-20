import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import glob

def meia_altura(arquivo, dic={}):
    arq = pd.read_csv(arquivo, encoding='ANSI', header=53, 
                          names=['a', 'T', 'Q', 'N'], sep=' ', 
                          skipfooter=1, skiprows=[8303], engine='python')
    
    mpl.rcParams.update({'font.size': 14, 'text.usetex':False, 'text.latex.unicode':True})
    mpl.rcParams.update({'mathtext.fontset':'dejavusans'})

    abaixo = arq.loc[:len(arq) // 2, ['T', 'Q']]
    acima =  arq.loc[len(arq) // 2:, ['T', 'Q']]

    if arquivo + 'abaixo' not in dic.keys():
        linhabase_abaixo = abaixo['Q'].median()
    else:
        linhabase_abaixo = dic[arquivo+'abaixo']
        
    if arquivo + 'acima' not in dic.keys():
        linhabase_acima = acima['Q'].median()
    else:
        linhabase_acima = dic[arquivo+'acima']

    abaixo = abaixo - linhabase_abaixo
    acima = acima - linhabase_acima

    y_pico_abaixo = abaixo['Q'].min()
    x_pico_abaixo = abaixo['T'][abaixo['Q'].idxmin()]

    y_pico_acima = acima['Q'].max()
    x_pico_acima = acima['T'][acima['Q'].idxmax()]

    meiaaltura_abaixo = y_pico_abaixo / 2
    meiaaltura_acima = y_pico_acima  / 2

    interesse_abaixo = abaixo[abaixo['Q'] < meiaaltura_abaixo]
    interesse_acima = acima[acima['Q'] > meiaaltura_acima]

    primeiro_abaixo = interesse_abaixo.iloc[0, :]
    primeiro_acima = interesse_acima.iloc[0, :]
    ultimo_abaixo = interesse_abaixo.iloc[-1, :]
    ultimo_acima = interesse_acima.iloc[-1, :]

    dict_line = {'linestyle':'--', 'color':'k'}
    dict_line2 = {'linestyle':'--', 'color':'r'}
    dict_text = {'horizontalalignment':'center', 'verticalalignment':'center', 'color':'k', 'fontsize':'10'}
    # continua ...