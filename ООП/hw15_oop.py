import time


class TrafficLight:
    _colors = ('red','yellow','green','yellow')

    # Стрелочная функция, которая выкрашивает текст в соответсвующий цвет
    static = lambda self : f'\033[{self.color_num()}m{self.color}\033[0m'
    # Хотела добавить мигание, но нынешние консоли его не поддерживают
    # dynamic = lambda self : f'\033[5;{self.color_num()}m{self.color}\033[0m'

    def __init__(self):
        self.color = 'green'

    # Метод принудительной смены цвета с защитой от некорректного
    def change_color(self, color):
        if color in self._colors:
            self.color = color
            print(f'The traffic light has turned {self.color}')
        else:
            print(f'The traffic light does not have a {color} color')

    # Метод, где задаётся время между переключением цветов
    def time_scip(self):
        if self.color == 'yellow':
            time.sleep(5)
        else:
            time.sleep(15)
        print(f'The {self.static()} light is blinking') # Мигание предполагалось здесь
        time.sleep(5)

    # Выделила соответствующие цветам коды
    def color_num(self):
        if self.color == 'red':
            return 31
        elif self.color == 'green':
            return 32
        else:
            return 33

    # Добавила счётчик, чтобы наглядно было видно, на сколько времени рассчитан один цикл светофора
    # @staticmethod
    # def timing(func):
    #     def wrapper(*args, **kwargs):
    #         star = time.time()
    #         result = func(*args, **kwargs)
    #         end = time.time()
    #         print(f'Время выполнения {end - star} сек.')
    #         return result
    #     return wrapper

    # Метод запуска одного цикла смены цветов
    # @timing
    def start(self):
        # print(f'The {self.color} light is on')
        for i in range(len(self._colors)):
            if self.color == self._colors[i]:
                self.time_scip()
                if i<3:
                    self.color = self._colors[i+1]
                else:
                    self.color = self._colors[0]

                print(f'The traffic light has turned {self.static()}')

    # Метод запуска заданного количества циклов
    def cycle(self, count):
        print(f'The {self.static()} light is on')
        i = 1
        while i <= count:
            self.start()
            i += 1


traffic_light = TrafficLight()
traffic_light.change_color('red')
traffic_light.change_color('pink')
# traffic_light.start()
traffic_light.cycle(2)
# print(traffic_light._colors)