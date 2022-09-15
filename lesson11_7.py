class ComplexNumber:
    def __init__(self, num_str):
        self.number = num_str.split('+')

    def __add__(self, other):
        return ComplexNumber(f'{int(self.number[0]) + int(other.number[0])}'
                             f'+{int(self.number[1][:-1]) + int(other.number[1][:-1])}i')

    def __mul__(self, other):
        return ComplexNumber(
            f'{int(self.number[0]) * int(other.number[0]) - int(self.number[1][:-1]) * int(other.number[1][:-1])}+'
            f'{int(self.number[0]) * int(other.number[1][:-1]) + int(other.number[0]) * int(self.number[1][:-1])}i'
        )

    def __str__(self):
        if self.number[0] == '0':
            return f'{self.number[1]}'
        else:
            return f'{self.number[0]}+{self.number[1]}'


a = ComplexNumber('1+1i')
b = ComplexNumber('2+2i')
c = ComplexNumber('3+4i')

print(a)
print(a + b)
print(a * b)
print(a * c)
