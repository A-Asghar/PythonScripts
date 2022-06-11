#https://www.analyticsvidhya.com/blog/2021/06/download-financial-dataset-using-yahoo-finance-in-python-a-complete-guide/

import yfinance as yf
from yahoofinancials import YahooFinancials
import pandas as pd
import datetime 
import yfinance.shared as shared
import itertools

df = pd.read_csv("C:\\Users\\Ali Asghar\\Downloads\\companies.csv" , header = None)

dict1 = {}
done = False

for i in range(len(df.index)):
	temp = df.values[[i],0]

	data = yf.download(temp[0], 
                      start='2012-01-01', 
                      end='2013-01-9', 
                      progress=False,)
	#print(data)
	#print(df.index)
	
	data = data.Close.round(decimals = 3 )
	'''
	if not done:
		dict1["Dates"] = data.Date
	'''
	li = data.values.tolist()
	dict1[temp[0]] = li
	

	'''
	dict1[temp[0]] = li
	if not dict1[temp[0]]:
		dict1[temp[0]] = ["Not Available"] * len(dict1[next(iter(dict1))])
	'''

nest = dict1.values()	
out = pd.DataFrame((_ for _ in itertools.zip_longest(*nest)), columns=dict1.keys())
for k in dict1:
	print(len(dict1[k]))
out.to_csv('output.csv', index=False)

