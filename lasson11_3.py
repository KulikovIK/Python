class OwnException(Exception):
    @staticmethod
    def validate(data):
        return True if data.isdigit() else print('Вводить можно только числа')


new_dict = []

while True:
    new_data = input('Введите число: ')
    if new_data != 'stop':
        if OwnException.validate(new_data):
            new_dict.append(new_data)
    else:
        break

print(new_dict)
