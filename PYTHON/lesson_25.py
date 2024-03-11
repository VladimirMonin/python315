"""
TODO - NotImplemented - почему не получаем Exception
Lesson 25
Что такое магические методы?
__init__ - конструктор
__str__ - строковое представление объекта
__repr__ - представление объекта
__bool__ - логическое представление объекта
__len__ - длина объекта

Методы сравнения
__eq__ - равенство
__ne__ - неравенство
__lt__ - меньше
__le__ - меньше или равно
__gt__ - больше
__ge__ - больше или равно

`NotImplemented` – специальное значение, которое можно вернуть из
метода сравнения в случае, когда сравнение между операндами невозможно, как описано выше.

`NotImplementedError` – это исключение, которое возникает, когда
абстрактный метод должен быть имплементирован классом-наследником,
 если класс_MIXIN не поддерживает этот метод, то должно быть явно указано это
 через `NotImplementedError`, однако используется он для понятия ошибки разработки
 не тестирования доступности метода сравнения разных типов объектов.


Как это работает с наследованием?

@total_ordering - декоратор, который позволяет определить все методы сравнения
Нам надо определить метод проверки на равенство
И один из методов сравнения: меньше, меньше или равно, больше, больше или равно
"""
from functools import total_ordering

"""
Опишите класс Город, у которого есть следующие атрибуты:  
- название (name)  
- население (population)  
  
Импортируйте декоратор total_ordering из модуля functools  
Используйте декоратор total_ordering для определения всех методов сравнения, описав  
лишь необходимый минимум (сравнение только по населению).
  
Опишите метод __str__ для вывода информации о городе в виде:  
"Город: <name>, Население: <population>"  
  
Создайте несколько экземпляров класса Город и сравните их между собой.
Сделайте список городов и отсортируйте его.
"""
