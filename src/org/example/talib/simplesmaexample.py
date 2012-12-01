'''
Created on Nov 25, 2012

@author: Shakti
'''
import pandas.io.data as web  
import talib as ta
import pandas as pd
import pylab

SMA_PERIOD = 10
FMA_PERIOD = 25

# Download SP500 data with pandas
spy = web.get_data_yahoo('SPY', '2011-01-01', '2012-06-30')
analysis = pd.DataFrame(index = spy.index)
analysis['SMA'] = ta.SMA(spy.Close,SMA_PERIOD)
analysis['FMA'] = ta.SMA(spy.Close,FMA_PERIOD)
pylab.plot(spy.index, analysis.SMA, 'r-', label="SMA 10")
pylab.plot(spy.index, analysis.FMA, 'g-', label="FMA 25")
pylab.plot(spy.index, spy.Close, 'b-', label="Current")

pylab.legend()
pylab.show()