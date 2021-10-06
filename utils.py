from lesson4_2 import currency_rates as cr


def currency(argv):

    programm, *args = argv
    print(f'Выполняется программа {programm}')
    cr(args[0])


if __name__ == "__main__":
    import sys

    exit(currency(sys.argv))
