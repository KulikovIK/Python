from itertools import zip_longest


class Matrix:
    """Объявление класса Matrix"""
    def __init__(self, data):
        self.matrix = data

    def __str__(self):
        """"Перегрузка оператора фывода для формирования матрицы на экране"""
        print(f'-' * (len(self.matrix[0])*6+1))
        for items in self.matrix:
            for item in items:
                print(f'| {item:^4d}', end='')
            print('|')
        return f'-' * (len(self.matrix[0])*6+1)

    def __add__(self, other):
        """Перегрузка оператора сложения.
        zip_longest выбран с целью недопущения потери данных в складываемых матрицах"""
        sum_matrix = []
        for items_self, items_other in zip_longest(self.matrix, other.matrix, fillvalue=0):
            result = list(map(lambda x: x[0] + x[1],
                              zip_longest(items_self, items_other, fillvalue=0)))
            sum_matrix.append(result)
        return Matrix(sum_matrix)


"""Объявление объектов класса Matrix"""
matrix_2_2 = Matrix([[1, 2], [1, 2]])  # Матрица 2*2
matrix_3_3 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])  # Матрица 3*3
matrix_2_4 = Matrix([[1, 2, 3, 4], [1, 2, 3, 4]])  # Матрица 4*2

"""Демонстрация работы метода вывода на экран"""
print(matrix_2_2)
print(matrix_3_3)

"""Демонстрация работы метода сложения"""
print(matrix_2_2 + matrix_2_4, '\n', type(matrix_2_2 + matrix_2_4))
