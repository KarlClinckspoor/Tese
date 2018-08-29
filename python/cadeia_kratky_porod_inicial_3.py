# ... Continuação ...
    # Calcular os termos A, Eq. \ref{eqn:AP_Ai}
    for i in range(2, 5 + 1, 1):
        AA[i] = 0
        for ii in range(0, 2 + 1, 1):
            if ii == 0:
                AA[i] = AA[i] + A1[i, ii] / (L ** ii) * AEXP
            else:
                AA[i] = AA[i] + A1[i, ii] / (L ** ii) * AEXP + A2[i, ii] * (L ** ii) * AEXP1
    
    # Calcular os termos B, Eq. \ref{eqn:AP_Bi}
    for i in range(0, 2 + 1, 1):
        BB[i] = 0
        for ii in range(0, 2 + 1, 1):
            if ii == 0:
                BB[i] = BB[i] + B1[i, ii] / (L ** ii)
            else:
                BB[i] = BB[i] + B1[i, ii] / (L ** ii) + B2[i, ii] * L ** ii * AEXP1
    
    # Calcular a função de correção FGAMMA, Eq. \ref{eqn:AP_Gamma}
    F1 = 0
    F2 = 0
    for i in range(2, 5 + 1, 1):
        F1 = F1 + AA[i] * PSI ** i
    for i in range(0, 2 + 1, 1):
        F2 = F2 + BB[i] / PSI ** i
    FGAMMA = 1 + (1 - CHI) * F1 + CHI * F2   

    # Função Final
    # Redução de Gamma por tentativa e erro para os efeitos de volume excluído

    if I_EXVOL == 1:
        FGAMMA = SCALE * (FGAMMA - 1) + 1
        
    # Expansão de argumentos grandes
    
    if KK == 0:
        S_KP_EXV = F_IP * FGAMMA  # Eq. \ref{eqn:AP_Fwc}
        return S_KP_EXV
    else:
        CONST = 100 * (F_IP * FGAMMA - PI / (10 * L))  # Constante de proporcionalidade
        S_KP_EXV = PI / (K_MEM * L) + CONST / (K_MEM * K_MEM)
        return S_KP_EXV