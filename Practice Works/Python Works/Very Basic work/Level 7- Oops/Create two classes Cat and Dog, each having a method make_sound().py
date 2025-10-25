#Q Create two classes Cat and Dog, each having a method make_sound().Write a common function that calls make_sound() for any object.

class Cat:
    def make_sound(self):
        print("Meow!")

class Dog:
    def make_sound(self):
        print("Woof!")

def animal_sound(animal):
    animal.make_sound()

c = Cat()
d = Dog()

animal_sound(c)
animal_sound(d)
