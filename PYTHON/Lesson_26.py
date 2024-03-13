"""
Lesson 26
13.03.2024
Магические методы Ч2
Магические методы для математических операций
__add__ - сложение
__sub__ - вычитание
__mul__ - умножение
__truediv__ - деление
__floordiv__ - целочисленное деление
__mod__ - остаток от деления
__pow__ - возведение в степень


Магические методы для операций inplace
__iadd__ - сложение
__isub__ - вычитание
__imul__ - умножение
__itruediv__ - деление

Практика - игровые персонажи, здоровье и мана
"""
"""
Создать класс Health (опишите логику вычитания здоровья и добавления здоровья)
1 аттрибут - значение (value)

Создать класс Berserk
В нем есть  здоровье Health class


"""


class Health:
    def __init__(self, value, owner):
        self.value = value
        self.max_value = value  # Запоминаем максимальное значение для определения 20% порога
        self.owner = owner  # Ссылка на объект Berserk

    def __add__(self, other):
        self.value += other
        self.check_bersek_mode()
        return self

    def __sub__(self, other):
        self.value -= other
        self.check_bersek_mode()
        return self

    def check_bersek_mode(self):
        if self.value <= self.max_value * 0.2:  # Если здоровье меньше 20%
            self.owner.turn_on_bersek()
        else:
            self.owner.turn_off_bersek()


class Berserk:
    def __init__(self, health: int = 120, damage: int = 50):
        self.health = Health(health, self)  # Передаем self в Health, чтобы Health мог управлять режимом берсерка
        self.base_damage = damage
        self.damage = damage
        self.is_bersek = False

    def turn_on_bersek(self):
        if not self.is_bersek:  # Активируем режим берсерка только если он уже не активирован
            self.damage *= 3
            self.is_bersek = True
            print("Режим берсерка включен!")

    def turn_off_bersek(self):
        if self.is_bersek:  # Деактивируем режим берсерка только если он был активирован
            self.damage = self.base_damage
            self.is_bersek = False
            print("Режим берсерка выключен!")

# Проверка
b = Berserk()
print(b.health.value)
b.health + 10  # Добавляем здоровье
print(b.health.value)
b.health - 130  # Снижаем здоровье для активации режима берсерка
print(b.health.value)
print(b.damage)
b.health + 100  # Восстанавливаем здоровье для деактивации режима берсерка
print(b.health.value)
print(b.damage)
