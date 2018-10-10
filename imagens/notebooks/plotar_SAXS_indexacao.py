import pandas as pd
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_ALL, '')

import matplotlib as mpl
mpl.rcParams.update({'font.size': 14})
mpl.rcParams.update({'mathtext.fontset':'dejavusans'})
mpl.rcParams['axes.formatter.use_locale'] = True

f = r'./dados experimentais/DTAB300Ur40.dat'
df = pd.read_csv(f, sep=' ', names=['q', 'I', 'l'], engine='python', header=1)
fig, ax = plt.subplots(1, 1, figsize=(9,6))

ax.plot('q', 'I', data=df)
ax.set(xlabel=r'q/nm$^{-1}$', ylabel='I/u.a.', xlim=(0,3.5), yscale='log')

pico_y = df['I'].max()
pico_x = df['q'][df['I'].idxmax()]

for i in range(6):
    ax.axvline(pico_x * (i+1), color='r', linestyle='--')
    ax.text(x=pico_x * (i+1), y=df['I'].max(), s=str(i+1))
#    ax.text(x=pico_x * (i+1), y=df['I'][df['I'].idxmax() * (i+1)], s='x', ha='center', va='center')
#ax.set(xscale='log', yscale='log', xlabel=r'q/nm$^{-1}$', ylabel='I/u.a.')
fig.savefig('../saxs/exemplo_SAXS_indexacao.pdf')
plt.show()
