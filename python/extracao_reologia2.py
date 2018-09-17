        # ... continuação 
        for i, item in enumerate(df_OF_m):
            try:
                if df_OF_m[i-1] == True and df_OF_m[i+1] == True and df_OF_m[i] == False:
                    df_OF_m[i] = True
            except KeyError:
                pass
            except IndexError:
                pass
                
        df_OF = df_osc[df_OF_m]
        df_OF = df_OF[['w', 'G1', 'G2', 'T']]
        df_OF = df_OF.add_prefix(nome)

        if df_OF.size == 0:
            df_OF = None
        elif (df_OF.index[0] + 1) != df_OF.index[1]: # É possível que haja uma coincidencia e repita um valor de Freq.
            
            df_OF = df_OF.drop(df_OF.index[-1])
    else:
        df_OT = None
        df_OF = None
    
    return df_CF, df_OT, df_OF

    
def main():
    nomes = [arq.split(' ')[0] for arq in glob.glob('*.txt')]
    arquivos = glob.glob('*.txt')

    for nome, arq in zip(nomes, arquivos):
        print('Tratando {0}'.format(arq))
        pd_temp = pd.read_csv(arq, delimiter=';', header=4, 
                        names=["serie", "GP", "Eta", "w", "G1", "G2", "T", "Tau", 'lixo'], encoding='latin1', decimal=',')

        temp_CF, temp_OT, temp_OF = extracao(pd_temp, nome=nome+' ')

        if type(temp_CF) != type(None):
            counter = 0
            while os.path.isfile('CF_{0}--{1}.csv'.format(nome, counter)):
                counter += 1
            temp_CF.to_csv('CF_{0}--{1}.csv'.format(nome, counter), sep=';', encoding='utf8', index=False, decimal=',')
            
        if type(temp_OT) != type(None):
            counter = 0 
            while os.path.isfile('OT_{0}--{1}.csv'.format(nome, counter)):
                counter += 1
            temp_OT.to_csv('OT_{0}--{1}.csv'.format(nome, counter), sep=';', encoding='utf8', index=False, decimal=',')
            
        if type(temp_OF) != type(None):
            counter = 0 
            while os.path.isfile('OF_{0}--{1}.csv'.format(nome, counter)):
                counter += 1
            temp_OF.to_csv('OF_{0}--{1}.csv'.format(nome, counter), sep=';', encoding='utf8', index=False, decimal=',')

        
if __name__ == '__main__':
    main()