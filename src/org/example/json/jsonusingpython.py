'''
Created on Dec 1, 2012

@author: Shakti
'''
import json

data = "{'chartDataProps':[{'xy':{'xstart':0,'xend':692,'ystart':15,'yend':534},'names':['Date','Time','Open','High','Low','Close',],'colors':['rgb(0,0,128)','rgb(0,0,128)','rgb(0,0,128)','rgb(0,0,128)','rgb(0,0,128)','rgb(0,0,128)',]}],'chartDataValues':{'Date':['11/30/2012'],'Time':['09:44:00'],'Open':['5848.40'],'High':['5848.40'],'Low':['5847.45'],'Close':['5848.40']}}";
#data =  [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
#with open('data.json') as data_file:    
#    data = json.load(data_file)
data_string = json.dumps(data)
loads = json.loads(data_string)
print loads["chartDataProps"]
