from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
otkr = input("Что для Вас найти в Викепедии?")


driver = webdriver.Firefox() # открытие браузера
driver.get(url) # открытие сайта

userinput = driver.find_element(By.ID, "searchInput") # поиск по ID поисковой строки
userinput.send_keys(otkr) # ввод в поисковую строку
userinput.send_keys(Keys.ENTER) # нажатие клавиши Enter на клавиатуре
sleep(4)

# vb1 = driver.find_element(By.LINK_TEXT, otkr).get_attribute("href") # получение атрибута "href" элемента с помощью метода get_attribute
# driver.get(vb1)
# sleep(3)



def invar1():
    li_list = []
    placelist = 1
    useraccept = "y"
    for element in driver.find_elements(By.TAG_NAME, "li"):
        cls = element.get_attribute("class") # получение атрибута "class" элемента с помощью метода get_attribute
        if cls == "toclevel-1 tocsection-"+str(placelist) or cls == "toclevel-1-1 tocsection-"+str(placelist):
            li_list.append(element)
        placelist = placelist + 1
    placelist = 0
    while useraccept == "y":
        print(li_list)
        if placelist == len(li_list):
            driver.get(url)
            menu()
        useraccept = input("Хотите перейти к следующему элементу? (y/n)")
        hatnote = li_list[placelist] # выбор случайного элемента из списка
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href") # получение атрибута "href" элемента с помощью метода get_attribute
        driver.get(link) # переход по ссылке при помощи метода get
        placelist = placelist + 1
        driver.save_screenshot("test.png") # сохранение скриншота
        sleep(3)
    inmenu()

def var1(driver):
    hatnotes = {}  # создание словаря
    elements = driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[3]/div[4]/ul/li")

    for index, element in enumerate(elements, start=1):
        hatnotes[index] = element

    for i in hatnotes:
        print(i, hatnotes[i].text)
        print("\n")

    whtlink = int(input("Куда вам надо? "))
    hatnote = hatnotes[whtlink]  # выбор элемента из списка
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")  # получение атрибута "href"
    driver.get(link)  # переход по ссылке
    sleep(3)
def var2(driver):
    hatnotes = {}  # создание словаря
    elements = driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[3]/div[4]/ul/li")

    for index, element in enumerate(elements, start=1):
        hatnotes[index] = element

    hatnote = hatnotes[1]  # выбор элемента из списка
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")  # получение атрибута "href"
    driver.get(link)  # переход по ссылке
def menu():
    print("1. Листать параграфы текущей страницы")
    print("2. Перейти на связанную страницу")
    print("3. Выход")
    var = int(input("Ваш выбор? "))
    if var == 1:
        var2(driver)
        invar1()
    if var == 2:
        var1(driver)
        inmenu()
    if var == 3:
        driver.quit()
def inmenu():
    print("1. Листать параграфы текущей страницы")
    print("2. Выход в главное меню")
    print("3. Выход из программы")
    var = int(input("Ваш выбор? "))
    if var == 1:
        invar1()
    if var == 2:
        menu()
    if var == 3:
        driver.quit()
menu()

# paragraphs = driver.find_elements(By.TAG_NAME, "p")
# for p in paragraphs:
#     print(p.text)
#     input("Press Enter to continue...")

# hatnote = choice(hatnotes) # выбор случайного элемента из списка
# link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href") # получение атрибута "href" элемента с помощью метода get_attribute
# driver.get(link) # переход по ссылке при помощи метода get
# sleep(3)
#
# driver.save_screenshot("test.png") # сохранение скриншота
# sleep(3)
# driver.quit() # закрытие браузера