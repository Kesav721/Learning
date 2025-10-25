#Q write a program to find whether a number is even or odd input by the user

num = float(input("Enter a number: "))

rem= num%2
if rem == 0:
    print("The number is even.")
else:
    print("The number is odd.")
