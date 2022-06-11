from bs4 import BeautifulSoup
import requests
import selenium 
from selenium import webdriver
import sys
from kora.selenium import wd
import pandas as pd
from openpyxl import load_workbook

def parse_content(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    print (soup.title.text)
    return soup


#brandname = input('Enter brand name: ')
brandname = 'cafe 1700'
url = 'https://www.ankorstore.com/search?q='+brandname
#driver = webdriver.Chrome()
#driver.get(url)
wd.get(url)
html_doc = wd.page_source
#html_doc = driver.page_source
#driver.close()
content = parse_content(html_doc)
a = content.find('a', class_='linkToBrand', href = True)
print(a['href'])
url = 'https://www.ankorstore.com'+a['href']
#driver.get(url)
wd.get(url)
#html_doc = driver.page_source 
#driver.close()
html_doc = wd.page_source 
html_doc = html_doc.replace("<br>"," ")

'''
print(html_doc)
with open('filename2.txt', "w", encoding="utf-8") as f:
    f.write(html_doc)
'''

content = parse_content(html_doc)



ul = content.find('ul', class_='brand-important-point' )
li = ul.find_all('li')
print(li)


for spantag in li:
	desc = spantag.find_all('span')
	#print(desc[1])
	Location = desc[1]
	break

print('\n' +'-----Location-----')	
print(Location)

print('\n' +'-----Description-----')
Description = content.find("meta", attrs={'name': 'description'})
print(Description)

print('\n' +'-----Brand-----')
Brand = content.find('div', class_='brand-title ds-flex ds-flex-wrap').find('h1').text
print(Brand)

print('\n' + '-----Done-----')


mydict= {'Brand': Brand,
                   'Location': Location,
                    'Description': Description}
df = pd.DataFrame([mydict])
writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl')
# try to open an existing workbook
writer.book = load_workbook('demo.xlsx')    
# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
reader = pd.read_excel(r'demo.xlsx')
# write out the new sheet
df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

writer.close()