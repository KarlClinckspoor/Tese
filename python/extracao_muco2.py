
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
        
        ############ Exponencial #########
        
        params_e = Parameters()
        params_e.add('a', 10., vary=True)
        params_e.add('b', 1. , vary=True)
        params_e.add('c', 0. , vary=True)
        
        try:
            fit1e = minimize(residual_exp, params_e, args=(x[:i], y1[:i]))
            g1fitsmade += 1
        except Exception as e:
            print(file, 'error on fit G1: {}'.format(e))
            continue
        try:
            fit2e = minimize(residual_exp, params_e, args=(x[:i], y2[:i]))
            g2fitsmade += 1
        except Exception as e:
            print(file, 'error on fit G2: {}'.format(e))
            continue
        
        ############### Linear ############
        
        params_l = Parameters()
        params_l.add('a', 10., vary=True)
        params_l.add('b', 1. , vary=True)
        