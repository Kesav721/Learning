#Q Function to check if a number is even or odd

def even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(n, "is", even_odd(n))
