# ... Continuação ...
   if I_EXVOL:
        AEXP = 2 * L
        if AEXP > 60:
            AEXP = 0
        else:
            AEXP = np.exp(-AEXP)
        
        # Declaração de algumas constantes
        EPSI = 0.17
        EXPAN = (1 + (abs(L / 3.12) ** 2) + abs(L / 8.67) ** 3) ** (EPSI / 3)
        S2 = L / 6 - 0.25 + 0.25 / L - (1 - AEXP) / (8 * L * L)
        S2 = S2 * EXPAN

        F_DEBYE = S_EXV_APP(K * np.sqrt(S2))
    # Função de espalhamento de bastões
    
    A = K * L
    # SI\_P: integral seno-cosseno, função seno cardinal
    # Eq. \ref{eqn:AP_Frod}
    F_ROD = 2 * SI_P(A) / A - (4 / (A ** 2)) * (np.sin(0.5 * A)) ** 2
    
    # Peso CHI
    
    if I_EXVOL:
        # Eq. \ref{eqn:AP_xi}
        PSI = K * ((PI / abs(1.103 * L)) ** 1.5) * (S2 ** 1.282)
    
    AEXP = 1 / (PSI ** 5)  # Eq. \ref{eqn:AP_chi}
    
    if AEXP > 74:
        CHI = 0
    else:
        CHI = np.exp(-AEXP)  # Eq. \ref{eqn:AP_chi}
    
    # Função interpolada F\_IP
    
    F_IP = (1 - CHI) * F_DEBYE + CHI * F_ROD  # Eq. \ref{eqn:AP_Fwc}
        
    # Função de correção FGAMMA
    # Calcular os termos A
    
    AEXP = 40 / (4 * L)
    
    if AEXP > 74:
        AEXP = 0
    else:
        AEXP = np.exp(-AEXP)
# ... Continua ...