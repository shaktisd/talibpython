import pandas.io.data as web    
import pandas as pd
import talib as ta
import matplotlib.pyplot as plt

# Download SP500 data with pandas
spy = web.get_data_yahoo('SPY', '2012-01-01')

# Compute some technical analysis on data with Ta-lib and store it in a pandas dataframe
analysis = pd.DataFrame(index = spy.index)
analysis['rsi'] = ta.RSI(spy.Close)
analysis['macd1'], analysis['macd2'], analysis['macd3'] = ta.MACD(spy.Close, 26, 12, 9)

# Prepare for drawing
desde, hasta = '2012-03-01', '2012-10-30'
fig, axes = plt.subplots(3, 1, sharex=True)
ax1, ax2, ax3 = axes[0], axes[1], axes[2]

# Draw close price line
spy['Close'].plot(ax = ax2)

# Draw some moving averages with pandas functions only
for n in [(34,'yellow'), (55,'green'), (89,'red')]:
    pd.rolling_mean(spy.Close, n[0]).plot(ax=ax2, color=n[1])

# Draw RSI computed with Talib
analysis.rsi.plot(ax=ax1)
for n in [30, 50, 70]:
    ax1.axhline(n, lw=2, color='0')

# Draw MACD computed with Talib
analysis.macd1.plot(ax=ax3, color='b') # MACD Line
analysis.macd2.plot(ax=ax3, color='g') # Signal Line
analysis.macd3.plot(ax=ax3, color='r') # Histogram Line
ax3.axhline(0, lw=2, color='0')

ax1.set_yticks([30,50,70])   
ax2.set_xlim([desde, hasta])
ax2.set_ylim([spy.Close[desde:hasta].min(),spy.Close[desde:hasta].max()])

plt.subplots_adjust(wspace=0, hspace=0)
plt.savefig('spy.png', dpi=400, bbox_inches='tight')