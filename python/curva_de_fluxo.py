import numpy as np
from scipy.optimize import curve_fit
from lmfit import minimize, Parameters

# Ajuste por curve\_fit
@staticmethod
def fit_lin(x, a, b):
    return a + b * x
# Algoritmo
for first_point in range(0, length//3, 1):
    for last_point in range(first_point + 3, length // 2, 1):
        GP_arr = np.array(self.GP[first_point:last_point + 1])
        Eta_arr = np.array(self.Eta[first_point:last_point + 1])
        try:
            popt, pcov = curve_fit(self.fit_lin, GP_arr, Eta_arr, p0=(30, 0),
                               bounds=(0, [self.VISC_LIMIT, 0.0001]))
        except Exception as e: 
            print(f'Error while using linear fit for file {self.filename}')
            print(traceback.format_exc())
            self.manip.logger(self.filename, 'Generic')

        perr = np.sqrt(np.diag(pcov))
        fittings.append((first_point, last_point, popt, perr))

if self.settings.LIN_SORTING_METHOD == 'by_error':
    fittings.sort(key=lambda x: np.log(x[3][0]))  # gets perr of eta\_0
elif self.settings.LIN_SORTING_METHOD == 'by_error_length':
    fittings.sort(key=lambda x: np.log(x[3][0]) / (x[1] - x[0]) ) # divides perr by last-first

# Ajuste por lmfit
# Definição das funções
@staticmethod
def fit_Carreau(GP, eta_0, eta_inf, GP_b, n):
    return eta_inf + (eta_0 - eta_inf) / (1 + (GP / GP_b) ** 2) ** (n / 2)

def residual(self, params, x, dataset):
    mod = self.fit_Carreau(x, params['eta_0'], params['eta_inf'], params['GP_b'], params['n'])
    resid = dataset - mod
    return resid
# Ajuste
params = Parameters()
SStot = sum((Eta - np.mean(Eta)) ** 2)
params.add('eta_0', 100, vary=True, min=0)
params.add('eta_inf', 1, vary=True, min=0)
params.add('GP_b', 5, vary=True, min=0)
params.add('n', 1, vary=True, min=0)
fit = minimize(self.residual, params, args=(GP, Eta))
params = [fit.params[par].value for par in fit.params]
param_errs = [fit.params[par].stderr for par in fit.params]
R2 = 1 - fit.chisqr / SStot
return params, param_errs, R2

