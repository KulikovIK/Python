from abc import ABC, abstractmethod


class Clothes(ABC):
    """Объявление абстрактного родительского класса Clothes"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def total(self):
        pass


class Coat(Clothes):
    """Объявление дочернего класса Clothes - Coat"""
    def __init__(self, value):
        self.h = value

    @property
    def total(self):
        return self.h / 6.5 + 0.5


class Suit(Clothes):
    """Объявление дочернего класса Clothes - Suit"""
    def __init__(self, value):
        self.v = value

    @property
    def total(self):
        return self.v * 2 + 0.3


"""Объявление объектов классов Coat и Suit"""
coat = Coat(46)
suit = Suit(1.78)

"""Демонтрация работы метода total"""
print(f'{coat.total + suit.total:.2f}')
