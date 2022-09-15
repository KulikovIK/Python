import os


def creator(data):
    """Функция создающая директорию или файл"""
    if '.' in data:
        with open(data[data.find('|--') + 3:-1], 'w', encoding='UTF-8'):
            pass
    else:
        os.mkdir(os.path.join(os.getcwd(), data[data.find('|--') + 3:-1]))


with open('config.ini', 'r', encoding='UTF-8') as file:
    depth = 0  # Определитель предыдущего места в ветви
    target_folder = ''  # Определитель предыдущей директории
    for line in file:

        # Определитель текущего места в ветви
        current_depth = (line.find('|--') - line.find('|')) // 2

        # Переход в поддиректорию, созданную ранее
        if current_depth > depth:
            os.chdir(target_folder)
            creator(line)

        # Создание поддиректории или файла
        elif current_depth == depth and line.startswith(' '):
            creator(line)

        # Создание корневой директории и переход в неё
        elif current_depth == depth and line.startswith('|--'):
            creator(line)
            os.chdir(line[line.find('|--') + 3:-1])
        else:
            # "Подъем" на требуемое количество поддиректорий
            for _ in range(depth - current_depth):
                os.chdir('..')
            creator(line)

        # Запоминание текущей директории и её места в ветви
        target_folder = line[line.find('|--') + 3:-1]
        depth = current_depth
