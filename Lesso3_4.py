def find_index(data, separate=None):
    """Функция принимающая перечень аргументов для формирования списка ключей словаря.
    Параметр separate определяет необходимость выбора ключа из фамилии"""

    processed_keys = []  # Список ключей

    for item in data:
        sep_index = item.index(' ') + 1 if separate == ' ' else 0  # Выбор требуемого символа в строке
        if item[sep_index] not in processed_keys:
            processed_keys.append(item[sep_index])  # Формирование списка ключей

    return processed_keys


def create_dict(data):
    """Функция создания словаря вида {X:{Y:[Z]}} из последовательности параметров"""

    dict_first, dict_last = {}, {}  # Объявление вложенного и основного словаря

    for last_key in find_index(data, ' '):  # Генерация и перебор ключей основного словаря - "фамилии"
        for first_key in find_index(data):  # Генерация и перебор ключей вложенного словаря - "имена"
            item_list = [item for item in data
                         if first_key == item[0] and
                         last_key == item[item.index(' ') + 1]]     # Генератор списка для вложенного словаря
            if item_list:                                           # Если список не пустой, то помещаем его
                dict_first[first_key] = item_list                   # во вложенный словарь

        dict_last[last_key] = dict_first.copy()  # Помещение вложенного словаря в основной
        dict_first.clear()

    return dict_last


def thesaurus_adv(*args, need_sort=False):
    """Функция принимающая перечень аргументов для формирования словаря.
    Параметр need_sort определяет необходимость сортировки по ключу, по умолчанию
    False - сортировка не требуется"""

    thesaurus_dict = create_dict(args)

    if need_sort:  # Сортировка по ключу "фамилия"
        thesaurus_dict = dict(sorted(thesaurus_dict.items()))

    return thesaurus_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", need_sort=True))
