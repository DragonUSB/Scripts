import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("S-BK7-6C-ZrO2-SiO2.txt", header=1, delim_whitespace=True)
LR = data.ix[:,0]
ER = data.ix[:,1]
TR = data.ix[:,2]*100
print (data)
print (ER)
print (TR)
datos = [i for i in range(6)]
plt.figure()
for i in range(6):
	datos[i] = data[data['layer'] == i]
	print (datos[i])
	if i%2 == 0:
		color = 'r'
	else:
		color = 'b'
	plt.subplot()
	plt.plot(datos[i]['thickness(nm)'], datos[i]['T']*100, color)
inter = data.drop_duplicates('layer', keep='first')
print (inter)
maximos = [i for i in range(6)]
minimos = [i for i in range(6)]
for i in range(6):
	maximos[i] = datos[i][datos[i]['T'] == pd.DataFrame.max(datos[i]['T'])]
	minimos[i] = datos[i][datos[i]['T'] == pd.DataFrame.min(datos[i]['T'])]
	print (maximos[i])
	print (minimos[i])
plt.subplot()
plt.plot(inter['thickness(nm)'], inter['T']*100, marker='.', linestyle='None', color='k')
plt.minorticks_on()
plt.grid(True, which=u'both')
plt.title('Titulo', fontweight='bold')
plt.text(max(ER), -10,'S-BK7-6C-ZrO2-SiO2', horizontalalignment='center', verticalalignment='center', fontweight='bold')
plt.xlim(xmin=0)
plt.ylim(0,100)
plt.ylabel('Transmitancia (%)', fontweight='bold')
plt.xlabel('Espesor (nm)', fontweight='bold')
plt.savefig('S-BK7-6C-ZrO2-SiO2.pdf', dpi = 300, orientation = 'landscape', format= 'pdf')
plt.show()
