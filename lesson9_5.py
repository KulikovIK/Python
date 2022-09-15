class Stationery:
    title = 'название'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'ручка'

    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print('Рисуем маркером')


item_pen = Pen()
item_pencil = Pencil()
item_handle = Handle()

print(item_pen.title)
print(item_pencil.title)
print(item_handle.title)

item_pen.draw()
item_pencil.draw()
item_handle.draw()
