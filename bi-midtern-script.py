from bs4 import BeautifulSoup
import requests
import selenium 
from selenium import webdriver
import sys
from time import sleep, time
#from kora.selenium import wd
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import strptime

def parse_content(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    print (soup.title.text)
    return soup

driver = webdriver.Chrome()

def month_to_number(month_name):
	return strptime(month_name, '%b').tm_mon

url = 'https://lms.iba.edu.pk/portal/site/b94b5e3e-b73c-43fd-bf91-5afd5cc1fb85/tool/e0646eab-2aa2-49f3-88cb-d06ac01ae085'

driver.get(url)
sleep(1)
element = driver.find_element_by_name("eid")
element.send_keys("18593")
print('found eid')
element = driver.find_element_by_name("pw")
element.send_keys("karachi@@123")
print('foudn pw')
element.send_keys(Keys.RETURN)
print('pressed enter')



opendate = []
duedate = []
opendatemonths = []
opendatedays = []
opendateyear = []

openDates = driver.find_elements(By.XPATH, ("//*[@headers='openDate']"))

#print(elements.get_attribute('innerHTML'))
for e in openDates:
	#print(e.get_attribute('innerHTML'))
	opendate.append(e.get_attribute('innerHTML'))

dueDates = driver.find_elements(By.XPATH, ("//*[@headers='dueDate']//span[@class='highlight']"))
for e in dueDates:
	#print(e.get_attribute('innerHTML'))
	duedate.append(e.get_attribute('innerHTML'))
	



for i in opendate:
	print(i)

for i in duedate:
	print(i)

for i in opendate:
	opendatemonths.append(i.split(' ')[0])		
	opendatedays.append(i.split(' ')[1])
	opendateyear.append(i.split(' ')[2])

opendatemonths2 = []
print('----- OPEN DATE MONTHS --------')
for i in opendatemonths:
	i = ''.join(i.split())
	i = month_to_number(i)
	opendatemonths2.append(i)
	print(i)
print('----- OPEN DATE MONTHS --------')

opendatedays = [s.strip(',') for s in opendatedays]
openDates2 = []
for i in range(0,len(opendatemonths)):
	string = opendatedays[i] + '/' + str(opendatemonths2[i]) + '/' + opendateyear[i]
	openDates2.append(string)

print('----- OPEN DATE 2 --------')
for i in openDates2:
	print(i)
print('----- OPEN DATE 2 --------')




duedatemonths = []
duedatedays=[]
duedateyear = []

for i in duedate:
	duedatemonths.append(i.split(' ')[0])		
	duedatedays.append(i.split(' ')[1])
	duedateyear.append(i.split(' ')[2])
duedatemonths2 = []

print('----- DUE DATE MONTHS --------')
for i in duedatemonths:
	i = ''.join(i.split())
	i = month_to_number(i)
	duedatemonths2.append(i)
	print(i)
print('----- DUE DATE MONTHS --------')



duedatedays = [s.strip(',') for s in duedatedays]
dueDates2 = []
for i in range(0,len(duedatemonths)):
	string = duedatedays[i] + '/' + str(duedatemonths2[i]) + '/' + duedateyear[i]
	dueDates2.append(string)

print('----- DUE DATE 2 --------')
for i in dueDates2:
	print(i)
print('----- DUE DATE 2 --------')


sleep(2)
driver.close()