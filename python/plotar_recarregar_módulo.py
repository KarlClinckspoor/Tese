# coding: utf-8
def retry(dado):
    importlib.reload(RheoFCClass)
    fit = RheoFCClass.Fitter(dado, settings)
    fit.plot_error_graphs()
