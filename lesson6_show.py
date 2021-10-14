def output_info(info):
    """Функция вывода значений из получаемого генератора"""
    while True:
        try:
            print(next(info))
        except StopIteration:
            break


def read_file(argv):
    """Функция вывода информации согласно запросу пользователя"""
    program, *argv = argv

    with open('sales.txt', 'r', encoding='UTF-8') as file:
        content = (item for item in file.read().splitlines())

        """Организация логики вывода информации в зависимости от полученных параметров"""
        if not argv:
            output_info(content)
        elif len(argv) == 1:
            for _ in range(int(argv[0])-1):
                next(content)
            output_info(content)
        elif len(argv) == 2:
            for _ in range(int(argv[0])-1):
                next(content)
            for _ in range(int(argv[1])-2):
                print(next(content))


if __name__ == '__main__':
    import sys
    exit(read_file(sys.argv))
