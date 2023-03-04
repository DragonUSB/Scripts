import pandas as pd
import quandl as qdl
import matplotlib.pyplot as plt
from scipy.stats import linregress

# get AAPL 10 years data

data = qdl.get("WIKI/AAPL", start_date="2007-01-01", end_date="2017-05-01")

data0 = data.copy()
data0['date_id'] = ((data0.index.date - data0.index.date.min())).astype('timedelta64[D]')
data0['date_id'] = data0['date_id'].dt.days + 1

# high trend line

data1 = data0.copy()

while len(data1)>3:

    reg = linregress(
                    x=data1['date_id'],
                    y=data1['Adj. High'],
                    )
    data1 = data1.loc[data1['Adj. High'] > reg[0] * data1['date_id'] + reg[1]]

reg = linregress(
                    x=data1['date_id'],
                    y=data1['Adj. High'],
                    )

data0['high_trend'] = reg[0] * data0['date_id'] + reg[1]

# low trend line

data1 = data0.copy()

while len(data1)>3:

    reg = linregress(
                    x=data1['date_id'],
                    y=data1['Adj. Low'],
                    )
    data1 = data1.loc[data1['Adj. Low'] < reg[0] * data1['date_id'] + reg[1]]

reg = linregress(
                    x=data1['date_id'],
                    y=data1['Adj. Low'],
                    )

data0['low_trend'] = reg[0] * data0['date_id'] + reg[1]

# plot

data0['Adj. Close'].plot()
data0['high_trend'].plot()
data0['low_trend'].plot()
plt.show()