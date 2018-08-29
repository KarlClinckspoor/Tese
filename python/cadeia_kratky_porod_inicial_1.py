import numpy as np

def S_KP_EXV(Q, RL, RLL):
    # RL = comprimento de contorno
    # RRL = comprimento de Kuhn
    # I\_EXVOL = 0:cadeias gaussianas
    #         = 1:efeitos de volume excluído inclusos (sempre 1 neste caso)
    # A1, A2, B1, B2, AA, BB: tabelas
    # K, L, K\_MEM: floats
    
    A1 = np.zeros((6, 6))
    A2 = np.zeros((6, 6))
    B1 = np.zeros((6, 6))
    B2 = np.zeros((6, 6))
    AA = np.zeros(6)
    BB = np.zeros(6)
    # Definições das constantes da tabela \ref{tab_ap:AiBi}
    A1[2, 0], A1[3, 0], A1[4, 0], A1[5, 0] = -0.1222, 0.3051, -0.0711, 0.0584
    A1[2, 1], A1[3, 1], A1[4, 1], A1[5, 1] = 1.761, 2.252, -1.291, 0.6994
    A1[2, 2], A1[3, 2], A1[4, 2], A1[5, 2] = -26.04, 20.00, 4.382, 1.594
    
    A2[2, 1], A2[3, 1], A2[4, 1], A2[5, 1] = 0.1212, -0.4169, 0.1988, 0.3435
    A2[2, 2], A2[3, 2], A2[4, 2], A2[5, 2] = 0.0170, -0.4731, 0.1869, 0.3350
    
    B1[0, 0], B1[1, 0], B1[2, 0] = -0.0699, -0.0900, 0.2677
    B1[0, 1], B1[1, 1], B1[2, 1] = 0.1342, 0.0138, 0.1898
    B1[0, 2], B1[1, 2], B1[2, 2] = -0.2020, -0.0114, 0.0123
    
    B2[0, 1], B2[1, 1], B2[2, 1] = -0.5171, -0.2028, -0.3112
    B2[0, 2], B2[1, 2], B2[2, 2] = 0.6950, -0.3238, -0.5403
    
    PI = np.pi  # Compatibiliade de código
    K = Q * RLL
    L = RL/RLL
    I_EXVOL = 1
    SCALE = 1
    KK = 0
    
    if K > 10:
        K_MEM = K
        K = 10
        KK = 1
    
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

# ... Continua ...