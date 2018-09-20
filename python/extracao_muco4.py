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
        
        #################################

    filtro1e = [i for i in ajustes_g1_exp if i.R2 > 0.90]
    filtro2e = [i for i in ajustes_g2_exp if i.R2 > 0.90]
    
    filtro1l = [i for i in ajustes_g1_lin if i.R2 > 0.90]
    filtro2l = [i for i in ajustes_g2_lin if i.R2 > 0.90]

    ##### Selecionando os melhores valores dos ajustes ############
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
    ## Linear ##
    if len(filtro1l) == 0:
        filtro1l = [i for i in ajustes_g1_lin if i.R2 > 0.85]
        filtro1l.sort(key = lambda x: x.R2, reverse=True)
        if len(filtro1l) == 0:
            filtro1l = ajustes_g1_lin[:]
            filtro1l.sort(key = lambda x: x.R2, reverse=True)
    else:
        filtro1l.sort(key = lambda x: x.ponto, reverse=True)