"""
Разбор домашнего задания 23
Расшифровка секретного послания
"""

"""  
Вам пришло секретное послание. Оно содержит много странных символов, которые вы не можете понять.  
Но вы знаете, что в этом послании используются только маленькие русские буквы. Используйте знание языка Python  
а так же знание for i чтобы расшифровать его.  
"""

# Секретное послание
secret_letter = [
    ['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
                 ['оafбasdf%^о^FFжа$#af243ю'], ['afпFsfайFтFsfо13н'],
                 ['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
                 ['и$##sfF'], ['вSFSDам'], ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
                 ['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']
    ]

# Список с маленькими русскими буквами
small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
             'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


result_string = ''
# Нам нужно сделать цикл
# Проходим по спискам
for list_ in secret_letter:
    # разделяем пробелами слова
    result_string += ' '
    # сразу проходим по буквам, взяв 0й элемент списка
    for letter in list_[0]:
        # если список есть в списке маленьких букв
        # то добавляем в строку
        if letter in small_rus:
            result_string += letter


print(result_string)
print(result_string.strip().capitalize())

# Вариант №2 - comrehension
result_string = ''.join([letter for list_ in secret_letter for letter in list_[0] if letter in small_rus])
print(result_string)