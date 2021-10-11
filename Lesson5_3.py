from itertools import zip_longest

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""Самодельная реализация"""


def contingent_generator(tmp_klass, tmp_tutor):
    """Функция-генератор состава классов"""

    for i in range(len(tmp_tutor)):
        """ Если индекс элемента меньше размера списка 'tmp_klass', то
        возвращается (<Ученик>,<Класс>), иначе (<Ученик>,None)"""

        yield tuple((tmp_tutor[i], tmp_klass[i]) if i < len(tmp_klass) else (tmp_tutor[i], None))


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена', 'Станислав',
          'Виктор', 'Василиса']

klasses = ['9А', '7В', '9Б', '9В', '8Б',
           '10А', '10Б', '9А']

contingent = contingent_generator(klasses, tutors)

print(type(contingent))      # Проверка, что объект 'contingent' генератор
for i in range(len(tutors)):
    print(next(contingent))  # Последовательный вывод кортежей

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""Реализация через zip_longest"""

contingent_zipped = zip_longest(tutors, klasses, fillvalue=None)
print(type(contingent_zipped))  # Но объект будет класса 'itertools.zip_longest'
print(*contingent_zipped)
