from lmfit import minimize, Parameters
import pandas as pd
import numpy as np

def maxwell_elast(w, G0, lambda1):
    return G0 * (lambda1 * w) ** 2 / (1 + (lambda1 * w) ** 2)

def maxwell_visc(w, G0, lambda1):
    return G0 * (lambda1 * w) / (1 + (lambda1 * w) ** 2)

def ajuste_Maxwell(w, G1, G2, chutes=[10, 1]):
    datasets = [G1, G2]
    params = Parameters()
    params.add('G0', chutes[0], vary=True, min=0)
    params.add('tr', chutes[1], vary=True, min=0)

    def residual_maxwell(params, x, datasets):
        model_elast = maxwell_elast(x, params['G0'], params['tr'])
        model_visc = maxwell_visc(x, params['G0'], params['tr'])

        resid1 = datasets[0] - model_elast
        resid2 = datasets[1] - model_visc
        return np.concatenate((resid1, resid2))

    fit = minimize(residual_maxwell, params, args=(w, datasets))
    return fit

df = pd.read_csv('OF_água100.csv', encoding='utf8', delimiter=';', decimal=',', names=['w', 'G1', 'G2', 'T'], header=1)
pontos = {'OF_água100.csv': 26}  # ...
final = pontos['OF_água100.csv']

dataset_x = df['w'].iloc[0:final]
dataset_elast = df['G1'].iloc[0:final]
dataset_visc = df['G2'].iloc[0:final]

fit = ajuste_Maxwell(dataset_x, dataset_elast, dataset_visc)
G0_fit = fit.params['G0']
tr_fit = fit.params['tr']

SSTcor_elast = sum((dataset_elast - np.mean(dataset_elast)) ** 2)
SSTcor_visc = sum((dataset_visc - np.mean(dataset_visc)) ** 2)

modelo_elast = maxwell_elast(dataset_x, G0_fit, tr_fit)
modelo_visc = maxwell_visc(dataset_x, G0_fit, tr_fit)

SSres = fit.chisqr
SSTcor = SSTcor_elast + SSTcor_visc
R2 = 1 - SSres / SSTcor

MQres = SSres / (final - 2)
MQTcor = SSTcor / (final - 1)
R2lin = 1 - MQres / MQTcor