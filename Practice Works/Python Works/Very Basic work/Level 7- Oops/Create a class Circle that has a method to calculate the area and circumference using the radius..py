#Q Create a class Circle that has a method to calculate the area and circumference using the radius.

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        p=3.14
        return p* self.radius**2
    def circumference(self):
        p=3.14
        return 2*p*self.radius

circle1=Circle(5)
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())
