def S_EXV_APP(Q):  # Eq. \ref{eqn:AP_fdebye}
    X = Q ** 2
    if X < 0.01:
        S_DEB = 1 - 0.333333333 * X
    else:
        if X > 74:
            AEXP = 0
        else:
            AEXP = np.exp(-X)
        S_DEB = 2 * (AEXP + X - 1) / (X ** 2)
    
    W = 0.5 * (np.tanh((Q - 1.523) / 0.1477) + 1)  # Eq. \ref{eqn:AP_w}
    if Q < 0.3:
        W = 0
        Y2 = 0
    else:
        # Constantes da Tab. \ref{tab_ap:C1C5}
        Y2 = 1.220 / (Q ** 1.709) + 0.4288 / (Q ** 3.419) - 1.651 / (Q ** 5.128)

    S_EXV_APP = (1 - W * S_DEB + W * Y2)  # \ref{eqn:AP_FchainExV}
    return S_EXV_APP