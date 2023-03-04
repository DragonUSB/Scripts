import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
sustrato = pd.read_csv('Calcular Espesor Peliculas Delgadas\Sustrato Portamuestra.csv', sep = ",", header = 1)
datos = pd.read_csv('Calcular Espesor Peliculas Delgadas\Germanio E1EBE 5min (200nm-2500nm).csv', sep = ",", header = [0, 1])

i = 0
for item in sustrato['Wavelength (nm).3']:
    if item == 999:
        i = i
        break
    i = i + 1

sustrato_x = sustrato['Wavelength (nm).3'][0:i]
sustrato_y = sustrato['%T.3'][0:i]

# Grabar archivo CSV
csvfile = {'Wavelength(nm)': sustrato_x, 'Transmission(%)': sustrato_y}
csvfile = pd.DataFrame(csvfile)
csvfile.to_csv('Calcular Espesor Peliculas Delgadas\Sustrato.csv', sep = ',', index = False)
    

for p in range(2, 9):
    data_x = datos['Germanio N' + str(p - 1) + ' (200nm-2500nm)']['Wavelength (nm)'][0:i]
    data_y = datos['Unnamed: ' + str(2 * p + 1) + '_level_0']['%T'][0:i]

    # Normalizar la curva de transmisión con respecto al sustrato
    data_y_n = (data_y / sustrato_y) * 100

    # Grabar archivo CSV
    csvfile = {'Wavelength(nm)': data_x, 'Transmission(%)': data_y_n}
    csvfile = pd.DataFrame(csvfile)
    csvfile.to_csv('Calcular Espesor Peliculas Delgadas\Germanio E1EBE 5min N' + str(p - 1) + ' (200nm-2500nm).csv', sep = ',', index = False)
    
    # Graficas
    plt.figure(figsize=(12, 6))
    plt.title('Grafica de la Pelicula Germanio N' + str(p - 1))
    plt.plot(sustrato_x, sustrato_y, label = 'Sustrato')
    plt.plot(data_x, data_y, label = 'Pelicula')
    plt.plot(data_x, data_y_n, label = 'Pelicula Normalizada')
    plt.legend(loc = 'center left')
    plt.grid(True)
    plt.show()