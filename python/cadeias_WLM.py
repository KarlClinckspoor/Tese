def wormlike_chains(q, scale, d_head, Rcore, rho_rel, sigma, back, cont_l, kuhn_l, eps, dist_cq, nu_ppa,
                    scale_pow, exponent):
    Rout = Rcore + d_head
    FX = (((rho_rel * Rout ** 2 * 2 * jv(1, Rout * q) / (q * Rout)) -
           ((rho_rel + 1) * Rcore ** 2 * 2 * jv(1, Rcore * q) / (q * Rcore))) *
          np.exp((-1/2) * q ** 2 * sigma ** 2))

    FOX = rho_rel * Rout ** 2 - (rho_rel + 1) * Rcore ** 2

    cyl_int = 0  # SUM
    npoints = 50
    step = 0.5 * np.pi / npoints

    EPSO = (Rcore * eps + d_head) / Rout
    for i in range(1, npoints + 1):
        alpha = (i - 0.5) * step
        sinalpha = sin(alpha)

        SC = np.sqrt(sinalpha ** 2 + eps ** 2 * (1 - sinalpha ** 2))
        RA = Rcore * SC

        # RO = R + A(2)  - unnecessary
        SCO = np.sqrt(sinalpha ** 2 + EPSO ** 2 * (1 - sinalpha ** 2))
        RAO = Rout * SCO

        F = (((EPSO * rho_rel * Rout ** 2 * 2 * jv(1, RAO * q) / (q * RAO)) -
              ((rho_rel + 1) * eps * Rcore ** 2 * 2 * jv(1, RA * q) / (q * RA))) *
             np.exp((-0.5) * q ** 2 * sigma ** 2))
        cyl_int = cyl_int + F ** 2  # === SUM=SUM+F**2

    cyl_int = cyl_int * step * 2 / np.pi
    FO = EPSO * rho_rel * Rout ** 2 - (rho_rel + 1) * eps * Rcore ** 2
    # if J == 1:
    # print (qs, FX ** 2, FOX ** 2, cyl_int, FO ** 2)
    SQ = S_KP_EXV(q, cont_l, kuhn_l)

    CQ = FI(q * dist_cq)
    FORMF = SQ * cyl_int / (FO ** 2)
    Rout = abs(d_head) + abs(Rcore)  # necessary?

    FORMFX = SQ  # 2 * jv(1, qs * Rout) / (qs * Rout) ** 2

    XSEC = scale * FORMF / (1 + nu_ppa * CQ * FORMFX) + back + scale_pow* (0.01 / q) ** exponent

    return XSEC

def WLM_whole_q(qs, scale, d_head, rad_core, rho_rel, sigma, back, L, kuhn, eps, D_CQ, nu_rpa, SC_pow, exponent):
    ints = np.zeros(len(qs))
    for i, q in enumerate(qs):
        ints[i] = wormlike_chains(q, scale, d_head, rad_core, rho_rel, sigma, back, L, kuhn, eps, D_CQ, nu_rpa,
                                  SC_pow, exponent)
    return ints

def FI(X):
    if X > 0.05:
        FI = 3 * (sin(X) - X * cos(X))/(X**3)
        return FI
    else:
        FI = 1 - 0.1 * X * X
        return FI