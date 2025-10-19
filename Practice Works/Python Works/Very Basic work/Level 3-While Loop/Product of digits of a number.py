#Q Product of digits of a number

num=int(input('Enter a number:'))
product=1
n=num

while n!=0:
    last_digit= n%10
    product *= last_digit
    n//=10

print(f"Product of digits of {num} is {product}")
