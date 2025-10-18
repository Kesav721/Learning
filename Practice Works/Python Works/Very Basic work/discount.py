#Q write a program to calculate the discount of an amount input by the user

amount = float(input("Enter the amount: "))

if amount > 10000:
    new_amount=amount*0.9
    print("discounted amount=",new_amount)
elif 5000< amount < 10000:
    new_amount=amount*0.95
    print("discounted amount=",new_amount)
else:
    print("No discount.")
