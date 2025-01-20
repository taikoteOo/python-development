import random


class Animal:
    _sizes = ('big', 'medium', 'small')
    def __init__(self, species, color, size):
        self.species = species
        self.color = color
        if size in Animal._sizes:
            self.size = size
        else:
            self.size = 'unknown'
        self.sleeping = False
        self.running = False
        self._paws = 4
        self.__existence = True
        self.name = 'animal'

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
            print(f'The {self.name} ran')

    def stop(self):
        if self.running:
            self.running = False
            print(f'The {self.name} stopped')
        else:
            print(f'The {self.name} does not run')

    def eat(self):
        if self.sleeping or self.run:
            print(f'The {self.name} cannot eat now')
        else:
            print(f'The {self.name} eats')



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

class Cat(Animal):
    def __init__(self, color, size, eye_color, breed, species='Cat'):
        super().__init__(species, color, size)
        self.eye_color = eye_color
        self.voice= 'meow'
        self.breed = breed
        self.name = 'cat'

    def sound(self):
        print(f'The {self.name} makes \'{self.voice}\'')

    def play(self):
        if self.sleeping:
            print(self._twitches_paw())
        else:
            print(f'The {self.name} plays')

    def _licking(self):
        print(f'The {self.name} is licking himself')

    def wake_up(self):
        if self.sleeping:
            Animal.__wake_up()
            if not self.sleeping:
                self._licking()
        else:
            print(f'The {self.name} does not sleep')






animal = Animal('cat', 'red', size='medium')
animal.sleep()
animal.run()
animal.wake_up()
cat = Cat('brown', size='medium', eye_color='blue', breed='munchkin')
cat.sound()
cat.sleep()
cat.play()
cat.wake_up()