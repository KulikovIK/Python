def edit_file(argv):
    """Функция редактирования файла"""
    program, line_num, *argv = argv

    # Чтение исходного файла
    with open('sales.txt', 'r', encoding='UTF-8') as file:
        file.seek(0)
        content = (item for item in file.read().splitlines())

    # Построковая запись файла
    with open('sales.txt', 'w', encoding='UTF-8') as file:
        try:
            for _ in range(int(line_num) - 1):
                file.writelines(f'{next(content)}\n')
            file.writelines(f'{argv[0]}\n')
            next(content)
            while True:
                try:
                    file.writelines(f'{next(content)}\n')
                except StopIteration:
                    break
        except StopIteration:
            print('Такой строки ещё не существует')


if __name__ == '__main__':
    import sys

    exit(edit_file(sys.argv))
