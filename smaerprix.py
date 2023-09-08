from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import html
s=Service("C:/Users/dell/Desktop/chromedriver-win64/chromedriver.exe")  #idi chrome browser ni open chestadi.
options=webdriver.ChromeOptions()#chrome browser automatic ga close avvanivvadu
options.add_experimental_option("detach",True) #automatic ga close avvanivvadu
driver=webdriver.Chrome(options=options)
driver.get("https://www.smartprix.com/mobiles")#smartprix lo mobile site open aitadi
time.sleep(1)#site open ainaka one second aagadaniki
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
#paina line 'exclude out of stock' ni select chestundi
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
#paina line 'exclude upcoming' ni select chestundi
old_height=driver.execute_script('return document.body.scrollHeight')
while True:
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    #paina code 'Load more' button ni click chestundi
    time.sleep(1)
    new_height=driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height=new_height
html = driver.page_source
with open('smaerprix.html', 'w',encoding='utf-8') as f:
    f.write(html)

