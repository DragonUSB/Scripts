import numpy as np
import pandas as pd
import scipy.interpolate
import matplotlib.pyplot as pt

datos = pd.read_csv('Germanio E1EBE 5min (200nm-2500nm).csv', sep=",", header=1)
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
f1 = scipy.interpolate.UnivariateSpline(t, s)
f1.set_smoothing_factor(6.5)
s = f1(t)

u_x = [0]
u_y = [s[0]]

l_x = [0]
l_y = [s[0]]

#Detect peaks and troughs and mark their location in u_x,u_y,l_x,l_y respectively.
for k in range(2,len(s)-1):
    if s[k] >= max(s[:k-1]):
        u_x.append(t[k])
        u_y.append(s[k])

for k in range(2,len(s)-1):
    if s[k] <= min(s[:k-1]):
        l_x.append(t[k])
        l_y.append(s[k])

u_p = scipy.interpolate.interp1d(u_x, u_y, kind = 'cubic', bounds_error = False, fill_value=0.0)
l_p = scipy.interpolate.interp1d(l_x, l_y, kind = 'cubic', bounds_error = False, fill_value=0.0)

q_u = np.zeros(s.shape)
q_l = np.zeros(s.shape)
for k in range(0,len(s)):
    q_u[k] = u_p(t[k])
    q_l[k] = l_p(t[k])

pt.plot(t,s)
pt.plot(t, q_u, 'r')
pt.plot(t, q_l, 'g')
pt.grid(True)
pt.show()