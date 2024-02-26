import random
import pandas as pd
from openpyxl.workbook import Workbook 

Personal = ['Bernardo Conquet', 'Miguel Palmera', 'Jairo Peña', 'Henry Flores', 'Jairo Prieto', 'Juan Gil', 'Jackson Diaz', 'Anderson Ramirez', 'Miguel Contreras']
Mañana = ['Bernardo Conquet', 'Jairo Peña', 'Henry Flores', 'Jairo Prieto', 'Jackson Diaz', 'Anderson Ramirez']
Tarde = ['Bernardo Conquet', 'Miguel Palmera', 'Henry Flores', 'Jairo Prieto', 'Juan Gil', 'Miguel Contreras']
Vacaciones = ['Anderson Ramirez', 'Miguel Contreras']

Semana_Mañana = []
Semana_Tarde = []

for i in range(5):
    m = True
    t = True
    while m:
        M = random.randint(0, len(Personal)-1)
        if (Personal[M] in Mañana) and (Personal[M] not in Semana_Mañana) and (Personal[M] not in Vacaciones):
            Semana_Mañana.append(Personal[M])
            m = False
        else:
            m = True

    while t:
        T = random.randint(0, len(Personal)-1)
        if (Personal[T] in Tarde) and (Personal[T] not in Semana_Tarde) and (Personal[T] not in Vacaciones):
            Semana_Tarde.append(Personal[T])
            t = False
        else:
            t = True

print(Semana_Mañana)
print(Semana_Tarde)

Semana1 = pd.DataFrame([Semana_Mañana, Semana_Tarde],
                   index=['row 1', 'row 2'],
                   columns=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'])
Semana1.to_excel("Python Scripts/Cronograma_Vigilancia.xlsx")