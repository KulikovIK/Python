# Задание №1
duration = 90061  # Заданная длительность в секундах

seconds = duration % 60  # Секунды
minutes = duration // 60 % 60  # Минуты
hours = (duration // (60 ** 2)) % 24  # Часы
days = (duration // (60 ** 2)) // 24  # Дни

print('Заданная продолжительность времени составляет: ', end=' ')

if days:  # Проверка на необходимость вывода общего колличества дней
    print(f'{days} дн.', end=' ')
if hours:  # Проверка на необходимость вывода общего колличества часов
    print(f'{hours} час.', end=' ')
if minutes:  # Проверка на необходимость вывода общего колличества минут
    print(f'{minutes} мин.', end=' ')
print(f'{seconds} сек.')  # Вывод количества секунд

# Задание №1 (с применением цикла и списка)

# Список может быть полезен для хранения данных в одной переменной,
# но в конктретно данной задаче выглядит как спорное решение, так как
# надо запомнить что есть что в этом списке, словарь был бы удобнее

duration_and_cycle_list = [1]  # Задание "истинного" значения переменной для обработки первой итерации цикла

while duration_and_cycle_list:

    # Формирование списка параметров в формате (<введенное значение>, <секунды>, <минуты>, <часы>, <дни>)
    duration_and_cycle_list.clear()
    duration_and_cycle_list.append(int(input('Введите длительность времени в '
                                             'секндах или "0" для завершения: ')))

    if duration_and_cycle_list[0] != 0:

        duration_and_cycle_list.append(duration_and_cycle_list[0] % 60)  # Секунды
        duration_and_cycle_list.append(duration_and_cycle_list[0] // 60 % 60)  # Минуты
        duration_and_cycle_list.append((duration_and_cycle_list[0] // (60 ** 2)) % 24)  # Часы
        duration_and_cycle_list.append((duration_and_cycle_list[0] // (60 ** 2)) // 24)  # Дни

        print('Заданная продолжительность времени составляет: ', end=' ')

        if duration_and_cycle_list[4]:  # Проверка на необходимость вывода общего колличества дней
            print(f'{duration_and_cycle_list[4]} дн.', end=' ')
        if duration_and_cycle_list[3]:  # Проверка на необходимость вывода общего колличества часов
            print(f'{duration_and_cycle_list[3]} час.', end=' ')
        if duration_and_cycle_list[2]:  # Проверка на необходимость вывода общего колличества минут
            print(f'{duration_and_cycle_list[2]} мин.', end=' ')
        print(f'{duration_and_cycle_list[1]} сек.')  # Вывод количества секунд

    else:
        duration_and_cycle_list.clear()  # Очистка списка

print('Конец программы задиния №1', end='\n\n')

# Задание № 2а

numbers = [number**3 for number in range(1, 1001, 2)]  # добавлен шаг перебора

result_a = 0  # Объявление переменной для хранения результата вычислений

for unit in numbers:

    unit = str(unit)
    total = 0  # Объявление переменной для хранения суммы цифр в числе

    for digit in range(len(unit)):  # Объявление переменной суммы цифр в числе
        total += int(digit)

    result_a += int(unit) if total % 7 == 0 else 0  # Если сумма делится на 7, то результат суммируется

print(result_a)

# Задание № 2b и с

result_b = 0  # Объявление переменной для хранения результата вычислений

for unit in numbers:

    unit = str(unit + 17)
    total = 0  # Объявление переменной для хранения суммы цифр в числе

    for digit in range(len(unit)):
        total = total + int(digit)

    result_b += int(unit) if total % 7 == 0 else 0  # Если сумма делится на 7, то результат суммируется

print(result_b)
print('Конец программы задания №2', end='\n\n')

# Задание 3

wrong_numbers = [11, 12, 13, 14]  # Определения списка "неправильных" чисел

for i in range(1, 101):
    if i not in wrong_numbers and 0 < i % 10 <= 4:
        if i % 10 == 1:
            print (f'{i} процент')
        else:
            print(f'{i} процента')
    else:
        print(f'{i} процентов')

print('Конец программы задания №3')
