# Aplicando os valores para a faixa inteira de q. Numpy arrays causam incompatibilidades com alguns componentes internos.
def WLM_q(qs, scale, d_head, rad_core, rho_rel, sigma, back, L, kuhn, eps, D_CQ, nu_rpa, SC_pow, exponent):
    ints = np.zeros(len(qs))
    for i, q in enumerate(qs):
        ints[i] = wormlike_chains(q, scale, d_head, rad_core, rho_rel, sigma, back, L, kuhn, eps, D_CQ, nu_rpa, SC_pow, exponent)
    return ints

