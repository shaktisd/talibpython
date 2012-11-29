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

# Technical Analysis
SMA_FAST = 34
SMA_SLOW = 144
RSI_PERIOD = 14
analysis = pd.DataFrame(index = spy.index)
analysis['sma_f'] = pd.rolling_mean(spy.Close, SMA_FAST)
analysis['sma_s'] = pd.rolling_mean(spy.Close, SMA_SLOW)
analysis['rsi'] = ta.RSI(spy.Close, RSI_PERIOD)

# Record signals (open position after crossover)
analysis['signal_bull'] = np.where((analysis.sma_f > analysis.sma_s) &
                                   (analysis.sma_f.shift(1) < analysis.sma_s.shift(1)) &
                                   (analysis.rsi > 50), 1, 0)

analysis['signal_bear'] = np.where((analysis.sma_f < analysis.sma_s) &
                                   (analysis.sma_f.shift(1) > analysis.sma_s.shift(1)) &
                                   (analysis.rsi < 50), 1, 0)

# Report
print 'Strategy: Moving Average Crossover filtered with RSI'
for i in analysis.index:
    if analysis.signal_bear[i]: print i.date(), 'sell @', spy.Open[i]
    if analysis.signal_bull[i]: print i.date(), 'buy  @', spy.Open[i]

# Prepare plot
fig, ax = plt.subplots(1, 1, sharex=True)
ax.set_ylabel('SP500', size=20)

# Plot candles
candlestick(ax, spy_ochl, width=0.5, colorup='g', colordown='r', alpha=1)

# Draw Moving Averages
analysis.sma_f.plot(c='r')
analysis.sma_s.plot(c='g')

# Plot entry arrows
for i in analysis.index: 
    if analysis.signal_bull[i]:
        plt.arrow(date2num(i), spy.High[i], 0, 2,
                  fc="b", ec="g", head_width=5, head_length=2)

    if analysis.signal_bear[i]:
        plt.arrow(date2num(i), spy.Low[i], 0, -2,
                  fc="r", ec="r", head_width=5, head_length=2)

# Show the picture!
plt.show()