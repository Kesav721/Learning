def Calculator():
    print("Simple Calculator")

    num1=int(input("Enter the first number"))
    num2=int(input("Enter the Second number"))

    Operation=input("Enter Operation: ")

    if Operation== "+":
        result=num1+num2
    elif Operation =="-":
        result=num1-num2
    elif Operation =="*":
        result=num1*num2
    elif Operation =="/":
         if num2!=0:
             result=num1/num2
         else:
             print("Division by zero is not allowed")
    else :
        print("the operation is invalid")
    return print(f"Result:{num1}{Operation}{num2}={int(result)}")
Calculator()
