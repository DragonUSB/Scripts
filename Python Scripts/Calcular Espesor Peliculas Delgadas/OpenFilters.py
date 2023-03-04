import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
sustrato = pd.read_csv('Calcular Espesor Peliculas Delgadas\OpenFilters_Data_Sustrato.csv', sep = ' ', header = 1)
datos = pd.read_csv('Calcular Espesor Peliculas Delgadas\OpenFilters_Data_Ge.csv', sep = ' ', header = 1)

sustrato_x = sustrato['wavelength(nm)']
sustrato_y = sustrato['T']

# Grabar archivo CSV
csvfile = {'Wavelength(nm)': sustrato_x, 'Transmission(%)': sustrato_y}
csvfile = pd.DataFrame(csvfile)
csvfile.to_csv('Calcular Espesor Peliculas Delgadas\OpenFilters_Sustrato.csv', sep = ',', index = False)

data_x = datos['wavelength(nm)']
data_y = datos['T']

# Normalizar la curva de transmisión con respecto al sustrato
# data_y_n = (data_y / sustrato_y)

# Grabar archivo CSV
csvfile = {'Wavelength(nm)': data_x, 'Transmission(%)': data_y}
csvfile = pd.DataFrame(csvfile)
csvfile.to_csv('Calcular Espesor Peliculas Delgadas\OpenFilters_Ge.csv', sep = ',', index = False)

# Graficas
plt.figure(figsize=(12, 6))
plt.title('Grafica de la Pelicula con OpenFilters')
plt.plot(sustrato_x, sustrato_y, label = 'Sustrato')
plt.plot(data_x, data_y, label = 'Pelicula')
# plt.plot(data_x, data_y_n, label = 'Pelicula Normalizada')
plt.legend(loc = 'center left')
plt.grid(True)
plt.show()