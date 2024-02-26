import random

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