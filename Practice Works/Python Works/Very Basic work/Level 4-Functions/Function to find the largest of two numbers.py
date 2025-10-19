#Q Function to find the largest of two numbers

def largest(a,b):
    if a>b:
        return a
    else:
        return b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Largest number is:", largest(x, y))
