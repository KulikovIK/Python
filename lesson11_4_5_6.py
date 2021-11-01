class Warehouse:
    _in_warehouse = {}
    _in_use = {}

    def __str__(self):
        return f'Техника на складе {self._in_warehouse}\nТехника в работе {self._in_use}\n'

    @staticmethod
    def validate(val_data):
        if val_data[0] in ['1', '2'] and val_data[1] in ['ксерокс', 'принтер', 'сканер'] and val_data[3].isdigit():
            return True
        else:
            print('Проверьте введенные данные!\n'
                  'Строка данных должна иметь вид\n'
                  '<операция> <тип оборудования> <наименование> <количество> <доп. информация>')

    @classmethod
    def insert(cls, other):
        if other.type not in cls._in_warehouse.keys():
            cls._in_warehouse.setdefault(other.type, {other.name: other.quantity, 'info': other.info})
        elif other.name in cls._in_warehouse[other.type].keys():
            cls._in_warehouse[other.type][other.name] += other.quantity
        else:
            cls._in_warehouse[other.type].setdefault(other.name, 1)

    @classmethod
    def used(cls, other):
        if 0 < cls._in_warehouse[other.type][other.name] >= other.quantity:
            cls._in_warehouse[other.type][other.name] -= other.quantity
            if other.type not in cls._in_use.keys():
                cls._in_use.setdefault(other.type, [other.name])
            else:
                cls._in_use[other.type].append(other.name)
        else:
            cls._in_warehouse[other.type].pop(cls._in_warehouse[other.type].index(other.name))


class OfficeEquip:
    def __init__(self, type_of, quantity=1, name=None):
        self.type = type_of
        self.name = name
        self.quantity = quantity


class Printer(OfficeEquip):
    def __init__(self, data):
        super().__init__('прентер', int(data[1]), data[0])
        self.info = data[2:]


class Scanner(OfficeEquip):
    def __init__(self, data):
        super().__init__('сканер', int(data[1]), data[0])
        self.info = data[2:]


class Xerox(OfficeEquip):
    def __init__(self, data):
        super().__init__('ксерокс', int(data[1]), data[0])
        self.info = data[2:]


while True:
    print('Что нужно сделать?\n'
          '1 - ввести данные о поступлении на склад\n'
          '2 - ввести данные о выдачи техники в работу\n'
          '3 - показать содержимое\n'
          '4 - выход из программы\n')

    data = input().split(' ')

    if data[0] == '4':
        break
    elif data[0] == '3':
        print(Warehouse())
    elif Warehouse.validate(data):

        if data[0] == '1':
            if data[1].lower() == 'ксерокс':
                Warehouse.insert(Xerox(data[2:]))
            elif data[1].lower() == 'принтер':
                Warehouse.insert(Printer(data[2:]))
            elif data[1].lower() == 'сканер':
                Warehouse.insert(Scanner(data[2:]))
        else:
            if data[1].lower() == 'ксерокс':
                Warehouse.used(Xerox(data[2:]))
            elif data[1].lower() == 'принтер':
                Warehouse.used(Printer(data[2:]))
            elif data[1].lower() == 'сканер':
                Warehouse.used(Scanner(data[2:]))
