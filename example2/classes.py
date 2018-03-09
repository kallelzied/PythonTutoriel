class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


class Bird(Animal):
    def talk(self):
        return "?¿?¿?¿?¿?¿"


animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie'),
           Bird("Tweet")]

for animal in animals:
    print(animal.name + ': ' + animal.talk())
