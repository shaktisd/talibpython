# Some sample code to test getting intrady prices from www.netfonds.no
# 
# Prices are available for appriximately the last 15 days (to be confirmed)
#
# Note that AAPL.O denotes NASDAQ where
#    NASDAQ: O
#    NYSE: N
#    AMEX: A
#

import pylab
import pandas
import urllib
import talib
import matplotlib.pyplot as plt

url='http://hopey.netfonds.no/posdump.php?date=20121130&paper=%s.O&csv_format=csv'

urllib.urlretrieve(url % 'AAPL', 'AAPL.csv')
urllib.urlretrieve(url % 'GOOG', 'GOOG.csv')

AAPL = pandas.read_csv('AAPL.csv')
GOOG = pandas.read_csv('GOOG.csv')

AAPL = AAPL.drop_duplicates(cols='time')
GOOG = GOOG.drop_duplicates(cols='time')

for i in AAPL.index:
    AAPL['time'][i]= pandas.datetime.strptime(AAPL['time'][i],'%Y%m%dT%H%M%S')
AAPL.index=AAPL['time']; del AAPL['time']

for i in GOOG.index:
    GOOG['time'][i]= pandas.datetime.strptime(GOOG['time'][i],'%Y%m%dT%H%M%S')
GOOG.index=GOOG['time']; del GOOG['time']
 
DATA = pandas.DataFrame({'AAPL':AAPL['bid'],'GOOG':GOOG['bid']}) 

DATA = DATA[DATA.index > pandas.datetime(2012, 11, 30, 9, 59, 0)]

#DATA['AAPL'] = (DATA['AAPL'].fillna(method='ffill')).fillna(method='backfill')
#DATA['GOOG'] = (DATA['GOOG'].fillna(method='ffill')).fillna(method='backfill')

#DATA['GOOG_SMA'] = talib.SMA(DATA['GOOG'],500)
#DATA['GOOG_FMA'] = talib.SMA(DATA['GOOG'],200)
 
#print DATA.ix[:20].to_string()
#DATA.plot(subplots=True)


DATA = pandas.DataFrame({'AAPL':AAPL['bid'], 'GOOG':GOOG['bid']})

# Compute OHLC data with pandas from raw tick data
DATA_15MIN = pandas.Panel({'AAPL':DATA.AAPL.resample('15min', how='ohlc', fill_method='backfill'),
                       'GOOG':DATA.GOOG.resample('15min', how='ohlc', fill_method='backfill')})
# Technical Analysis
for n in DATA_15MIN:
    DATA_15MIN[n]['SMA'] = talib.MA(DATA_15MIN[n].close, 50)
    DATA_15MIN[n]['FMA'] = talib.MA(DATA_15MIN[n].close, 20)

# Plot
fig, (ax1, ax2) = plt.subplots(2, 1, sharex = True)
ax1.set_ylabel('AAPL', size=20)
ax2.set_ylabel('GOOG', size=20)

DATA_15MIN.AAPL.close.plot(ax=ax1, lw=2)
DATA_15MIN.AAPL.SMA.plot(ax=ax1, c = 'g')
DATA_15MIN.AAPL.FMA.plot(ax=ax1, c = 'r')

DATA_15MIN.GOOG.close.plot(ax=ax2, lw=2)
DATA_15MIN.GOOG.SMA.plot(ax=ax2, c = 'g')
DATA_15MIN.GOOG.FMA.plot(ax=ax2, c = 'r')
plt.plot()
