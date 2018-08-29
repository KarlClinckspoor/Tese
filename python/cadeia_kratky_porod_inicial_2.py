# ... Continuação ...
    # Função de espalhamento de bastões
    
    A = K * L
    # SI\_P: integral seno-cosseno, função seno cardinal
    # Eq. \ref{eqn:AP_Frod}
    F_ROD = 2 * SI_P(A) / A - (4 / (A ** 2)) * (np.sin(0.5 * A)) ** 2
    
    # Peso CHI
    
    if I_EXVOL:
        # Eq. \ref{eqn:AP_xi}
        PSI = K * ((PI / abs(1.103 * L)) ** 1.5) * (S2 ** 1.282)
    
    AEXP = 1 / (PSI ** 5)
    
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
    
    AEXP1 = 2 * L
    
    if AEXP1 > 74:
        AEXP = 0
    else:
        AEXP1 = np.exp(-AEXP1)
# ... Continua ...