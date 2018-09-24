# %% Cela 0

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# %% Cela 1

filename = 'Exp3_t_int'
length = 570
colnames = ['t'] + [f'l{i}' for i in range(0,length)]
dados = pd.read_csv(f'{filename}.csv', sep=' ', decimal=',', names=colnames)
lambdas = pd.read_csv('lambdas.txt', sep=' ', decimal=',', names=['lambda'])

# %% Cela 2

num_start = 0
num_stop = -1
plt.scatter(range(0,len(dados['l229'].iloc[num_start:num_stop])), dados['l229'].iloc[num_start:num_stop])
plt.xlabel('Pto num (tempo = Pto * 6ms)')
plt.ylabel('Intensidade')
plt.gcf().set_figwidth(12)
plt.savefig(filename+'_red.png')

# %% Cela 3

intensidades = dados.iloc[:, 1:]
tempos = dados.iloc[:,0]
df = pd.DataFrame([tempos, dados['l229'] / max(dados['l229'])])
df.T.to_csv(file.split('_')[0] + '_importante_norm.csv', sep=';', index=False)

fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(9,6))
im = ax1.imshow(intensidades.T, aspect=13)

xlabels = np.linspace(tempos.values[0], tempos.values[-1], num=6)
xlabels = np.concatenate(([0], xlabels))
xlabels = ['{:3.0f}'.format(i) for i in xlabels]

ylabels = np.linspace(350.328184, lambdas.values[-1], num=6)
ylabels = np.concatenate(([0], ylabels))
ylabels = ['{:3.2f}'.format(i) for i in ylabels]

ax1.set(xticklabels=xlabels, yticklabels=ylabels, xlabel='tempo/ms', ylabel=r'$\lambda$\nm', title=filename)
fig.colorbar(im, orientation='vertical', fraction=0.046, pad=0.04)

fig.tight_layout()
fig.savefig(filename.split('_')[0] + '_mapa.png', dpi=150)