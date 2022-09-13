import os
from logging import exception
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def GettingServer(server):
    gettingServer = driver.find_element(by=By.CSS_SELECTOR, value=f'div[data-dnd-name="{server}"]')
    gettingServer.click()
    driver.implicitly_wait(10)


os.environ['PATH'] += r'.\ chromedriver.chromedriver.exe'
URL = 'https://discord.com/login'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

print("\n\n Driver waiting for user to login...\nLogin using QR code or Login using email and password\n")
driver.implicitly_wait(15)
time.sleep(15)

#server name 
GetServer = "Testing2"
GetServer2 = "Testing2"
AuditServer = "Testing3"

GettingServer(GetServer)

findChannels = driver.find_element(by=By.ID, value='channels')
gettingChannel = findChannels.find_element(by=By.CSS_SELECTOR, value='li[data-dnd-name="general"]')
gettingChannel.click()


listA = []   # for webelement
listB = []   # for actual text
listA = driver.find_elements(by=By.CLASS_NAME, value='markup-eYLPri')

# Getting the text from the WebElement
for i in listA:
    listB.append(i.text)

# sending it to Auditing server

GettingServer(AuditServer)
chatBox = driver.find_element(by=By.CSS_SELECTOR , value='div[role="textbox"]')
chatBox.click()

for i in listB:
    chatBox.send_keys(i, Keys.ENTER)
    time.sleep(1.5)
