#Q Create a class Person with a constructor (init) that initializes name and age.Create two objects with different details and print them

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


p1 = Person("Ravi", 25)
p2 = Person("Meera", 30)

p1.display()
p2.display()
