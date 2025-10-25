#Q Create a class Parent with an attribute name and a method display().Create a class Child that inherits from Parent and displays both parent and child names.

class Parent:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("Parent Name",self.name)

class Child(Parent):
    def __init__(self,parent_name, child_name):
        super().__init__(parent_name)
        self.child_name = child_name

    def display(self):
        super().display()
        print("Child Name:", self.child_name)

# Creating object
c1 = Child("Ramesh", "Arun")
c1.display()
        
