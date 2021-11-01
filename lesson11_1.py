class Date:
    def __init__(self, date_str):
        self.date = date_str

    @classmethod
    def date_pars(cls, param):
        return cls([int(item) for item in param.split('-')])

    @staticmethod
    def validate(date):
        if type(date) == str:
            data = Date.date_pars(date)
        elif type(date) == list:
            data = Date(date)
        else:
            data = date
        if 1 <= data.date[0] <= 31 and 1 <= data.date[1] <= 12 and 0 <= data.date[2] <= 2021:
            return 'Все нормально'
        else:
            return 'Данные не соответствуют формату'


print(Date.validate([1, 1, 2001]))
print(Date.validate('01-01-2001'))
a = Date('02-02-2002')
print(a.date)
b = Date.date_pars('03-03-2003')
print(b)
print(Date.validate(b))


