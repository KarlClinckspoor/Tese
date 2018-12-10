import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import glob

def meia_altura(arquivo, dic={}):
    arq = pd.read_csv(arquivo, encoding='ANSI', header=53, names=['a', 'T', 'Q', 'N'], sep=' ', skipfooter=1, skiprows=[8303], engine='python')

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
    # continua ...