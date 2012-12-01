'''
Created on Nov 30, 2012
Implemented http://www.earnforex.com/forex-strategy/parabolic-sar-strategy
Entry Conditions
Enter Long position when the current price touches the indicator from below and it changes its direction.
Enter Short position when the current price touches the indicator from above and it changes its direction.

@author: Shakti
'''
import pandas.io.data as web
import pandas as pd
import numpy as np
import talib as ta
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from matplotlib.finance import candlestick

# Download sample data
spy = web.get_data_yahoo('SPY', '2010-01-01')

# Data for matplotlib finance plot
spy_ochl = np.array(pd.DataFrame({'0':date2num(spy.index),
                                  '1':spy.Open,
                                  '2':spy.Close,
                                  '3':spy.High,
                                  '4':spy.Low}))

analysis = pd.DataFrame(index = spy.index)
analysis['SAR'] = ta.SAR(spy.High,spy.Low, acceleration=0.05, maximum=0.2)
# Prepare plot
fig, ax = plt.subplots(1, 1, sharex=True)
ax.set_ylabel('SP500', size=20)

# Plot candles
candlestick(ax, spy_ochl, width=0.5, colorup='g', colordown='r', alpha=1)

# Draw Moving Averages
analysis.SAR.plot(c='r')

# Show the picture!
plt.show()