import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import re
from uncertainties import ufloat
import locale
locale.setlocale(locale.LC_ALL, '')
import matplotlib as mpl
mpl.rcParams.update({'font.size': 14, 'text.usetex':False, 'text.latex.unicode':True})
mpl.rcParams.update({'mathtext.fontset':'dejavusans'})
mpl.rcParams['axes.formatter.use_locale'] = True

def linear(x, slp, inter):
    return inter + slp * x

c_surf = 12.107     # mmol/L
V_cela = 240e-6     # L

conc_ur = re.compile(r'\d?\d\dmM')
fig2, ax2 = plt.subplots(1, 1, figsize=(9,6))
colors = [f'C{i}' for i in range(10, -1, -1)]

arquivos = glob.glob(r'./csv/convertidos/*csv')
brancos = [i for i in arquivos if 'ctrl' in i]
experimentos = [i for i in arquivos if 'ctrl' not in i]
experimentos = [i for i in experims if ' - 2' not in i]

for exp in experimentos:
    df = pd.read_csv(exp)
    df = df.iloc[1:,:]
    Cur = conc_ur.findall(exp)[0].replace('mM', ' mmol.L$^{-1}$')
    df_br = pd.read_csv(brancos_unique[Cur])
    df_br = df_br.iloc[1:, :]
    nome = f'{Cur}'
    x = df['Xt'] * 1e-3
    y = (df['DQ'] - df_br['DQ']) * 1e-6 / (df['Mt'] * 1e-3 * V_cela)  # (Real - branco)uJ / (n Surf. cela)
    
    p, cov = np.polyfit(x, y, deg=1, full=False, cov=True)
    errs = np.sqrt(np.diag(cov))
    
    u_int = ufloat(p[1], errs[1])
    u_slp = ufloat(p[0], errs[0])
    y_vals_errs = [linear(i, u_slp, u_int) for i in x]
    y_vals = [i.nominal_value for i in y_vals_errs]
    y_errs = [i.std_dev for i in y_vals_errs]
    
    color = colors.pop()
    ax2.plot(x, y, linewidth=0, markersize=5, marker='o', label=nome, color=color)
    ax2.errorbar(x, y_vals, yerr=y_errs, color=color, capsize=3)

ax2.legend(ncol=2, fontsize='small', title='Conc. Ureia')
ax2.set_xlabel('Concentração de ureia na cela/mol.L$^{-1}$')
ax2.set_ylabel('$\Delta H$/J.mol$^{-1}$ de surfactante na cela')
ax2.set_title('TTAB 12 mmol.L$^{-1}$', loc='right')