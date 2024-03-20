"""
Lesson 28
20.03.2024
ООП
Selenium webdriver
# Установка selenium - pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройки
options = webdriver.ChromeOptions()

SETTINGS = [
    "--start-maximized",  # Открыть браузер на весь экран
     # "--new-headless" # Открыть браузер в фоне
    "--incognito",  # Включить режим инкогнито
    # "--window-size=1920,1080", # Размеры окна
]

for params in SETTINGS:
    options.add_argument(params)

# Создаем экземпляр драйвера
driver = webdriver.Chrome(options=options)

# Переходим на сайт
driver.get("https://www.google.com")
# Скриншот страницы
driver.save_screenshot("google.png")
time.sleep(2)



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

# Ищем по CSS texarea аттрибут title="Поиск"
search_input = driver.find_element(By.CSS_SELECTOR, 'textarea[title="Поиск"]')

# Ввожу сообщение
message = "Привет группа!"
search_input.send_keys(message)

# Нажемем enter через клавиатуру (KEYS)
search_input.submit()
# search_input.send_keys(webdriver.common.keys.Keys.ENTER)
time.sleep(5)

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
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание 10 секунд
    return driver
