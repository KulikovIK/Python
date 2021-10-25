class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print('Машина поехала')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn_it(self, direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}')


class TownCar(Car):

    def __init__(self, color='black', name='lada', is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        if self.speed >= 60:
            print('Сбавьте скорость!')
        else:
            print(f'Скорость автомобиля: {self.speed}')


class SportCar(Car):
    def __init__(self, color='ultramarine', name='Bugatti', is_police=False):
        super().__init__(color, name, is_police)


class WorkCar(Car):
    def __init__(self, color='grey', name='MAZ', is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        if self.speed >= 40:
            print('Сбавьте скорость!')
        else:
            print(f'Скорость автомобиля: {self.speed}')


class PoliceCar(Car):
    def __init__(self, color='white-blue', name='BMW', is_police=True):
        super().__init__(color, name, is_police)


test_car_1 = TownCar()
test_car_1.show_speed()
test_car_1.go(50)
test_car_1.show_speed()
test_car_1.go(80)
test_car_1.show_speed()
test_car_1.turn_it('left')
test_car_2 = PoliceCar()
print(test_car_2.is_police)
