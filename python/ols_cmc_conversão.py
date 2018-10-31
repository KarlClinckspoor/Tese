import sympy as sp
n = sp.Symbol('n')
e = sp.Symbol('e')
G = sp.Symbol('G')

n_ave = dados_ME['Índice de refração'].mean()
e_ave = dados_ME['Cte dielétrica'].mean()
G_ave = dados_ME['Param Gordon'].mean()
cmc_ave = dados_ME['cmc/mM'].mean()
dh_ave = dados_ME['DeltaH/kJ.mol-1'].mean()

n_std = dados_ME['Índice de refração'].std()
e_std = dados_ME['Cte dielétrica'].std()
G_std = dados_ME['Param Gordon'].std()
cmc_std = dados_ME['cmc/mM'].std()
dh_std = dados_ME['DeltaH/kJ.mol-1'].std()

n_reg = results.params['Índice de refração']
e_reg = results.params['Cte dielétrica']
G_reg = results.params['Param Gordon']

expr_cmc = (
    (
      (n - n_ave) / n_std * n_reg +
      (e - e_ave) / e_std * e_reg +
      (G - G_ave) / G_std * G_reg
    ) * cmc_std + cmc_ave 
)