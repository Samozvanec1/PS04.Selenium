from selenium import webdriver
from time import *

driver = webdriver.Firefox()
driver.get("https://ru.wikipedia.org/wiki/Document_Object_Model")
driver.save_screenshot("dom.png")

sleep(5)
driver.get("https://ru.wikipedia.org/wiki/Selenium")
sleep(3)
driver.save_screenshot("selenium.png")
sleep(3)
driver.refresh()
sleep(5)
driver.quit()