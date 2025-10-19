#Q Find largest of two numbers using lambda

largest = lambda a, b: a if a > b else b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Largest number is:", largest(x, y))
