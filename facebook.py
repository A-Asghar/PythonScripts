from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random


# fb_post = 'https://fb.watch/eA-v40zaik/'
fb_post = str(input('Facebook post link: '))
# email = ''
email = str(input('Email: '))
# motDePass = ''
motDePass = str(input('Password: '))
groups_file = 'file.txt'


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})
driver=webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities = chrome_options.to_capabilities())
driver.get('https://www.facebook.com/login/')

def sleepForRandomTime():
     time.sleep(random.randint(15,30))
     



try:
    user_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
except:
    print("Error")

user_name.send_keys(email)
password=driver.find_element_by_name("pass")
password.send_keys(motDePass)
password.submit()
time.sleep(90)

driver.get(fb_post)



#share using Page account
with open(groups_file, 'r', encoding='utf-8') as file:
    for group in file:
        try:
            share = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[normalize-space()="Share"]/div'))
            )
            share.click()
            sleepForRandomTime()
        except:
            print('- - - - -Share failed- - - - -')
            driver.get(fb_post)
            time.sleep(10)
            continue



        try:
            shareToGroup = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[normalize-space()="More Options"]/div'))
            )
            # time.sleep(5)
            shareToGroup.click()
            sleepForRandomTime()
        except:
            print('- - - - -More Options failed- - - - -')
            driver.get(fb_post)
            time.sleep(10)
            continue


        try:
            shareToGroup = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[normalize-space()="Share to a group"]/div'))
            )
            # time.sleep(5)
            shareToGroup.click()
            sleepForRandomTime()
        except:
            print('- - - - -Share to a group failed- - - - -')
            driver.get(fb_post)
            time.sleep(10)
            continue

        try:
            shareAs = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//label[@aria-label='Share as']"))
            )
            # time.sleep(5)
            shareAs.click()
            sleepForRandomTime()
        except:
            print('- - - - -Share As failed- - - - -')
            driver.get(fb_post)
            time.sleep(10)
            continue


        try:
            shareAs = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[normalize-space()="Apnastock.PK"]/div'))
            )
            # time.sleep(5)
            shareAs.click()
            sleepForRandomTime()
        except:
            print('- - - - -Click on account failed- - - - -')
            driver.get(fb_post)
            time.sleep(10)
            continue


        try:
            group_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH , "//input[@role='textbox']"))
            )
            group_name.send_keys(group)
            # time.sleep(5)
            sleepForRandomTime()
        except:
            print(group , 'Typing Failed')
            driver.get(fb_post)
            time.sleep(10)
            continue
        

        try:
            click_group = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , "//div[@class='b20td4e0 muag1w35']//div[@role='button']"))
            )
            click_group.click()
            sleepForRandomTime()
        except:
            print(group)
            driver.get(fb_post)
            time.sleep(10)
            continue

        try:
            publish = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , "//div[normalize-space()='Post']//div[@role='button']"))
            )
            # time.sleep(3)
            publish.click()
            sleepForRandomTime()
        except:
            print(group)
            driver.get(fb_post)
            time.sleep(10)
            continue

        print('Shared to > ' , group)

        time.sleep(random.randint(60,300))

print('Done Sharing')
driver.quit()