import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, UnivariateSpline

# example data with peaks:
# x = np.linspace(-1,3,1000)
# data = -0.1*np.cos(12*x)+ np.exp(-(1-x)**2)

datos = pd.read_csv('Calcular Espesor Peliculas Delgadas\Germanio E1EBE 5min N1 (200nm-2500nm).csv', sep = " ", header = 0)
x = datos['Wavelength(nm)']
data = datos['Transmission(%)']
x = np.flipud(x)
data = np.flipud(data)

# Define spline para la pelicula
data = UnivariateSpline(x, data)
data.set_smoothing_factor(6.5)
data = data(x)

f1 = interp1d(x, data)
f2 = interp1d(x, data, kind = 'cubic')

#     ___ detection of local minimums and maximums ___

a = np.diff(np.sign(np.diff(data))).nonzero()[0] + 1               # local min & max
b = (np.diff(np.sign(np.diff(data))) > 0).nonzero()[0] + 1         # local min
c = (np.diff(np.sign(np.diff(data))) < 0).nonzero()[0] + 1         # local max
# +1 due to the fact that diff reduces the original index number

# plot
plt.figure(figsize=(12, 6))
plt.plot(x, data, color = 'grey')
plt.plot(x[b], data[b], "o", label = "min", color = 'r')
plt.plot(x[c], data[c], "o", label = "max", color = 'b')
plt.show()


plt.figure(figsize=(12, 6))
plt.plot(x, f1(x), '-', x, f2(x), '--')
plt.legend(['linear', 'cubic'], loc = 'best')
plt.show()