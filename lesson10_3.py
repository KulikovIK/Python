class Cell:
    def __init__(self, wol):
        self.wol = wol

    def __add__(self, other):
        return self.wol + other.wol

    def __sub__(self, other):
        return self.wol - other.wol if self.wol - other.wol >= 0 \
            else f'Операция не допустимаю Разность меньше нуля'

    def __mul__(self, other):
        return Cell(self.wol * other.wol)

    def __floordiv__(self, other):
        return Cell(self.wol // other.wol)

    def __truediv__(self, other):
        return Cell(self.wol // other.wol)

    def make_order(self, n):
        for _ in range(self.wol // n):
            print('*' * n)
        print('*' * (self.wol % n))


"""Объявление объектов класса Cell"""
a = Cell(12)
b = Cell(13)
c = Cell(5)

"""Демонстрация работы перегруженых операторов класса Cell"""
print(a + b)  # 125
print(a - b)  # Операция не допустима
print(a - c)  # 7
print((a * b).wol, type(a * b))  # 156 __main__.Cell
print((a / c).wol, type(a / c))  # 2 __main__.Cell
print((a // c).wol, type(a / c))  # 2 __main__.Cell

"""Демонстрация работы метода make_order"""
a.make_order(5)
