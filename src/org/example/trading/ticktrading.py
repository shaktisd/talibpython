'''
Created on Dec 2, 2012

@author: Shakti
Can't use esignal for quotes as there are duplicates quotes , not a very reliable source.

@deprecated: 
'''
import urllib
import json
import numpy as np
import pandas as pd
import matplotlib.finance as fin
import matplotlib.pyplot as plt

SYMBOL = '$NIFTY-NSE'

def __request(symbol):
    #url = 'http://quotes.esignal.com/esignalprod/esigchartspon?cont=%s&period=V&varminutes=1&size=745x550&bartype=AREA&bardensity=MEDIUM&chartdata=wstudies&callback=ohlcModule.chartCallback' % (symbol)
    url = 'http://quotes.esignal.com/esignalprod//esigchartspon?cont=%s&period=V&varminutes=5&size=745x550&bartype=CANDLE&bardensity=MEDIUM&showextendednames=true&chartdata=wstudies&callback=ohlcModule.chartCallback'  % (symbol)
    return urllib.urlopen(url).read()

def get_json_quotes(symbol):
    filter_data = __request(symbol)[25:][:-2].replace("'Close',],'colors'", "'Close'],'colors'").replace("'rgb(0,0,128)',]}],'chartDataValues'","'rgb(0,0,128)']}],'chartDataValues'").replace("'", "\"")
    json_data = json.loads(filter_data)
    return json_data

def get_quote_block(quotes,block_type):
    return np.array(filter(None,quotes["chartDataValues"][block_type]),dtype='|S10').astype(np.longdouble)

json_quotes = get_json_quotes(SYMBOL)
start = json_quotes["chartDataProps"][0]["xy"]["xstart"]
end = json_quotes["chartDataProps"][0]["xy"]["xend"]
print 'start, end' ,start,end

#dates = np.array(json_quotes["chartDataValues"]["Date"])
#time = np.array(json_quotes["chartDataValues"]["Time"])
openl = get_quote_block(json_quotes,"Open")
close = get_quote_block(json_quotes,"Close")
high = get_quote_block(json_quotes,"High")
low = get_quote_block(json_quotes,"Low")


print openl.size , high.size, low.size, close.size
print openl , high, low, close

# Data for matplotlib finance plot
spy_ochl = np.array(pd.DataFrame({'0':range(1,openl.size+1),'1':openl,'2':close,'3':high,'4':low}))
print spy_ochl
fig = plt.figure()
fig.subplots_adjust(bottom=0.2)
ax = fig.add_subplot(111)
ax.set_ylabel(SYMBOL, size=20)
fin.candlestick(ax, spy_ochl, width=0.5, colorup='g', colordown='r', alpha=1)

# Show the picture!
plt.show()