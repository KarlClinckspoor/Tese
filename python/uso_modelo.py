from SAXS_FF import WLM_q
import numpy as np
import matplotlib.pyplot as plt

# Inicialização dos parâmetros, obtidos de um ajuste
scale    = 0.1440E+00
d_head   = 0.1929E+02
rad_core = 0.8109E+01
rho_rel  = 0.5999E-01
sigma    = 0.1000E+01
back     = 0.0000E+00
L        = 0.5000E+04
kuhn     = 0.1000E+04
eps      = 0.1000E+01
D_CQ     = 0.1050E+03
nu_rpa   = 0.3846E+02
SC_pow   = 0.6757E-03
exponent = 4.0000E+00

# Criação dos arrays de dados
q = np.logspace(-2.5, -0.5)  # Faixa de q usual
I = WLM_q(q, scale, d_head, rad_core, rho_rel, sigma, back, L, kuhn, eps, D_CQ, nu_rpa, SC_pow, exponent)

# Plotando
#        x, y
plt.plot(q, I)
plt.xscale('log')
plt.yscale('log')
plt.show()