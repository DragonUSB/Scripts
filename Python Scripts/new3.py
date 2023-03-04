import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

recubrimiento = input('Tipo de Recubrimiento: ')
longref = input('Longitud de Referencia: ')
sustrato = input('Sustrato: ')
capas = input('Cantidad de Capas: ')
materiales = input('Cuantos materiales se van a depositar: ')
m = [i for i in range(int(materiales))]
for i in m:
	m[i] = input('Nombre del Material ' + str(i + 1) + ': ')
documento = input('Nombre del Archivo: ')
datos = pd.read_csv(documento + '.txt', header=1, delim_whitespace=True)
LR = datos.ix[:,0]
ER = datos.ix[:,1]
TR = datos.ix[:,2]*100
E = np.zeros((len(LR),int(capas)-1))
for i in range(int(capas)-1):
	for j in range(len(LR)):
		if LR[j] == i:
			E[i,j] = ER[j]
		else:
			E[i,j] = 0
print (datos)
print (ER)
print (TR)
print (E)
titulo = input('Escriba el Titulo de la Grafica: ')
plt.figure()
plt.plot(ER, TR, 'r')
plt.text(max(ER), -10,documento, horizontalalignment='center', verticalalignment='center', fontweight='bold')
plt.minorticks_on()
plt.grid(True, which=u'both')
plt.title(titulo, fontweight='bold')
plt.xlim(xmin=0)
plt.ylim(0,100)
plt.ylabel('Transmitancia (%)', fontweight='bold')
plt.xlabel('Espesor (nm)', fontweight='bold')
plt.savefig(documento + '.pdf', dpi = 300, orientation = 'landscape', format= 'pdf')
plt.show()