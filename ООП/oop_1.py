"""
    ООП

     Класс - общее описание предметной области на языке программирования
     Объект - экземпляр (конкретный представитель)
     Метод - функция свзанная с объектом класса (классом)
     Атрибут - характеристика (свойство) объекта или класса (это какбы переменные)
     Конструктор - метод, который управляет созданием объекта

     Инкапсуляция - механизм позволяющий скрывать внутренние детали реализации объекта и предоставлять доступ к ним,
     только, через определённые методы, чтобы защитить данные и кониролировать доступ к ним.
"""

class Car:
    _COLORS = ("red", "green", "blue", "")
    def __init__(self, brand, model, year, power, currency='RUB'):
        self.brand = brand
        self.model = model
        self.year = year
        self.power = power
        self.currency = currency
        self.is_power = False

        #защищённый атрибут
        self._color = ''

        #приватный атрибут
        self.__speed = 100

    def go(self):
        if self.is_power:
            print(f"{self.brand} {self.model} to go!")
        else:
            print("Car must be power on!")

    def stop(self):
        if self.is_power:
            print(f"{self.brand} {self.model} stop!")
        else:
            print("Car must be power on!")

    def turn(self, direction):
        if self.is_power:
            print(f"{self.brand} {self.model} TURN {direction.upper()}")
        else:
            print("Car must be power on!")

    def power_on(self):
        if self.is_power:
            print("Car is already power on!")
        else:
            print(f"{self.brand} {self.model} power on!")
            self.is_power = True


    def power_off(self):
        if not self.is_power:
            print("Car is already power off!")
        else:
            print(f"{self.brand} {self.model} power off!")
            self.is_power = False

    def display_color(self):
        print(self._color)

    def set_color(self, new_color):
        if new_color in Car._COLORS:
            self._color = new_color
        else:
            raise ValueError("Неправильный цвет")

    # Getter для получения значения скороcти
    @property #декоратор, позваляющий обращаться к методу, как в параметру
    def speed(self):
        return self.__speed

    # Setter для получения скорости, имя которого задаётся от имени параметра
    @speed.setter
    def speed(self, value):
        if value > 300:
            raise ValueError('Max speed 300')
        self.__speed = value

# Дочерний класс грузовых машин
class Truck(Car):
    # Указываем характеристики родительского класса и новые характеристики дочернего класса
    def __init__(self, brand, model, year, power, capasity, axles, currency='RUB'):
        # Вызываем конструктор родительского класса с его параметрами через функцию super
        super().__init__(brand, model, year, power, currency='RUB')
        self.capasity = capasity
        self.axles = axles
    def tilt_trailer(self):
        print(f'{self.brand} {self.model} tilt trailer')
    def power_off(self):
        super().power_off()
        print('The method of Truck class')


car_audi = Car(brand="Audi", model="A6", year=2024, power=249)
car_bmw = Car(brand='BMW', model='X5', year=2022, power=249)

truck = Truck(brand='Volvo', model='xxx', year=2019, capasity=4000, axles=4, power=700)
truck.tilt_trailer()
print(car_bmw.speed)
