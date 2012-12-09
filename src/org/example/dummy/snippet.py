'''
Created on Dec 8, 2012

@author: Shakti
Dummy changes  in tag
'''
import urllib2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick
import talib as ta

# 1 min quote of nse live data
URL = "http://www.nseindia.com/ChartApp/install/charts/data/GetHistoricalNew.jsp?Instrument=FUTSTK&CDSymbol=S%26P%20CNX%20NIFTY&Segment=OI&Series=EQ&CDExpiryMonth=1&FOExpiryMonth=1&IRFExpiryMonth=27-03-2013&CDIntraExpiryMonth=27-12-2012&FOIntraExpiryMonth=27-12-2012&IRFIntraExpiryMonth=&CDDate1=01-12-2011&CDDate2=08-12-2012&PeriodType=2&Periodicity=1&ct0=g1|1|1&ct1=g2|2|1&ctcount=2&time=1354976463676"
SMA_FAST = 5
SMA_SLOW = 20
quotes = {}

def _request():
    req = urllib2.Request(URL)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    return urllib2.urlopen(req).read()
    
#data format date|g1_o|g1_h|g1_l|g1_c|g2|g2_CUMVOL~
#line delimiter ~
def _parse_delimited_data(data):
    rows = data.split ('~')
    d = {}
    keys = rows [0].split ('|')
    for key in keys: d [key] = []
    for row in rows [1:]:
        for idx, value in enumerate (row.split ('|') ):
            d [keys [idx] ].append (value)
    return d

# Data for matplotlib finance plot
quotes = _parse_delimited_data(_request())
ochl = np.array(pd.DataFrame({'0':range(1,np.array(quotes['g1_o']).size + 1),
                                  '1':np.array(quotes['g1_o']).astype(np.float),
                                  '2':np.array(quotes['g1_c']).astype(np.float),
                                  '3':np.array(quotes['g1_h']).astype(np.float),
                                  '4':np.array(quotes['g1_l']).astype(np.float)}))

quotes['g1_c'] = np.array(quotes['g1_c']).astype(np.float)
analysis = pd.DataFrame(index = quotes['date'])
analysis['sma_f'] = ta.SMA(quotes['g1_c'], SMA_FAST)
print analysis['sma_f']
analysis['sma_s'] = ta.SMA(quotes['g1_c'], SMA_SLOW)
print analysis['sma_s']
# Prepare plot
fig, ax = plt.subplots(1, 1, sharex=True)
ax.set_ylabel('SP500', size=20)

# Plot candles
candlestick(ax, ochl, width=0.5, colorup='g', colordown='r', alpha=1)

# Draw Moving Averages
analysis.sma_f.plot(c='g')
analysis.sma_s.plot(c='b')

# Show the picture!
plt.show()

            