def rand_gen(n):
    """Функция-Генератор нечетных чисел от 1 до n"""

    for i in range(1, n + 1, 2):
        yield i


iterations = int(input('Введите i: '))

odd_to = rand_gen(iterations)
print(next(odd_to))  # Вывод первого элемента
print(next(odd_to))  # Вывод второго элемента
print(*odd_to)       # Вывод оставшихся элементов

"""Генератор нечетных чисел от 1 до n"""

odd_to_adv = (i for i in range(1, iterations + 1, 2))

print(next(odd_to_adv))  # Вывод первого элемента
print(next(odd_to_adv))  # Вывод второго элемента
print(*odd_to_adv)       # Вывод оставшихся элементов
