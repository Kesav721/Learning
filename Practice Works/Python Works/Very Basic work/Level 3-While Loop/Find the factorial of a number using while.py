#Q Find the factorial of a number using while

num = int(input("Enter a number: "))
i = 1
factorial = 1
while i <= num:
    factorial *= i
    i += 1
print(f"Factorial of {num} is {factorial}")
