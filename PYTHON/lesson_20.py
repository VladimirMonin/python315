"""
Lesson 20
21.02.2024
Git и GitHub

Разрешаем конфликт слияния
"""


def say_hello(name: str) -> None:
    """
    Приветствие пользователя по имени
    :param name: имя пользователя
    :return: строка приветствия
    """
    print(f"Hello, {name}!")


def get_name() -> str:
    """
    Получение имени пользователя
    :return: имя пользователя
    """
    name = input("Enter your name: ")
    return name


if __name__ == "__main__":
    name = get_name()
    say_hello(name)
