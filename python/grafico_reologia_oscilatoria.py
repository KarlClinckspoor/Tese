import locale
locale.setlocale(locale.LC_ALL, '')
import matplotlib as mpl
mpl.rcParams.update({'mathtext.fontset':'dejavusans'})
mpl.rcParams['axes.formatter.use_locale'] = True
mpl.rcParams.update({'font.size': 26, 'text.usetex':False})
import os
import matplotlib.pyplot as plt
import numpy as np

def gamma(gamma0, omega, t):
    gamma = gamma0 * np.cos(omega * t)
    return gamma

def tau(tau0, omega, theta, t):
    tau = tau0 * np.cos(omega * t - theta)
    return tau

omega = 5
gamma0 = 5
tau0 = 1
t = np.linspace(3 * np.pi/(2 * omega), 7 * np.pi/(2 * omega), 1000)
theta = np.pi/6

y_gamma = gamma(gamma0, omega, t)

fig, ax4 = plt.subplots(nrows=1, ncols=1, figsize=(10.8, 7.2))
ax1 = ax4.twinx()

valid_is = [0, 25, 50, 75, 100]
for i in range(0, 201, 1):
    if i < 100:
        perc = i/100
        tau_elast = tau0 - perc * tau0
        tau_visc = tau0 - tau_elast
        title = '{0}% elástico, {1}% viscoso'.format(100-i, i)
    if i >= 100:
        perc = (i-100)/100
        tau_visc = tau0 - perc * tau0
        tau_elast = tau0 - tau_visc
        title = '{0}% elástico, {1}% viscoso'.format(i-100, 100 - (i - 100))
# continua ...