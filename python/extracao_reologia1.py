#!python3

import pandas as pd
import glob
import numpy as np
import os

def extracao(df, nome=''):
    df = df.replace(to_replace=r'\s+', value=np.nan, regex=True)
    
    # Curva de fluxo
    df_CF = df[['GP', 'Eta','T', 'Tau']].dropna()
    df_CF = df_CF.add_prefix(nome)

    if df_CF.size == 0:
        df_CF = None
    
    df_osc = df[['w','Tau', 'G1', 'G2', 'T']].dropna()
    
    if df_osc.size != 0:
        contagem_w_OT = df_osc['w'].value_counts()
        if contagem_w_OT.size == 0:
            w_mais_freq_OT = pd.Series([])
            df_OT = None
        elif contagem_w_OT.max() == 1:
            df_OT = None
            w_mais_freq_OT = 0 
        else:
            w_mais_freq_OT = contagem_w_OT.idxmax()
            indice_w_mais_freq = contagem_w_OT.max()

            df_OT_m = df_osc['w'] == w_mais_freq_OT
            df_OT = df_osc[df_OT_m]
            df_OT = df_OT[['Tau', 'G1', 'G2', 'T']]
            if df_OT.index[-1] - 1 != df_OT.index[-2]:
                df_OT = df_OT.drop(df_OT.index[-1])
            df_OT = df_OT.add_prefix(nome)

        ## Frequencia
        if contagem_w_OT.size != 0:
            df_OF_m = df_osc['w'] != w_mais_freq_OT
        else:
            df_OF_m = []
        # continua ...