import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


capas = input('Cantidad de Capas: ')
materiales = input('Cuantos materiales se van a depositar: ')
documento = input('Nombre del Archivo: ')
datos = pd.read_csv(documento + '.txt', header=1, delim_whitespace=True)
L = datos.ix[:,0]
E = datos.ix[:,1]
T = datos.ix[:,2]*100
print(datos)
print (E)
print (T)
titulo = input('Escriba el Titulo de la Grafica: ')
plt.figure()
plt.plot(E, T, 'r')
plt.text(max(E), -10,documento, horizontalalignment='center', verticalalignment='center', fontweight='bold')
plt.minorticks_on()
plt.grid(True, which=u'both')
plt.title(titulo, fontweight='bold')
plt.xlim(xmin=0)
plt.ylim(0,100)
plt.ylabel('Tramitancia (%)', fontweight='bold')
plt.xlabel('Espesor (nm)', fontweight='bold')
apdf = input('Nombre del Archivo PDF: ')
plt.savefig(apdf + '.pdf', dpi = 300, orientation = 'landscape', format= 'pdf')
plt.show()