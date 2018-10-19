import locale
locale.setlocale(locale.LC_ALL, '')

import matplotlib as mpl
mpl.rcParams.update({'font.size': 14, 'text.usetex':False})
mpl.rcParams.update({'mathtext.fontset':'dejavusans'})
mpl.rcParams['axes.formatter.use_locale'] = True

dict_simbolos = {'Água':'o',
                 'Sacarose':'s',
                 'Glicerina':'<',
                 'DMSO':'>',
                 '1,3BD':'^',
                 'Ureia':'v'}
