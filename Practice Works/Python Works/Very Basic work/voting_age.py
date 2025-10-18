#Q write a program to check a person is eligible for voting based on the age input by the user

age = int(input("Enter your age: "))

if age > 18:
    print("You can Vote")
else:
    print("You cannot vote")
