from numpy import array, dtype, sign, zeros
from scipy.interpolate import interp1d, UnivariateSpline
from matplotlib.pyplot import plot, show, grid, legend
import numpy as np
import pandas as pd

#This is your noisy vector of values.
datos = pd.read_csv('Calcular Espesor Peliculas Delgadas\Germanio E1EBE 5min (200nm-2500nm).csv', sep = ",", header = 1)
x = []
y = []
for i in range(1,2301):
    x.append(datos['Wavelength (nm).3'][i])
    y.append(datos['%T.3'][i])
t = np.array(x)
s = np.array(y)
t = np.flipud(t)
s = np.flipud(s)

#define spline
f1 = UnivariateSpline(t, s)
f1.set_smoothing_factor(6.5)
s = f1(t)
print(s)

q_u = zeros(s.shape)
q_l = zeros(s.shape)
q_m = zeros(s.shape)

#Prepend the first value of (s) to the interpolating values. This forces the model to use the same starting point for both the upper and lower envelope models.
u_x = [200, ]
u_y = [s[0], ]

l_x = [200, ]
l_y = [s[0], ]

#Detect peaks and troughs and mark their location in u_x,u_y,l_x,l_y respectively.
for k in range(1, len(s)-1):
    if (sign(s[k] - s[k - 1]) == 1) and (sign(s[k] - s[k + 1]) == 1):
        u_x.append(k)
        u_y.append(s[k])

    if (sign(s[k] - s[k - 1]) == -1) and ((sign(s[k] - s[k + 1])) == -1):
        l_x.append(k)
        l_y.append(s[k])

#Append the last value of (s) to the interpolating values. This forces the model to use the same ending point for both the upper and lower envelope models.
u_x.append(len(s)-1)
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
peaks_x = t[u_x[1:5]]
peaks_y = s[u_x[1:5]]
for i in range(250, 950, 50):
    u_x.insert(i, i)
    u_y.insert(i, s[i])

l_x.append(len(s)-1)
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
valleys_x = t[l_x[1:5]]
valleys_y = s[l_x[1:5]]
for i in range(250, 950, 50):
    l_x.insert(i, i)
    l_y.insert(i, s[i])

#Fit suitable models to the data. Here I am using cubic splines, similarly to the MATLAB example given in the question.
u_p = interp1d(u_x, u_y, kind = 'cubic', bounds_error = False, fill_value = 0.0)
l_p = interp1d(l_x, l_y, kind = 'cubic', bounds_error = False, fill_value = 0.0)

#Evaluate each model over the domain of (s)
for k in range(0, len(s)):
    q_u[k] = u_p(k)
    q_l[k] = l_p(k)
    q_m[k] = (u_p(k) + l_p(k))/2

#Plot everything
plot(t, s, linestyle = 'dashed', label = "Signal")
plot(peaks_x, peaks_y, 'o', ms = 4, color = 'r', label = "Peaks")
plot(valleys_x, valleys_y, 'o', ms = 4, color = 'g', label = "Valleys")
plot(t, q_u, 'r', label = "Envelope High")
plot(t, q_l, 'g', label = "Envelope Low")
plot(t, q_m, 'b', label = "Envelope Mid")
grid(True)
legend(loc = 'best')
show()