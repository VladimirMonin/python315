"""
Разбор hw_33

#### Класс `TxtFileHandler`

1. `read_file(filepath)`: Метод для чтения данных из TXT файла. Должен быть реализован как метод экземпляра.
2. `write_file(filepath, data)`: Метод для записи данных в TXT файл. Должен быть реализован как метод экземпляра.
3. `append_file(filepath, data)`: Метод для дописывания данных в TXT файл. Должен быть реализован как метод экземпляра.

#### Класс `JsonFileHandler`

1. `read_file(filepath, as_dict=False)`: Метод для чтения данных из JSON файла. Флаг `as_dict` работает аналогично как в классе `CsvFileHandler`. Должен быть реализован как метод экземпляра.
2. `write_file(filepath, data, as_dict=False)`: Метод для записи данных в JSON файл. Флаг `as_dict` работает аналогично как в классе `CsvFileHandler`. Должен быть реализован как метод экземпляра.
3. `append_file(filepath, data)`: Метод для дописывания данных в JSON файл. При попытке вызова этого метода должно возникать исключение `TypeError` с сообщением, что данный тип файла не поддерживает операцию дописывания. Должен быть реализован как метод экземпляра.

"""
from typing import List, Dict
import json


# Класс ошибки JsonAppendError

class JsonAppendError(Exception):
    pass


class TxtFileHandler:
    """
    Класс для работы с TXT файлами
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def read_file(self):
        """
        Метод для чтения данных из TXT файла, пытаеся открыть файл, если файл не найден, выводит сообщение
        Если файл найден, читает его и возвращает данные. Данные сохраняются в атрибуте экземпляра `data`
        :return:
        :raises: FileNotFoundError: если файл не найден
        """
        try:
            with open(self.filepath, 'r') as file:
                self.data = file.read()
                return self.data
        except FileNotFoundError:
            print(f'Файл {self.filepath} не найден')

    def write_file(self, data):
        pass

    def append_file(self, data):
        pass


class JsonFileHandler:
    """
    Класс для работы с JSON файлами. Работает с List и Dict
    """

    def __init__(self, filepath, encoding='utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self.data = None

    def write_file(self, data: List | Dict):
        """Ensure ascii False indend 4"""
        with open(self.filepath, 'w', encoding=self.encoding) as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def append_file(self, data):
        raise JsonAppendError('Данный тип файла не поддерживает операцию дописывания')
        """
        Альтернативная реализация. Если вы работаете со списками (список словарей, список списков и т.д.)
        Вы можете расширить один список другим и записать его в файл используя метод write_file
        """
