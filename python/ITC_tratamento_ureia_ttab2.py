# ... continuação
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
    ax.plot(x, y, linewidth=0, markersize=5, marker='o', label=nome, color=color)
    ax.errorbar(x, y_vals, yerr=y_errs, color=color, capsize=3)

ax.set(xlabel='Concentração de ureia na cela/mol.L$^{-1}$', ylabel=r'$\Delta H$/J.mol$^{-1}$ de surfactante na cela')
ax.legend(ncol=2, fontsize='small', title='Conc. Ureia')
ax.set_title('TTAB 12 mmol.L$^{-1}$', loc='right')