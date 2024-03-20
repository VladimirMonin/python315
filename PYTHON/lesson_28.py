"""
Lesson 28
20.03.2024
ООП
Selenium webdriver
# Установка selenium - pip install selenium

# NoSuchElementException - исключение, которое возникает, когда элемент не найден


# Поиск элементв на странице с помощью объекта By
# find_element_by_id
# find_element(By.ID, "id")

# Какие варианты есть в By?
# By.ID
# By.NAME
# By.TAG_NAME
# By.CLASS_NAME
# By.LINK_TEXT
# By.PARTIAL_LINK_TEXT
# By.XPATH
# By.CSS_SELECTOR
"""
import json
import time
from pprint import pprint
from typing import List

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def get_driver(driver_options: list = None) -> webdriver.Chrome:
    """
    Создание драйвера с настройками.
    :param driver_options: Список строковых параметров для настройки драйвера.
    :return: Объект драйвера webdriver.Chrome.
    """
    options = webdriver.ChromeOptions()
    if driver_options:
        for option in driver_options:
            options.add_argument(option)
    driver = webdriver.Chrome(options)
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание 10 секунд
    return driver


SETTINGS = [
    "--start-maximized",  # Открыть браузер на весь экран
    # "--new-headless" # Открыть браузер в фоне
    "--incognito",  # Включить режим инкогнито
    # "--window-size=1920,1080", # Размеры окна
]



# Создаем экземпляр драйвера
driver = get_driver(SETTINGS)

# Переходим на сайт
# driver.get("http://books.toscrape.com/index.html")

# Ищем все товарные карточки на странице
# article class product_pod
# books : List[WebElement] = driver.find_elements(By.CLASS_NAME, "product_pod")

book_marks = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# result = []
# while True:
#     # Нашли все книги на странице
#     books = driver.find_elements(By.CLASS_NAME, "product_pod")
#
#     # Спарсили информацию о книгах на странице
#     for book in books:
#         # h3 > a[title] - содержимое title
#         title = book.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("title")
#         text_mark = book.find_element(By.CSS_SELECTOR, "p[class^='star-rating']").get_attribute("class").split()[1]
#         mark = book_marks.get(text_mark)
#         # Цена по имени класса price_color
#         price_str = book.find_element(By.CLASS_NAME, "price_color").text
#         price = float(price_str.lstrip('£'))
#         # Найдем наличие в продаже. Div product_price в нем второй ребенок p - содержит текст
#         in_stock_str = book.find_element(By.CSS_SELECTOR, "div.product_price").find_elements(By.TAG_NAME, "p")[1].text
#         in_stock = True if in_stock_str == "In stock" else False
#         # img_url - src тега img
#         row_img_url = book.find_element(By.TAG_NAME, "img").get_attribute("src")
#         img_url = f'{row_img_url.lstrip('..')}'
#
#
#         result.append({
#             "title": title,
#             "mark": mark,
#             "price": price,
#             "in_stock": in_stock,
#             "img_url": img_url
#         })
#
#
#
#     # Пробуем найти a с текстом Next
#     try:
#         next_page = driver.find_element(By.LINK_TEXT, "next")
#         next_page.click()
#         time.sleep(1)
#
#     except NoSuchElementException:
#         break
#
# # Сохраняем результат в файл json encoding='utf-8', ensure_ascii=False indent=4
# with open('books.json', 'w', encoding='utf-8') as file:
#     json.dump(result, file, ensure_ascii=False, indent=4)
#
# pprint(result, sort_dicts=False)


# Пробуем открыть локальный HTML файл
FILE = r'C:\Users\user\Syncthing\Работа\Academy_Top\ПРИМЕРЫ КОДА\python315\data\Books.htm'

driver.get(f'file://{FILE}')
time.sleep(10)