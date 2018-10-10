import pandas as pd
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_ALL, '')

import matplotlib as mpl
mpl.rcParams.update({'font.size': 14})
mpl.rcParams.update({'mathtext.fontset':'dejavusans'})
mpl.rcParams['axes.formatter.use_locale'] = True

f = r'./dados experimentais/CTAB300Ur40_qbaixo.dat'
df = pd.read_csv(f, sep='  ', names=['q', 'I'], engine='python')
fig, ax = plt.subplots(1, 1, figsize=(9,6))

ax.plot('q', 'I', data=df)
ax.set(xscale='log', yscale='log', xlabel=r'q/nm$^{-1}$', ylabel='I/u.a.')
fig.savefig('../saxs/exemplo_SAXS.pdf')
