import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

def I_esfera (q, R):
    qR = q * R
    return ( 3 * ( np.sin(qR) - qR * np.cos(qR) ) / (qR ** 3)  ) ** 2

q = np.linspace(6E-3, 2, num=300)
R = 7
Int = I_esfera(q, R)
fig, ax = plt.subplots(1, 1, figsize=(9,6))

ax.plot(q * R, Int/Int.max())
ax.set(yscale='log', ylabel = 'Intensidade de espalhamento normalizada', xlabel='qR', ylim=(1E-5, 1.1), xlim=(0, 14))