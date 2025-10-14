num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1>num2:
    if num3>num1:
        print(f"{num3},third number is largest")
    elif num1>num3:
        print(f"{num1},first number is largest")
    else:
        print("undefined")

elif num2>num1:
     if num3>num2:
        print(f"{num3},third number is largest")
     elif num2>num3:
        print(f"{num2},second number is largest")
     else:
        print("undefined")

else:
    print("undefined")
