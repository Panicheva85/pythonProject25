import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_show_my_pets(selenium_driver):
    ''' Тест на проверку списка питомцев:
       1. Проверяем, что оказались на странице питомцев пользователя.
       2. Проверяем, что присутствуют все питомцы.  '''

    driver = selenium_driver

    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    driver.find_element_by_css_selector("a.nav-link[href='/my_pets']").click()
    time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # 1. Проверяем, что присутствуют все питомцы, для этого:
    # находим кол-во питомцев по статистике пользователя и проверяем, что их число
    # соответствует кол-ву питомцев в таблице

    # Устанавливаем явное ожидание
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))
    pets_number = driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    # pets_count = 100
    # Устанавливаем явное ожидание
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr')))
    pets_count = driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr')
    assert int(pets_number) == len(pets_count)

def test_all_info(selenium_driver):
    driver = selenium_driver

    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    driver.find_element_by_css_selector("a.nav-link[href='/my_pets']").click()
    time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

   # убедиться, что внутри каждого из них есть имя питомца, возраст и вид.
    driver.implicitly_wait(10)
    names = driver.find_elements_by_css_selector('.card-deck .card-title')
    driver.implicitly_wait(10)
    descriptions = driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
       assert names[i].text != ''
       assert descriptions[i].text != ''
       assert ', ' in descriptions[i]
       parts = descriptions[i].text.split(", ")
       assert len(parts[0]) > 0
       assert len(parts[1]) > 0

def test_half_pet_with_foto(selenium_driver):
    driver = selenium_driver

    # Нажимаем на кнопку входа в пункт меню Мои питомцы

    driver.find_element_by_css_selector("a.nav-link[href='/my_pets']").click()
    time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # 1. Проверяем, что присутствуют все питомцы, для этого:
    # находим кол-во питомцев по статистике пользователя и проверяем, что их число
    # соответствует кол-ву питомцев в таблице

    # явное ожидание
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))

    pets_number = driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]

    # убедиться, что Хотя бы у половины питомцев есть фото
    driver.implicitly_wait(10)
    images = driver.find_elements_by_css_selector('.card-deck .card-img-top')
    images_count = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            images_count += 1
    assert images_count < (int(pets_number)/2)

def test_different_name(selenium_driver):
    driver = selenium_driver
    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    driver.find_element_by_css_selector("a.nav-link[href='/my_pets']").click()
    time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # Устанавливаем явное ожидание
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr')))
    pets_count = driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr')

# Проверякем что у всех питомцев разные имена:
# Перебираем данные из pets_count, оставляем имя, возраст, и породу, остальное меняем на пустую строку
   # и разделяем по пробелу. Выбираем имена и добавляем их в список pets_name.
    name_pet = []
    for i in range(len(pets_count)):
       info_pet = pets_count[i].text.replace('\n', '').replace('×', '')
       info_pet_split = info_pet.split(' ')
       name_pet.append(info_pet_split[0])

   # Перебираем имена и если имя повторяется то прибавляем к счетчику m единицу.
   # Проверяем, если m == 0 то повторяющихся имен нет.
    m = 0
    for i in range(len(name_pet)):
       if name_pet.count(name_pet[i]) > 1:
         m += 1
    assert m == 0

def test_different_pets(selenium_driver):
    driver = selenium_driver

    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    driver.find_element_by_css_selector("a.nav-link[href='/my_pets']").click()
    time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'
    # явное ожидание
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr')))
    pets_count = driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr')

# Проверякем , что в списке нет повторяющихся питомцев:

# Перебираем данные из pets_count, оставляем имя, возраст, и породу, остальное меняем на пустую строку
   # и разделяем по пробелу.
    pets_all = []
    for i in range(len(pets_count)):
       info_pet_all = pets_count[i].text.replace('\n', '').replace('×', '')
       info_pet_split_all = info_pet_all.split(' ')
       pets_all.append(info_pet_split_all)

       # Склеиваем имя, возраст и породу, получившиеся склееные слова добавляем в строку
       # и между ними вставляем пробел
    pets_line = ''
    for i in pets_all:
        pets_line += ''.join(i)
        pets_line += ' '

       # Получаем список из строки line
    pets_line_list = pets_line.split(' ')

       # Превращаем список в множество
    pets_line_set = set(pets_line_list)

       # Из количества элементов списка вычитаем количество элементов множества
    result = len(pets_line_list) - len(pets_line_set)

       # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
    assert result == 0




