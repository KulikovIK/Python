def write_file(argv):
    """Функция записи данных, вводимых пользователем"""
    program, file_name, *argv = argv
    with open(f'{file_name}', 'a', encoding='UTF-8') as file:
        file.write(f'{argv[0]}\n')


if __name__ == '__main__':
    import sys
    exit(write_file(sys.argv))
