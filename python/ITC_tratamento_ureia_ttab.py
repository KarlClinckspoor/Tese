import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import re
from uncertainties import ufloat

def linear(x, slp, inter):
    return inter + slp * x

c_surf = 12.107     # mmol/L
V_cela = 240e-6     # L

conc_ur = re.compile(r'\d?\d\dmM')
fig, ax = plt.subplots(1, 1, figsize=(9, 6))
colors = [f'C{i}' for i in range(10, -1, -1)]

arquivos = glob.glob(r'./csv/convertidos/*csv')
brancos = [i for i in arquivos if 'ctrl' in i]
experimentos = [i for i in arquivos if 'ctrl' not in i]
experimentos = [i for i in experimentos if ' - 2' not in i]
# continua ...