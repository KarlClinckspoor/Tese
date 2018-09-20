    if len(filtro2l) == 0:
        filtro2l = [i for i in ajustes_g2_lin if i.R2 > 0.85]
        filtro2l.sort(key = lambda x: x.R2, reverse=True)
        if len(filtro2l) == 0:
            filtro2l = ajustes_g2_lin[:]
            filtro2l.sort(key = lambda x: x.R2, reverse=True)
    else:
        filtro2l.sort(key = lambda x: x.ponto, reverse=True)
    
    ######## Extraindo outros parâmetros das curvas ###############
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
        g1_1hz = df[df['f / Hz'] == 1]["G' / Pa"].iloc[0]
        g2_1hz = df[df['f / Hz'] == 1]["G'' / Pa"].iloc[0]
    except:
        print(f'File: {file} has no data at 1Hz')
    
    ######## Salvando os resultados em arquivos ##########
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
    