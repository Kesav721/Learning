#Q Create two empty lists,name=[ ] and age=[ ] .insert names and ages of 3 people into the lists input by the user.



name = []
age = []
for i in range(3):
    n = input("Enter name: ")
    a = int(input("Enter age: "))
    name.append(n)
    age.append(a)
print("name =", name)
print("age =", age)
