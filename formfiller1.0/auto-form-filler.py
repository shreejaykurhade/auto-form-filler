from selenium import webdriver
import time

#Setting up your web browser
web=webdriver.Chrome()

#Setting up your google form which you will be using 
web.get(' YOUR GOOGLE FORM LINK ')
time.sleep(3)

#Submitting your name in text 
sname='jay'
name=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(sname)
time.sleep(1)

#Submitting your email in text
smail='jay@gmail.com'
mail=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
mail.send_keys(smail)
time.sleep(0.5)

#submitting your organization in text
sorganization='TVM High School'
organization=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
organization.send_keys(sorganization)
time.sleep(1)

#Clicking on checkbox
sday1=web.find_element('xpath','//*[@id="i18"]/div[2]')
sday1.click()
time.sleep(0.5)

#Clicking on radio button
sdiet=web.find_element('xpath','//*[@id="i31"]/div[3]/div')
sdiet.click()
time.sleep(0.5)

#Clicking on checkbox
spay=web.find_element('xpath','//*[@id="i54"]/div[2]')
spay.click()
time.sleep(0.5)

#Clicking on Submit button
submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()





