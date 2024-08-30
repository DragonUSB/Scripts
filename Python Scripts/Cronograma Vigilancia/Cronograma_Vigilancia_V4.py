import datetime
import random
import csv

def generar_calendario_llaves(ano, mes, trabajadores, vacaciones):
  """
  Genera un calendario mensual de entrega y recepción de llaves considerando las vacaciones de 12 trabajadores,
  solo mostrando eventos de lunes a viernes.

  Args:
    ano: Año del calendario.
    mes: Mes del calendario (1-12).
    trabajadores: Lista con los nombres de los 12 trabajadores.
    vacaciones: Diccionario donde la clave es el nombre del trabajador y el valor es una lista con tuplas 
    representando el inicio y fin de sus vacaciones [(inicio1, fin1), (inicio2, fin2), ...].
  """

  # Crear un rango de fechas para el mes
  primer_dia_mes = datetime.date(ano, mes, 1)
  if mes == 12:
    ultimo_dia_mes = primer_dia_mes.replace(year = ano +1, month = 1, day = 1) - datetime.timedelta(days = 1)
  else:
    ultimo_dia_mes = primer_dia_mes.replace(month = primer_dia_mes.month + 1, day = 1) - datetime.timedelta(days = 1)

  # Calcular el número de trabajadores
  num_trabajadores = len(trabajadores)

  trabajador_entrega_ant = ['0', '0']
  trabajador_recibe_ant = ['0', '0']
  datos = list()
  
  # Iterar sobre cada día del mes
  for dia in range(1, ultimo_dia_mes.day + 1):
    fecha = primer_dia_mes + datetime.timedelta(days = dia - 1)
    weekday = fecha.weekday()  # Obtener el día de la semana (0: lunes, 6: domingo)

    # Filtrar solo días de lunes a viernes (0 a 4)
    if 0 <= weekday <= 4:

      m = True
      while m:
        # Calcular índice del trabajador que entrega
        indice_entrega = random.randint(0, num_trabajadores - 1)

        # Calcular índice del trabajador que recibe
        indice_recibe = random.randint(0, num_trabajadores - 1)

        # Verificar si hay vacaciones
        trabajador_entrega = trabajadores[indice_entrega]
        trabajador_recibe = trabajadores[indice_recibe]
        if fecha in vacaciones.get(trabajador_entrega, []) or trabajador_entrega == trabajador_recibe:
          m = True
        elif fecha in vacaciones.get(trabajador_recibe, []) or trabajador_entrega == trabajador_recibe:
          m = True
        elif trabajador_entrega == trabajador_entrega_ant[-1] or trabajador_entrega == trabajador_entrega_ant[-2]:
          m = True
        elif trabajador_recibe == trabajador_recibe_ant[-1] or trabajador_recibe == trabajador_recibe_ant[-1]:
          m = True
        else:
          print(f"{fecha.strftime('%d/%m/%Y')}: {trabajador_recibe} recibe las llaves a las 8:00 a.m. y {trabajador_entrega} entrega las llaves a las 3:00 p.m.")
          m =False
          trabajador_entrega_ant.append(trabajador_entrega)
          trabajador_recibe_ant.append(trabajador_recibe)
          data = [weekday,fecha.strftime('%d/%m/%Y'),trabajador_recibe,trabajador_entrega]
          datos.append(data)
          
  with open("/home/bernardoconquet/Documentos/GitHub/Scripts/Python Scripts/Cronograma Vigilancia/Cronograma_Vigilancia.csv", "w", newline ='') as csvfile:
    wr = csv.writer(csvfile, dialect='excel', delimiter=',')
    wr.writerows(datos)

def vacaciones_trabajadores(trabajadores, vacaciones_trabajadores):
  # Calcular el número de trabajadores
  num_trabajadores = len(trabajadores)
  vacaciones ={}
  for t in range(num_trabajadores):
    trabajador_vac = trabajadores[t]
    fecha = vacaciones_trabajadores.get(trabajador_vac, [])
    # print(f'{trabajador_vac} de vacaciones desde el {fecha[0]} al {fecha[1]}')
    fechas_vac = []
    ano_vac = fecha[0].year
    mes_vac = fecha[0].month
    dia_vac = fecha[0].day
    diferencia = fecha[1] - fecha[0]
    for dia in range(1, diferencia.days + 2):
      fecha = datetime.date(ano_vac, mes_vac, dia_vac) + datetime.timedelta(days = dia - 1)
      fechas_vac.append(fecha)
    # print(f'{trabajador_vac}: {len(fechas_vac)}')
    # print(f'{trabajador_vac}: {fechas_vac}')
    vacaciones[trabajador_vac] = fechas_vac
  # print(vacaciones)
  return vacaciones

# Ejemplo de uso:
trabajadores = ['Bernardo Conquet', 'Miguel Palmera', 'Jairo Peña', 'Henry Flores', 'Jairo Prieto', 'Juan Gil', 'Anderson Ramirez', 'Miguel Contreras']
vac_trabajadores = {
  'Miguel Palmera': [datetime.date(2024, 7, 1), datetime.date(2024, 7, 1)],
  'Jairo Prieto': [datetime.date(2024, 7, 1), datetime.date(2024, 7, 1)],
  'Juan Gil': [datetime.date(2024, 7, 1), datetime.date(2024, 7, 1)],
  'Anderson Ramirez': [datetime.date(2024, 7, 1), datetime.date(2024, 7, 1)],
  'Miguel Contreras': [datetime.date(2024, 7, 1), datetime.date(2024, 7, 1)],
  'Jairo Peña': [datetime.date(2024, 7, 1), datetime.date(2024, 7, 1)],
  'Bernardo Conquet':[datetime.date(2024, 8, 12), datetime.date(2024, 9, 27)],
  'Henry Flores':[datetime.date(2024, 8, 12), datetime.date(2024, 10, 4)]
}

Ano = datetime.datetime.now().year
Mes = int(input("Colocar el Mes(1-12): "))
vacaciones = vacaciones_trabajadores(trabajadores, vac_trabajadores)
generar_calendario_llaves(Ano, Mes, trabajadores, vacaciones)