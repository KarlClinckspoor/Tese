import statsmodels.api as sm

Y1_AS = (Y1 - Y1.mean()) / Y1.std()
Y2_AS = (Y2 - Y2.mean()) / Y2.std()
X_AS =  (X - X.mean()) / X.std()

results = sm.OLS(Y1_AS, X_AS).fit()

Y_modelo = results.params[0] * X_AS.iloc[:,0] + results.params[1] * X_AS.iloc[:,1] + results.params[2] * X_AS.iloc[:,2]
Y_modelo_revertido = Y_modelo * Y1.std() + Y1.mean()
fig, ax = plt.subplots(1, 1, figsize=(9,6))

for comp in dados_ME['Composto'].unique():
    mascara = dados_ME['Composto'] == comp
    ax.plot(Y1[mascara], Y_modelo_revertido[mascara], color=Cores[comp], linewidth=0, marker=Simbolos[comp], markersize=def_markersize, label=comp)

for i, conc in enumerate(pls_pirouette_cmc['Conc']):
    comp = dict_tabela_pls[pls_pirouette_cmc['Comp'][i]]
    if conc == 100:
        conc = '0'
    ax.text(Y1[i], Y_modelo_revertido[i]-0.2, s=conc, color=Cores[comp], ha='center', va='top')
    
SStot = np.sum( (Y1 - Y1.mean()) ** 2 )
chisqr = np.sum( (Y1 - Y_modelo_revertido) ** 2 )
R2 = 1 - chisqr / SStot

min_cmc = Y1.min()
max_cmc = Y1.max()
r = np.linspace(min_cmc, max_cmc)
ax.plot(r, r, color='k', ls='--', label='1:1')

z = np.polyfit(Y1, Y_modelo_revertido, 1)
ax.plot(r, z[0] * r + z[1], color='r', ls='--', label=rf'$R^2$={R2:.2f}')
ax.set(xlabel='CMC medida/mmol.L$^{-1}$', ylabel='CMC prevista/mmol.L$^{-1}$')
ax.legend()
ax.grid()