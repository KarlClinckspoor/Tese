        try:
            fit1l = minimize(residual, params_l, args=(x[:i], y1[:i]))
        except Exception as e:
            print(file, 'error on linear fit G1: {}'.format(e))
            continue
        try:
            fit2l = minimize(residual, params_l, args=(x[:i], y2[:i]))
        except Exception as e:
            print(file, 'error on linear fit G2: {}'.format(e))
            continue
        
        ######## Extraindo valores dos ajustes exponenciais #######
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

        ######## Extraindo valores dos ajustes lineares #######
        a1l = fit1l.params['a'].value
        aerr1l = fit1l.params['a'].stderr
        b1l = fit1l.params['b'].value
        berr1l = fit1l.params['b'].stderr

        a2l = fit2l.params['a'].value
        aerr2l = fit2l.params['a'].stderr
        b2l = fit2l.params['b'].value
        berr2l = fit2l.params['b'].stderr