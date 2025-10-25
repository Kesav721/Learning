#Q Write a program to create a class Employee with attributes name and salary. Add a method to display the employee details

class Employee:
    def __init__(self,name,salary):
        self.name =name
        self.salary=salary

    def display(self):
        print(f"The name of the employee is {self.name}")
        print(f"The Salary of the employee is {self.salary}")



emp1= Employee("Walter White", 50000)
emp1.display()
