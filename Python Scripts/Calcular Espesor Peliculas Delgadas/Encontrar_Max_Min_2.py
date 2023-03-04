import matplotlib
# matplotlib.use('Agg') # Bypass the need to install Tkinter GUI framework
 
from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
 
# Generate random data.
# data_x = np.arange(start = 0, stop = 25, step = 1, dtype='int')
# data_y = np.random.random(25)*6

datos = pd.read_csv('Germanio E1EBE 5min (200nm-2500nm).csv', sep=",", header=1)
x = []
y = []
for i in range(1,2301):
    x.append(datos['Wavelength (nm).3'][i])
    y.append(datos['%T.3'][i])
data_x = np.array(x)
data_y = np.array(y)
data_x = np.flipud(data_x)
data_y = np.flipud(data_y)

#define spline
f1 = UnivariateSpline(data_x, data_y)

#create smooth line chart
# plt.plot(data_x, f1(data_x), '-', data_x, f2(data_x), '--')
plt.plot(data_x, data_y, 'ro', ms = 2.5)
plt.plot(data_x, f1(data_x), 'g')
f1.set_smoothing_factor(6.5)
plt.plot(data_x, f1(data_x), 'b')
plt.show()

data_y = f1(data_x)

# Find peaks(max).
peak_indexes = signal.argrelextrema(data_y, np.greater)
peak_indexes = peak_indexes[0]
peak_indexes_x = data_x[peak_indexes]
peak_indexes_x = peak_indexes_x.astype('int64')
i = 0
j = len(peak_indexes_x)
while i < j:
    if peak_indexes_x[i] <= 1000:
        peak_indexes_x = np.delete(peak_indexes_x, i)
        peak_indexes = np.delete(peak_indexes, i)
        i = 0
        j = len(peak_indexes_x)
    else:
        i = i + 1
 
# Find valleys(min).
valley_indexes = signal.argrelextrema(data_y, np.less)
valley_indexes = valley_indexes[0]
valley_indexes_x = data_x[valley_indexes]
valley_indexes_x = valley_indexes_x.astype('int64')
i = 0
j = len(valley_indexes_x)
while i < j:
    if valley_indexes_x[i] <= 1000:
        valley_indexes_x = np.delete(valley_indexes_x, i)
        valley_indexes = np.delete(valley_indexes, i)
        i = 0
        j = len(valley_indexes_x)
    else:
        i = i + 1

# Plot main graph.
(fig, ax) = plt.subplots()
ax.plot(data_x, data_y, label = "Signal")
 
# Plot peaks.
peak_x = peak_indexes_x
peak_y = data_y[peak_indexes]
ax.plot(peak_x, peak_y, marker = 'o', ms = 4, linestyle = 'dashed', color = 'green', label = "Peaks")
 
# Plot valleys.
valley_x = valley_indexes_x
valley_y = data_y[valley_indexes]
ax.plot(valley_x, valley_y, marker = 'o', ms = 4, linestyle = 'dashed', color = 'red', label = "Valleys")
 
 
# Save graph to file.
plt.title('Find peaks and valleys using argrelextrema()')
plt.legend(loc = 'best')
plt.show()
# plt.savefig('argrelextrema.png')