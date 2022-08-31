from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


#opening webbrowsers
def tutorialPart1(url):
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get(url)
    driver.close() # .quit()

#tutorialPart1('https://www.skysports.com/football/derby-county-vs-grimsby-town/471655')


def tutorialPart2(url):
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get(url)

    accept_terms = driver.find_element(By.ID,"L2AGLb")
    accept_terms.click()

    search = driver.find_element(By.NAME,"q")
    search.send_keys("sky sports")
    search.send_keys(Keys.RETURN)

    time.sleep(5)


    driver.close() # .quit()

tutorialPart2('https://www.google.com/')