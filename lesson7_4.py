import os
import json


def dict_creator(data, value):
    """Формирование словаря в формате {<kye>: (<number_of_files>, [type_of_files]), ...}"""

    extension_of_file = data[data.rfind('.'):]

    # Наполнение словаря данными
    try:
        number_of_files = result[value][0] + 1
        type_of_files = result[value][1]

        # Формирование списка типов файлов
        if extension_of_file not in type_of_files:
            type_of_files.append(extension_of_file)
        result[value] = (number_of_files, type_of_files)

    except KeyError:
        result[value] = (1, [extension_of_file])


folder = os.path.join(os.getcwd(), 'some_data')

result = {}

for item in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, item)):

        if os.stat(os.path.join(folder, item)).st_size >= 10 ** 5:
            dict_creator(item, 10**5)

        elif os.stat(os.path.join(folder, item)).st_size >= 10 ** 4:
            dict_creator(item, 10**4)

        elif os.stat(os.path.join(folder, item)).st_size >= 10 ** 3:
            dict_creator(item, 10**3)

        else:
            dict_creator(item, 10**2)

result = dict(sorted(result.items(), reverse=True))

with open(f'{"some_data"}_summary.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)

