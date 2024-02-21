"""
Lesson 20
21.02.2024
Git и GitHub

"""


def say_hello(name: str) -> None:
    """
    Приветствие
    :param name:
    :return:
    """
    print(f"Hello, {name}!")


def get_name() -> str:
    name = input("Enter your name: ")
    return name


if __name__ == "__main__":
    name = get_name()
    say_hello(name)
