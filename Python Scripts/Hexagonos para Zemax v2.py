#Hexagonos para Zemax

from math import sqrt, cos, sin

file = open('testfile.uda', 'w')
Pi = 3.14159265359
DIA = int(input('COLOQUE LA LONGITUD DEL DIAMETRO DEL OBJETIVO (mm): '))
print ('Diametro del Objetivo = ' + str(DIA) + ' mm')
R = DIA / 2
print ('Radio del Objetivo = ' + str(R) + ' mm')
A = int(input('COLOQUE LA LONGITUD DEL SEGMENTO HEXAGONO (mm): '))
print ('Longitud del Segmento Hexagonal = ' + str(A) + ' mm')
B = (A / 2) * sqrt(3)
GAP = int(input('COLOQUE LA SEPARACION ENTRE LOS SEGMENTOS HEXAGONALES (mm): '))
print ('Separacion entre los Segmentos Hexagonales = ' + str(GAP) + ' mm')
L1 = (2 * B) + GAP
print ('L1 = ' + str(L1))
L2 = ((3 * L1) / 2) / 0.866
print ('L2 = ' + str(L2))
file.write('POL 0 0 ' + str(A) + ' 6 0\n')
for i in range(1,10):
		for j in range(30, 360, 60):
			X = i * L1 * cos((j * Pi) / 180)
			Y = i * L1 * sin((j * Pi) / 180)
			Y1 = sqrt((X * X) + (Y * Y))
			if (Y1 < (R * 0.9)):
				file.write('POL ' + str(X) + ' ' + str(Y) + ' ' + str(A) + ' 6 0\n')
				print ('X1 = ' + str(X) + '	Y1 = ' + str(Y))
for i in range(1, 10):
		for j in range(30, 360, 60):
			X = i * L2 * sin((j * Pi) / 180)
			Y = i * L2 * cos((j * Pi) / 180)
			Y1 = sqrt((X * X) + (Y * Y))
			if (Y1 < (R * 0.9)):
				file.write('POL ' + str(X) + ' ' + str(Y) + ' ' + str(A) + ' 6 0\n')
				print ('X1 = ' + str(X) + '	Y1 = ' + str(Y))
for i in range(1, 10):
	Y1 = (i + 1.5) * L1
	for j in range(0, 360, 60):
		for k in range(-1, 2, 2):
			X = (k * L1 * 0.866 * cos((j * Pi) / 180)) - (Y1 * sin((j * Pi) / 180))
			Y = (k * L1 * 0.866 * sin((j * Pi) / 180)) + (Y1 * cos((j * Pi) / 180))
			Y2 = sqrt((X * X) + (Y * Y))
			if (Y2 < (R * 0.9)):
				file.write('POL ' + str(X) + ' ' + str(Y) + ' ' + str(A) + ' 6 0\n')
				print ('X1 = ' + str(X) + '	Y1 = ' + str(Y))
for i in range(1, 10):
	Y1 = (i + 3) * L1
	for j in range(0, 360, 60):
		for k in range(-1, 2, 2):
			X = (k * 2 * L1 * 0.866 * cos((j * Pi) / 180)) - (Y1 * sin((j * Pi) / 180))
			Y = (k * 2 * L1 * 0.866 * sin((j * Pi) / 180)) + (Y1 * cos((j * Pi) / 180))
			Y2 = sqrt((X * X) + (Y * Y))
			if (Y2 < (R * 0.9)):
				file.write('POL ' + str(X) + ' ' + str(Y) + ' ' + str(A) + ' 6 0\n')
				print ('X1 = ' + str(X) + '	Y1 = ' + str(Y))
for i in range(1, 10):
	Y1 = (i + 4.5) * L1
	for j in range(0, 360, 60):
		for k in range(-1, 2, 2):
			X = (k * 3 * L1 * 0.866 * cos((j * Pi) / 180)) - (Y1 * sin((j * Pi) / 180))
			Y = (k * 3 * L1 * 0.866 * sin((j * Pi) / 180)) + (Y1 * cos((j * Pi) / 180))
			Y2 = sqrt((X * X) + (Y * Y))
			if (Y2 < (R * 0.9)):
				file.write('POL ' + str(X) + ' ' + str(Y) + ' ' + str(A) + ' 6 0\n')
				print ('X1 = ' + str(X) + '	Y1 = ' + str(Y))
file.close()
file = open('testfile.uda', 'r')
print (file.read())