def open_file():
    """Функция возвращающая генератор считываемых данных"""
    file_name_def = f'{input("")}.csv'
    with open(file_name_def, 'r') as users_f:
        processing_list = (item for item in users_f.read().split('\n'))
        return processing_list


def file_union():
    """Функция объединения данных из файлов указанных пользователем"""
    print('файл с пользователями: ', end='')
    users_list = open_file()
    print('файл с хобби: ', end='')
    hobby_list = open_file()

    # Построковая запись в файл, указанный пользователем
    file_name = f'{input("Введите имя файла для записи ")}.txt'
    with open(file_name, 'w', encoding='UTF-8') as f_users_hobby:

        while True:
            try:
                key = next(users_list)
                try:
                    f_users_hobby.writelines(f'{key}: {next(hobby_list)}\n')
                except StopIteration:
                    f_users_hobby.writelines(f'{key}: {None}\n')
            except StopIteration:
                print('1')
                break


if __name__ == '__main__':

    exit(file_union())
