from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://ru.wikipedia.org/wiki/Заглавная_страница"


driver = webdriver.Firefox() # открытие браузера
driver.get(url) # открытие сайта

assert "Википедия" in driver.title # проверка наличия "Википедия" в заголовке страницы
sleep(3) # пауза 3 секунды
searchbox = driver.find_element(By.ID, "searchInput") # поиск по ID поисковой строки
searchbox.send_keys("Солнечная система") # ввод в поисковую строку "Солнечная система"
searchbox.send_keys(Keys.RETURN) # нажатие клавиши Enter на клавиатуре
sleep(3) # пауза 3 секунды
driver.save_screenshot("test.png") # сохранение скриншота
sleep(3)
a = driver.find_element(By.LINK_TEXT, "Солнечная система") # поиск по тексту ссылки
a.click() # нажатие на ссылку
sleep(3)
driver.save_screenshot("test2.png") # сохранение скриншота
sleep(3)
driver.quit() # закрытие браузера