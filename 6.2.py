

class Road:
    def __init__(self, leght, width):
        self._length = leght
        self._width = width


    def get_full_profit(self, weight = 25, thickness = 5 ):
        return f"{(self._length * self._width * weight * thickness) / 1000}"


road = Road (5000, 20)
print(road.get_full_profit())