from symtable import Class


class Car:

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


car_bmw = Car(brand='BMW', model='X5', year=2022, power=249)

truck = Truck(brand='Volvo', model='xxx', year=2019, capasity=4000, axles=4, power=700)
truck.tilt_trailer()
print(car_bmw.speed)
