'''
Created on Dec 2, 2012

@author: Shakti
'''
import urllib
import json
import numpy as np
import pandas as pd

SYMBOL = 'AAPL'

def __request(symbol):
    url = 'http://quotes.esignal.com/esignalprod/esigchartspon?cont=%s&period=V&varminutes=1&size=745x550&bartype=AREA&bardensity=MEDIUM&chartdata=wstudies&callback=ohlcModule.chartCallback' % (symbol)
    return urllib.urlopen(url).read()

def get_json_quotes(symbol):
    filter_data = __request(symbol)[25:][:-2].replace("'Close',],'colors'", "'Close'],'colors'").replace("'rgb(0,0,128)',]}],'chartDataValues'","'rgb(0,0,128)']}],'chartDataValues'").replace("'", "\"")
    json_data = json.loads(filter_data)
    return json_data

json_quotes = get_json_quotes(SYMBOL)
start = json_quotes["chartDataProps"][0]["xy"]["xstart"]
end = json_quotes["chartDataProps"][0]["xy"]["xend"]
print 'start, end' ,start,end

dates = json.dumps(json_quotes["chartDataValues"]["Date"])
time = json.dumps(json_quotes["chartDataValues"]["Time"])
openq = json.dumps(json_quotes["chartDataValues"]["Open"])
high = json.dumps(json_quotes["chartDataValues"]["High"])
low = json.dumps(json_quotes["chartDataValues"]["Low"])
print json_quotes["chartDataValues"]["Close"]
close = np.array(filter((json_quotes["chartDataValues"]["Close"]),''))
print close

