import numpy as np
def wormlike_chains(q, scale, d_head, Rcore, rho_rel, sigma, back, cont_l, kuhn_l, eps, dist_cq, nu_ppa, scale_pow, exponent):
    Rout = Rcore + d_head   # Raio
    # Integração numérica da Eq. \ref{eqn:AP_Fcs}, primeiro fator da Eq. \ref{eqn:AP_Fwc}
    cyl_int = 0
    npoints = 50
    step = 0.5 * np.pi / npoints

    EPSO = (Rcore * eps + d_head) / Rout  # epsilon casca
    for i in range(1, npoints + 1):
        alpha = (i - 0.5) * step
        sinalpha = sin(alpha)
        # Interior
        SC = np.sqrt(sinalpha ** 2 + eps ** 2 * (1 - sinalpha ** 2))  # Eq. \ref{eqn:AP_Rc}
        RA = Rcore * SC  # Eq. \ref{eqn:AP_Rs}
        # Casca
        SCO = np.sqrt(sinalpha ** 2 + EPSO ** 2 * (1 - sinalpha ** 2)) # Eq. \ref{eqn:AP_Rc}
        RAO = Rout * SCO # Eq. \ref{eqn:AP_Rs}

        # jv: Função de bessel (de primeiro grau)
        F = (((EPSO * rho_rel * Rout ** 2 * 2 * jv(1, RAO * q) / (q * RAO)) -
              ((rho_rel + 1) * eps * Rcore ** 2 * 2 * jv(1, RA * q) / (q * RA))) *
             np.exp((-0.5) * q ** 2 * sigma ** 2))

        cyl_int = cyl_int + F ** 2 
    cyl_int = cyl_int * step * 2 / np.pi  # Fim da integração numérica e uma normalização
    
    FO = EPSO * rho_rel * Rout ** 2 - (rho_rel + 1) * eps * Rcore ** 2
    SQ = S_KP_EXV(q, cont_l, kuhn_l)  # Presente na seção \ref{sec:apendice_F_KPchain}
    CQ = FI(q * dist_cq)
    FORMF = SQ * cyl_int / (FO ** 2)
    Rout = abs(d_head) + abs(Rcore)

    FORMFX = SQ
    # Eq. \ref{eqn:AP_saxs_MG_geral}
    XSEC = scale * FORMF / (1 + nu_ppa * CQ * FORMFX) + back + scale_pow* (0.01 / q) ** exponent
    return XSEC

def FI(X):  # Fator forma da esfera, Eq. \ref{eqn:AP_Fsphere}
    if X > 0.05:
        FI = 3 * (sin(X) - X * cos(X))/(X**3)
        return FI
    else:  # Aproximação para valores de qR baixos
        FI = 1 - 0.1 * X * X
        return FI