import time


class TrafficLight:

    def __init__(self):
        self.__color = ''

    def running_tl(self):
        time_color = {'red': 7, 'yellow': 2, 'green': 7}
        for running_color, running_time in time_color.items():
            self.__color = running_color
            print(self.__color)
            time.sleep(running_time)


tl = TrafficLight()

tl.running_tl()
