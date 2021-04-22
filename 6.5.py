

class Stationery:
    def __init__(self, title = ""):
        self.title = title

    def draw(self):
        print(f'Hello Picasso {self.title}))')


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} - для рисковых")


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} - для новичков')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} - это уже по-взрослому')


stat = Stationery
stat.draw
pen = Pen("ручка")
pen.draw()
pencil = Pencil("карандаш")
pencil.draw()
handle = Handle("маркер")
handle.draw()