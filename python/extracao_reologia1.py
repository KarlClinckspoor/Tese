#!python3

import pandas as pd
import glob
import numpy as np
import os

def extracao(df, nome=''):
    df = df.replace(to_replace=r'\s+', value=np.nan, regex=True)
    
    # Curva de fluxo
    df_CF = df[['GP', 'Eta','T', 'Tau']].dropna() # Extrai CF porque os Osc tem n/a nos valores de eta
    df_CF = df_CF.add_prefix(nome)

    if df_CF.size == 0:
        df_CF = None
    
    
    df_osc = df[['w','Tau', 'G1', 'G2', 'T']].dropna()
    
    if df_osc.size != 0:  # Checa se tem dado de oscilatório
        ## Oscilatório Tensão
        contagem_w_OT = df_osc['w'].value_counts() # Conta quantas vezes um valor de freq se repetiu
        if contagem_w_OT.size == 0: # Matriz vazia
            w_mais_freq_OT = pd.Series([])
            df_OT = None # Sem qualquer dado oscilatório
        elif contagem_w_OT.max() == 1:  # Não repete nenhum valor
            df_OT = None  # Sem dado de Osc Tens
            w_mais_freq_OT = 0  # Coloca um valor para comparar
        else:
            w_mais_freq_OT = contagem_w_OT.idxmax() # Valor de freq que mais repete (1 Hz): indica Osc Tens
            indice_w_mais_freq = contagem_w_OT.max()

            df_OT_m = df_osc['w'] == w_mais_freq_OT  # Criar máscara para o Osc Tens
            df_OT = df_osc[df_OT_m]  # Aplicar a máscara.
            df_OT = df_OT[['Tau', 'G1', 'G2', 'T']]  # Separa só os valores de interesse

            if df_OT.index[-1] - 1 != df_OT.index[-2]: # É possível que haja uma coincidencia e repita um valor de Freq.
                #df\_OT = df\_OT.drop(index = df\_OT.index[-1]) # Remove último ponto se ele não for contínuo com o anterior
                df_OT = df_OT.drop(df_OT.index[-1])

            df_OT = df_OT.add_prefix(nome)  # Coloca o nome para exportação

        ## Frequencia
        
        
        if contagem_w_OT.size != 0: # Revisar aqui
            df_OF_m = df_osc['w'] != w_mais_freq_OT # complementar ao Osc Tens
        else:
            df_OF_m = [] # Matriz vazia
        # continua ...