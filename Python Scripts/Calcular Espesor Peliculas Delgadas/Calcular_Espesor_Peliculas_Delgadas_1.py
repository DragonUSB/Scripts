from typing import ItemsView
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, UnivariateSpline

# Carga de datos
sustrato = pd.read_csv('Calcular Espesor Peliculas Delgadas\Sustrato Portamuestra.csv', sep = ",", header = 1)
datos = pd.read_csv('Calcular Espesor Peliculas Delgadas\Germanio E1EBE 5min (200nm-2500nm).csv', sep = ",", header = [0, 1])

sustrato_x = sustrato['Wavelength (nm).3'][0:2301]
sustrato_y = sustrato['%T.3'][0:2301]
sustrato_x = np.flipud(sustrato_x)
sustrato_y = np.flipud(sustrato_y)

# Define spline para el sutrato
f_sustrato = UnivariateSpline(sustrato_x, sustrato_y)
f_sustrato.set_smoothing_factor(6.5)
sustrato_y_s = f_sustrato(sustrato_x)

for p in range(2, 9):
    data_x = []
    data_y = []
    for j in range(0,2301):
        data_x.append(datos['Germanio N' + str(p - 1) + ' (200nm-2500nm)']['Wavelength (nm)'][j])
        data_y.append(datos['Unnamed: ' + str(2 * p + 1) + '_level_0']['%T'][j])
    data_x = np.array(data_x)
    data_y = np.array(data_y)
    data_x = np.flipud(data_x)
    data_y = np.flipud(data_y)

    # Define spline para la pelicula
    f_data = UnivariateSpline(data_x, data_y)
    f_data.set_smoothing_factor(6.5)
    data_y_s = f_data(data_x)

    q_u = np.zeros(data_y_s.shape)
    q_l = np.zeros(data_y_s.shape)
    q_m = np.zeros(data_y_s.shape)

    #Prepend the first value of (s) to the interpolating values. This forces the model to use the same starting point for both the upper and lower envelope models.
    u_x = [200, ]
    u_y = [data_y_s[0], ]

    l_x = [200, ]
    l_y = [data_y_s[0], ]

    #Detect peaks and troughs and mark their location in u_x,u_y,l_x,l_y respectively.
    for k in range(1, len(data_y_s)-1):
        if (np.sign(data_y_s[k] - data_y_s[k - 1]) == 1) and (np.sign(data_y_s[k] - data_y_s[k + 1]) == 1):
            u_x.append(k)
            u_y.append(data_y_s[k])

        if (np.sign(data_y_s[k] - data_y_s[k - 1]) == -1) and ((np.sign(data_y_s[k] - data_y_s[k + 1])) == -1):
            l_x.append(k)
            l_y.append(data_y_s[k])

    #Append the last value of (s) to the interpolating values. This forces the model to use the same ending point for both the upper and lower envelope models.
    u_x.append(len(data_y_s)-1)
    u_y.append(u_y[-1])
    i = 1
    j = len(u_y)
    while i < j:
        if u_x[i] <= 1000:
            u_y.pop(i)
            u_x.pop(i)
            i = 1
            j = len(u_y)
        else:
            i = i + 1
    peaks_x = data_x[u_x[1:len(u_x)-1]]
    peaks_y = data_y_s[u_x[1:len(u_x)-1]]
    for i in range(250, 950, 50):
        u_x.insert(i, i)
        u_y.insert(i, data_y_s[i])

    l_x.append(len(data_y_s)-1)
    l_y.append(l_y[-1])
    i = 1
    j = len(l_y)
    while i < j:
        if l_x[i] <= 1000:
            l_y.pop(i)
            l_x.pop(i)
            i = 1
            j = len(l_y)
        else:
            i = i + 1
    valleys_x = data_x[l_x[1:len(l_x)-1]]
    valleys_y = data_y_s[l_x[1:len(l_x)-1]]
    for i in range(250, 950, 50):
        l_x.insert(i, i)
        l_y.insert(i, data_y_s[i])

    #Fit suitable models to the data. Here I am using cubic splines, similarly to the MATLAB example given in the question.
    u_p = interp1d(u_x, u_y, kind = 'cubic', bounds_error = False, fill_value = 0.0)
    l_p = interp1d(l_x, l_y, kind = 'cubic', bounds_error = False, fill_value = 0.0)

    #Evaluate each model over the domain of (s)
    for k in range(0, len(data_y_s)):
        q_u[k] = u_p(k)
        q_l[k] = l_p(k)
        q_m[k] = (u_p(k) + l_p(k))/2

    # Graficas
    plt.figure(figsize=(12, 6))
    plt.title('Grafica de la Pelicula Germanio N' + str(p - 1))
    plt.plot(sustrato_x, sustrato_y, label = 'Sustrato')
    plt.plot(sustrato_x, sustrato_y_s, label = 'Sustrato con smoothing')
    plt.plot(data_x, data_y, label = 'Pelicula')
    plt.plot(data_x, data_y_s, label = 'Pelicula con smoothing')
    plt.plot(peaks_x, peaks_y, 'o', ms = 4, color = 'r', label = "Peaks")
    plt.plot(valleys_x, valleys_y, 'o', ms = 4, color = 'g', label = "Valleys")
    plt.plot(data_x, q_u, 'r', label = "Envelope High")
    plt.plot(data_x, q_l, 'g', label = "Envelope Low")
    plt.plot(data_x, q_m, 'b', label = "Envelope Mid")
    plt.legend(loc = 'center left')
    plt.grid(True)
    plt.show()