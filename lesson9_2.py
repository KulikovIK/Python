class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_road(self, thick):
        mass = (self._length * self._width * thick * 25) / 1000
        return mass


road_mass = Road(5000, 20)

print(road_mass.mass_of_road(5))
