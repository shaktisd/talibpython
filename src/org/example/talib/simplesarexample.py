'''
Created on Nov 30, 2012
Implemented http://www.earnforex.com/forex-strategy/parabolic-sar-strategy
Entry Conditions
Enter Long position when the current price touches the indicator from below and it changes its direction.
Enter Short position when the current price touches the indicator from above and it changes its direction.

@author: Shakti
'''
import pandas.io.data as web  
import talib as ta
import pandas as pd
import pylab


# Download SP500 data with pandas
spy = web.get_data_yahoo('SPY', '2011-01-01', '2012-06-30')
analysis = pd.DataFrame(index = spy.index)
analysis['SAR'] = ta.SAR(spy.High,spy.Low)
print spy.index
pylab.plot(spy.index, analysis.SAR, 'r-', label="SAR")
pylab.plot(spy.index, spy.Close, 'b-', label="Current")

pylab.legend()
pylab.show()