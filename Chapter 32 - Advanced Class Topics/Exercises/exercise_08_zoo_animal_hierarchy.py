class Animal:
    def replay(self):                   # Back to subclass
        self.speak()

    def speak(self):                    # Custom message
        print('spam')


class Mammal(Animal):
    def speak(self):
        print('huh?')

class Cat(Mammal):
    def speak(self):
        print('meow')

class Dog(Mammal):
    def speak(self):
        print('bark')

class Primate(Mammal):
    def speak(self):
        print('Hello world!')

class Hacker(Primate):
    pass

if __name__ == '__main__':
    spot = Cat()
    spot.replay()                   # Animal.reply: calls Cat.speak

    data = Hacker()                 # Animal.reply: calls Primate.speak
    data.replay()
