#Q Check if a number is odd or even using lambda

odd_even= lambda x: "Even" if x%2==0 else "odd"

n = int(input("Enter a number: "))
print(n, "is", odd_even(n))
