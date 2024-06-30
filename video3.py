from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import choice

url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0"


driver = webdriver.Firefox() # открытие браузера
driver.get(url) # открытие сайта

# paragraphs = driver.find_elements(By.TAG_NAME, "p")
# for p in paragraphs:
#     print(p.text)
#     input("Press Enter to continue...")

hatnotes = []
for element in driver.find_elements(By.TAG_NAME, "div"):
    cls = element.get_attribute("class") # получение атрибута "class" элемента с помощью метода get_attribute
    if cls == "hatnote navigation-not-searchable":
        hatnotes.append(element)
print(hatnotes)
hatnote = choice(hatnotes) # выбор случайного элемента из списка
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href") # получение атрибута "href" элемента с помощью метода get_attribute
driver.get(link) # переход по ссылке при помощи метода get
sleep(3)

driver.save_screenshot("test.png") # сохранение скриншота
sleep(3)
driver.quit() # закрытие браузера