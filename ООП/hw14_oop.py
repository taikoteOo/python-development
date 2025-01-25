import random


# Создаём класс Animal
class Animal:
    _sizes = ('big', 'medium', 'small')
    _satiety_levels = ('very hungry','hungry', 'not hungry', 'full', 'very full')

    # Конструктор
    def __init__(self, species, color, size):
        self.species = species
        self.color = color
        if size in Animal._sizes:
            self.size = size
        else:
            self.size = 'unknown'
        self.sleeping = False
        self.running = False
        self.name = 'animal'
        self._paws = 4
        self.__satiety_level = 3


    # Методы
    def sleep(self):
        if self.sleeping:
            print(f'The {self.name} is already sleeping')
        else:
            self.sleeping = True
            print(f'The {self.name} fell asleep')

    def wake_up(self):
        if self.sleeping:
            self.__wake_up()
        else:
            print(f'The {self.name} does not sleep')

    def run(self):
        if self.sleeping:
            print(self._twitches_paw())
        elif self.running:
            print(f'The {self.name} is already running')
        else:
            self.running = True
            print(f'The {self.name} run')

    def stop(self):
        if self.running:
            self.running = False
            print(f'The {self.name} stopped')
        else:
            print(f'The {self.name} does not run')

    # Геттер и сеттер
    @property
    def satiety_level(self):
        return self.__satiety_level

    @satiety_level.setter
    def satiety_level(self, new_level):
        if 1 <= new_level <= 5:
            self.__satiety_level= new_level
        elif new_level < 1:
            raise ValueError(f'A satiety level of less than 1 will harm the {self.name}!')
        else:
            raise ValueError(f'The {self.name}\'s satiety cannot be more than 5!')


    # Защищённый и приватный методы
    def _twitches_paw(self):
        return f'The {self.name} twitches its paw in its sleep'

    def __wake_up(self):
        num = random.randint(1,100)
        if 1 <= num < 34:
            self.sleeping = False
            print(f'The {self.name} woke up')
        elif 34 <= num < 67:
            print(f'The {self.name} does not wake up')
        elif 67 <= num < 100:
            print(self._twitches_paw())
        else:
            print(f'Aww, you\'ve been given a gentle nibble\nThe {self.name} continues to sleep')


# Создаём класс Cat
class Cat(Animal):
    def __init__(self, color, size, eye_color, breed, species='Cat'):
        super().__init__(species, color, size)
        self.eye_color = eye_color
        self.voice= 'meow'
        self.breed = breed
        self.name = 'cat'

    # Личные методы
    def sound(self):
        print(f'The {self.name} makes \'{self.voice}\'')

    def play(self):
        if self.sleeping:
            print(self._twitches_paw())
        else:
            print(f'The {self.name} plays')

    def _licking(self):
        print(f'The {self.name} is licking himself')

    def eat(self):
        if self.sleeping or self.running:
            print(f'The {self.name} cannot eat now')
        else:
            try:
                self.satiety_level += 1
                print(f'The {self.name} eats')
                print(f'The {self.name} is {Animal._satiety_levels[self.satiety_level-1]}')
            except:
                print(f'The {self.name} can no longer eat!')

    # Перезапись родительского метода
    def stop(self):
        if self.running:
            self.running = False
            print(f'The {self.name} stopped')
            num = random.randint(1, 5)
            if  num == 5:
                self._licking()
        else:
            print(f'The {self.name} does not run')



animal = Animal('cat', 'red', size='medium')
animal.sleep()
animal.run()
animal.wake_up()
animal.wake_up()
animal.run()
animal.stop()
cat = Cat('brown', size='medium', eye_color='blue', breed='munchkin')
cat.sound()
cat.run()
cat.stop()
cat.play()
cat.eat()
cat.eat()
cat.eat()
