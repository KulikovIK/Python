class OwnException(Exception):
    def __init__(self, text):
        self.txt = text


a = int(input('Введите число А: '))
b = int(input('Введите число Б: '))

try:
    if b != 0:
        print(a / b)
    else:
        raise OwnException('Использовать ноль нельзя')
except OwnException as err:
    print(err)
