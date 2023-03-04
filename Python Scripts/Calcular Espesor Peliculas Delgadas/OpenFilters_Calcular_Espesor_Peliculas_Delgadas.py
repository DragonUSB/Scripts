import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from scipy.interpolate import interp1d, UnivariateSpline
from prettytable import PrettyTable

# Carga de datos
sustrato = pd.read_csv('Calcular Espesor Peliculas Delgadas\OpenFilters_Sustrato.csv', sep = ",", header = 0)
datos = pd.read_csv('Calcular Espesor Peliculas Delgadas\OpenFilters_Ge.csv', sep = ",", header = 0)

sustrato_x = sustrato['Wavelength(nm)']
sustrato_y = sustrato['Transmission(%)']
sustrato_x = np.array(sustrato_x)
sustrato_y = np.array(sustrato_y)

# Define spline para el sutrato
# f_sustrato = UnivariateSpline(sustrato_x, sustrato_y)
# f_sustrato.set_smoothing_factor(0.001)
# sustrato_y_s = f_sustrato(sustrato_x)
sustrato_y_s = sustrato_y

# Calculo indice de refraccion sustrato
n_s = np.zeros(sustrato_y_s.shape)
for k in range(0, len(n_s)):
    n_s[k] = (1 / sustrato_y_s[k]) + sqrt((1 / sustrato_y_s[k]) - 1)

data_x = datos['Wavelength(nm)']
data_y = datos['Transmission(%)']
data_x = np.array(data_x)
data_y = np.array(data_y)

# Define spline para la pelicula
# f_data = UnivariateSpline(data_x, data_y)
# f_data.set_smoothing_factor(0.001)
# data_y_s = f_data(data_x)
data_y_s = data_y

#Prepend the first value of (s) to the interpolating values. This forces the model to use the same starting point for both the upper and lower envelope models.
u_x = []
u_y = []

l_x = []
l_y = []

#Detect peaks and troughs and mark their location in u_x,u_y,l_x,l_y respectively.
for k in range(1, len(data_y_s)-1):
    if (np.sign(data_y_s[k] - data_y_s[k - 1]) == 1) and (np.sign(data_y_s[k] - data_y_s[k + 1]) == 1):
        u_x.append(k)
        u_y.append(data_y_s[k])

    if (np.sign(data_y_s[k] - data_y_s[k - 1]) == -1) and ((np.sign(data_y_s[k] - data_y_s[k + 1])) == -1):
        l_x.append(k)
        l_y.append(data_y_s[k])

peaks_x = data_x[u_x[0:len(u_x)]]
peaks_y = data_y_s[u_x[0:len(u_x)]]

valleys_x = data_x[l_x[0:len(l_x)]]
valleys_y = data_y_s[l_x[0:len(l_x)]]

if u_x[0] < l_x[0]:
    inicio = u_x[0]
else:
    inicio = l_x[0]

if u_x[-1] > l_x[-1]:
    final = u_x[-1]
else:
    final = l_x[-1]

#Fit suitable models to the data. Here I am using cubic splines, similarly to the MATLAB example given in the question.
u_p = interp1d(u_x, u_y, kind = 'cubic', bounds_error = False, fill_value = 'extrapolate')
l_p = interp1d(l_x, l_y, kind = 'cubic', bounds_error = False, fill_value = 'extrapolate')

q_u = np.zeros(data_y_s.shape)
q_l = np.zeros(data_y_s.shape)
q_m1 = np.zeros(data_y_s.shape)
q_m2 = np.zeros(data_y_s.shape)

# #Evaluate each model over the domain of (s)
for k in range(inicio, final + 1):
    q_u[k] = u_p(k)
    q_l[k] = l_p(k)
    q_m1[k] = sqrt(u_p(k) * l_p(k))
    q_m2[k] = 2 * u_p(k) * l_p(k) / (u_p(k) + l_p(k))

u_l_x = u_x + l_x
u_l_x.sort()
u_l_x = np.flipud(u_l_x)
peaks_x = data_x[u_l_x[0:len(u_l_x)]]
peaks_y = q_u[u_l_x[0:len(u_l_x)]]
valleys_x = data_x[u_l_x[0:len(u_l_x)]]
valleys_y = q_l[u_l_x[0:len(u_l_x)]]

