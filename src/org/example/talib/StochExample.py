'''
Created on Nov 30, 2012

@author: Shakti
'''
import pandas.io.data as web  
import talib as ta
import pandas as pd
import pylab

# Download SP500 data with pandas
spy = web.get_data_yahoo('^NSEI', '2011-01-01', '2012-06-30')
analysis = pd.DataFrame(index = spy.index)
analysis['STOCH_K'], analysis['STOCH_D'] = ta.STOCH(spy.High, spy.Low, spy.Close,slowk_period=14,slowd_period=3)

pylab.figure(1)
pylab.subplot(211)
pylab.plot(spy.index, analysis.STOCH_K, 'r-', label="STOCH_K")
pylab.plot(spy.index, analysis.STOCH_D, 'g-', label="STOCK_D")
pylab.legend()

pylab.subplot(212)
pylab.plot(spy.index, spy.Close, 'b-', label="Current")

pylab.legend()
pylab.show()
