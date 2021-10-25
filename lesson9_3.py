class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position (Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        total_income = self._Worker__income["wage"] + self._Worker__income["bonus"]
        return total_income


ivan = Position('Ivan', 'Ivanov', 'Master', 100, 10)


print(ivan.name)
print(ivan.surname)
print(ivan.position)
print(ivan._Worker__income)
print(ivan.get_full_name())
print(ivan.get_total_income())
print(ivan.__income)  # Тут будет AttributeError
