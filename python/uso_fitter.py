from RheoFCClass import Fitter
from Settings import Settings

settings = Settings()
# Output:
# Settings file not found. Loading defaults.
# Creating a new settings file with the defaults
settings.edit_settings() # Configura de acordo com o que se deseja fazer

fit = Fitter('Dado-exemplo.csv', settings)
# Output:
# linear: Intercept=149.10000223652688 +- 1.3686335845677013 (...)
# Dado-exemplo.csv: Intercept=149.43833082940597 +- 0.9443341152601855 (...)

fit.plot_error_graphs()