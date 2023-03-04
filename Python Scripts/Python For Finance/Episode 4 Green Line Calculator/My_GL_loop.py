import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

now = dt.datetime.now()
stock = input('Enter the stock symbol : ') 
while stock != 'quit':
    datos = pd.read_csv(stock + '_1d.csv', sep = ',')
    datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
    datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
    datos.set_index('Close_Timestamp', inplace = True)
    datos.drop(datos[datos['Volume'] < 1000].index, inplace = True)
    datosmonth = datos.groupby(pd.Grouper(freq = 'M'))['High'].max()

    glDate = 0
    lastGLV = 0
    currentDate = ''
    curentGLV = 0
    for index, value in datosmonth.items():
        if value > curentGLV:
            curentGLV = value
            currentDate = index
            counter = 0
        if value < curentGLV:
            counter = counter + 1

        if counter == 3:
            if curentGLV != lastGLV:
                print(curentGLV)
            glDate = currentDate
            lastGLV = curentGLV
            counter = 0

    inimonth = glDate - dt.timedelta(days = 30)
    datosdays = datos[(datos.index > inimonth) & (datos.index <= glDate)].groupby(pd.Grouper(freq='d'))['High'].max()
    
    for index, value in datosdays.items():
        if value == lastGLV:
            glDate = index
            lastGLV = value

    if lastGLV == 0:
        message = stock + ' has not formed a green line yet'
    else:
        message = ('Last Green Line: ' + str(lastGLV) + ' on ' + str(glDate))

    print(message)

    fig = plt.figure(figsize = (12,6))
    plt.subplot(1, 1, 1)
    plt.plot(datos.Close)
    plt.hlines(lastGLV, glDate, now, colors = 'g')
    plt.show()
    
    stock = input('Enter the stock symbol : ')