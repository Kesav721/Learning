#Q Check if a number is positive or negative using lambda

check_sign=lambda x:"Positive" if x>0 else("Zero" if x==0 else "Negative")


n = int(input("Enter a number: "))
print("The number is:", check_sign(n))
