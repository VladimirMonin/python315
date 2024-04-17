"""
Lesson 36: Поведенческие паттерны
- Strategy - стратегия
- Observer - наблюдатель
- Visitor - посетитель
- State - состояние
"""

# State - состояние. 

"""
1. Класс создающий экземплер Браузера
2. Класс контекст состояний
3. Класс сосстояния, в котором браузер идет на сайт book.toscrape.com
4. Класс сосстояния, в котором браузер идет на сайт Гугл
5. Фасад для управления состояниями и получения задачи от пользователя __call__
"""

from abc import ABC, abstractmethod
from tkinter import N
from selenium import webdriver
from selenium.webdriver.common.by import By


class Chrome():
    """
    Класс создающий экземплер Браузера
    """
    def __init__(self, settings=None, implicity_wait=10):
        self.settings = settings
        self.implicity_wait = implicity_wait

    def get_options_object(self):
        """
        Получение объекта настроек для Chrome
        """
        options = webdriver.ChromeOptions()
        if self.settings:
            for option in self.settings:
                options.add_argument(option)
        return options

    def get_driver(self):
        """
        Получение драйвера для Chrome
        """
        options = self.get_options_object()
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(self.implicity_wait)
        return driver
    
    def __call__(self):
        """
        Получение драйвера для Chrome
        """
        return self.get_driver()



class Browser:
    def __init__(self, state: "State", driver: Chrome):
        self.state = state
        self.driver = driver

    def change_state(self, state: "State"):
        self.state = state

    def work(self):
        self.state.work(self.driver)


class State(ABC):
    def __init__(self, driver: Chrome):
        self.driver = driver

    @abstractmethod
    def work(self):
        pass


class BookToscrapeState(State):
    def work(self):
        self.driver.get("http://books.toscrape.com")
        time.sleep(5)


class GoogleState(State):
    def work(self):
        self.driver.get("http://google.com")
        # Ищем поисковую форму title="Поиск"
        search_form = self.driver.find_element(By.CSS_SELECTOR, "input[name='q']")
        search_form.send_keys("Котики")
        search_form.submit()


class MainFacade:
    def __init__(self):
        self.driver = Chrome()()
        self.state = GoogleState(self.driver)
        self.browser = Browser(self.state, self.driver)

    def __call__(self):
        while True:
            task = input("Введите задачу: ")
            if task == "google":
                self.browser.change_state(GoogleState(self.driver))
            elif task == "book":
                self.browser.change_state(BookToscrapeState(self.driver))
            elif task == "exit":
                break
            self.browser.work()


if __name__ == "__main__":
    MainFacade()()