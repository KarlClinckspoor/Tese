import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_decomposition import PLSRegression
Cores = {'Água':'k', 'Glicerina':'#e67300', 'Sacarose':'#00b300', 'Ureia':'#ff0000', '1,3BD':'#0000ff', 'DMSO':'#bf00ff'}
Simbolos = {'Água':'s', 'Glicerina':'o', 'Sacarose':'<', 'Ureia':'>', '1,3BD':'v', 'DMSO':'^'}
def_markersize = 10

dados_ME = pd.read_csv(r'./dados experimentais/cmc_ttab/CMC_DH.csv', sep=';', decimal=',')
X = dados_ME[['Índice de refração', 'Cte dielétrica', 'Param Gordon']]
Y1 = dados_ME['cmc/mM']
Y2 = dados_ME['DeltaH/kJ.mol-1']

pls = PLSRegression(n_components=2)
pls.fit(X, Y1)
Y_pred = pls.predict(X)

fig, ax = plt.subplots(1, 1, figsize=(9,6))

for comp in dados_ME['Composto'].unique():
    mascara = dados_ME['Composto'] == comp
    ax.plot(Y1[mascara], Y_pred[mascara], color=Cores[comp], linewidth=0, marker=Simbolos[comp], markersize=def_markersize, label=comp, alpha=0.7)

r = np.linspace(Y1.min(), Y1.max())
ax.plot(r, r, color='k', ls='--')  # Reta 1:1

ax.set(xlabel='CMC observada/mmol.L$^{-1}$', ylabel='CMC prevista/mmol.L$^{-1}$')
ax.legend()
ax.grid()

for i, conc in enumerate(dados_ME['Concentração (% m/m)']):
    comp = dados_ME['Composto'][i]
    ax.text(Y1[i], Y_pred[i]-0.2, s=conc, color=Cores[comp], ha='center', va='top')

plt.show()