# Graficas
plt.figure(figsize=(12, 6))
plt.title('Grafica de la Pelicula Germanio OpenFilters')
plt.plot(sustrato_x, sustrato_y, label = 'Sustrato')
plt.plot(sustrato_x, sustrato_y_s, label = 'Sustrato con smoothing')
plt.plot(data_x, data_y, label = 'Pelicula')
plt.plot(data_x, data_y_s, label = 'Pelicula con smoothing')
plt.plot(peaks_x, peaks_y, 'o', ms = 4, color = 'r', label = 'T_max')
plt.plot(valleys_x, valleys_y, 'o', ms = 4, color = 'g', label = "T_min")
plt.plot(data_x[inicio:final], q_u[inicio:final], 'r', label = "Envelope High")
plt.plot(data_x[inicio:final], q_l[inicio:final], 'g', label = "Envelope Low")
plt.plot(data_x[inicio:final], q_m1[inicio:final], 'b', label = "Envelope Mid")
plt.plot(data_x[inicio:final], q_m2[inicio:final], label = "Envelope Mid")
plt.xlabel('Wavelength (nm)', fontsize = 14)
plt.ylabel('Transmission (%)', fontsize = 14)
plt.xlim(data_x[0] - 25, data_x[-1] + 25)
plt.legend(loc = 'center left')
plt.xticks(np.arange(data_x[0], data_x[-1] + 1, 100))
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.title('Grafica del Sustrato')
plt.plot(sustrato_x, n_s, label = 'Sustrato')
plt.xlabel('Wavelength (nm)', fontsize = 14)
plt.ylabel('Refractive Index', fontsize = 14)
# plt.xlim(data_x[0] - 25, data_x[-1] + 25)
plt.legend(loc = 'best')
# plt.xticks(np.arange(data_x[0], data_x[-1] + 1, 100))
plt.grid(True)
plt.show()

# Calculo del indice de refraccion de la pelicula
n_p_1 = np.zeros(len(u_l_x))
n_p_2 = np.zeros(len(u_l_x))
n_s = n_s[u_l_x[0:len(u_l_x)]]
for k in range(0, len(n_p_1)):
    N1 = 2 * n_s[k] * (peaks_y[k] - valleys_y[k]) / peaks_y[k] / valleys_y[k] + (n_s[k] ** 2 + 1) / 2
    n_p_1[k] = sqrt(N1 + sqrt(N1 ** 2 - n_s[k] ** 2))
    N2 = 2 * n_s[k]  / valleys_y[k] + (n_s[k] ** 2 + 1) / 2
    n_p_2[k] = sqrt(N2 + sqrt(N2 ** 2 - n_s[k] ** 2))

# Calculo de las distancias de la pelicula
d_p_1 = np.zeros(len(u_l_x))
d_p_2 = np.zeros(len(u_l_x))
d1 = d_p_1[0]
d2 = d_p_2[0]
print(peaks_x[1])
print(n_p_1)
for k in range(1, len(u_l_x) - 1):
    d_p_1[k] = (peaks_x[k] * peaks_x[k + 1]) / (2 * (peaks_x[k] * n_p_1[k + 1] - peaks_x[k +1] * n_p_1[k]))
    d1 = d_p_1[k] + d1
    d_p_2[k] = (peaks_x[k] * peaks_x[k + 1]) / (2 * (peaks_x[k] * n_p_2[k + 1] - peaks_x[k +1] * n_p_2[k]))
    d2 = d_p_2[k] + d2
d_prom_1 = d1 / (len(u_l_x) - 1)
d_prom_2 = d2 / (len(u_l_x) - 1)

# Calculo del numero de orden
m_p_1 = np.zeros(len(u_l_x))
m_p_2 = np.zeros(len(u_l_x))
for k in range(0, len(u_l_x)):
    m_p_1[k] = 2 * n_p_1[k] * d_prom_1 / peaks_x[k]
    m_p_2[k] = 2 * n_p_2[k] * d_prom_2 / peaks_x[k]

tabla = PrettyTable()
tabla.field_names = ['W (nm)', 'n_s', 'n_p_1', 'n_p_2', 'd_p_1', 'd_p_2', 'm_p_1', 'm_p_2']
for k in range(0, len(u_l_x)):
    tabla.add_row([peaks_x[k], n_s[k], n_p_1[k], n_p_2[k], d_p_1[k], d_p_2[k], m_p_1[k], m_p_2[k]])
tabla.float_format['W (nm)'] = ".2"
tabla.float_format['n_s'] = ".2"
tabla.float_format['n_p_1'] = ".2"
tabla.float_format['n_p_2'] = ".2"
tabla.float_format['d_p_1'] = ".2"
tabla.float_format['d_p_2'] = ".2"
tabla.float_format['m_p_1'] = ".2"
tabla.float_format['m_p_2'] = ".2"
print(tabla)
print('distancia promedio de la pelicula = ' + str(d_prom_1))
print('distancia promedio de la pelicula = ' + str(d_prom_2))