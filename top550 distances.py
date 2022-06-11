import requests
import pandas as pd
import json

#url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Gent, Belgie&destinations=Brugge, Belgie&units=imperial&key=AIzaSyAYWnjCkONBfLMp1i5QAO8P_PPROs_s-iY"

df = pd.read_excel("Distances 2021-10-29.xlsx")

for row in range(1,3):
	src = df.loc[row,'City1']
	dest = df.loc[row,'City2']
	url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + src + "&destinations=" +dest +"&units=imperial&key=AIzaSyAYWnjCkONBfLMp1i5QAO8P_PPROs_s-iY"
	response = requests.request("GET", url).json()
	print(response , "\n")

	'''
	for obj in response['rows']:
		for obj2 in obj['elements']:
			print(data['distance']['text'])
			print(data['duration']['text'])
	'''

	print(src , ' -> ' ,  dest , '\n')








