def thesaurus(*args, need_sort=False):
    """Функция принимающая перечень аргументов для формирования словаря.
    Параметр need_sort определяет необходимость сортировки по ключу, по умолчанию
    False - сортировка не требуется"""

    thesaurus_dict = {}  # Результирующий словарь

    key_list = [item[0] for item in args]

    for key in key_list:  # Перебор значений item_list на соответствие ключам из key_list
        thesaurus_dict[key] = [item for item in args if key == item[0]]

    if need_sort:  # Ввборка элементов словаря и сортировка их по ключу
        thesaurus_dict = dict(sorted(thesaurus_dict.items()))

    return thesaurus_dict


print(thesaurus('Илья', 'Наташа', 'Игорь', 'Виктория', 'Денис', need_sort=False))
print(thesaurus('Илья', 'Наташа', 'Игорь', 'Виктория', 'Денис', need_sort=True))
