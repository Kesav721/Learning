#Q Create a class named Student with attributes name and age. Create two objects and print their details.


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")



student1=Student("Eren Yeager",20)
student2=Student("Levi Ackerman",30)

student1.show_details()
student2.show_details()
