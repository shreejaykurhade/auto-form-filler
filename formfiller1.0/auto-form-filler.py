from selenium import webdriver
import time

web=webdriver.Chrome()
web.get('https://forms.gle/y8anLHC3jGFcPPtU8')
time.sleep(3)

sname='jay'
name=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(sname)
time.sleep(1)

smail='kshreejay@gmail.com'
mail=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
mail.send_keys(smail)
time.sleep(0.5)

sorganization='Ryan international school'
organization=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
organization.send_keys(sorganization)
time.sleep(1)

sday1=web.find_element('xpath','//*[@id="i18"]/div[2]')
sday1.click()
time.sleep(0.5)

sdiet=web.find_element('xpath','//*[@id="i31"]/div[3]/div')
sdiet.click()
time.sleep(0.5)

spay=web.find_element('xpath','//*[@id="i54"]/div[2]')
spay.click()
time.sleep(0.5)

submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()





