from time import sleep


class TrafficLight:
    __color = ""

    def start(self):
        while True:
            print("Красный")
            sleep(7)
            print("Жёлтый")
            sleep(2)
            print("Зелёный")
            sleep(10)


T = TrafficLight()
T.start()