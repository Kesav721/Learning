#Q Sum of digits of a number

num = int(input("Enter a number : "))
sum_digits = 0
n = num
while n != 0:
    last_digit=n % 10
    sum_digits += last_digit
    n //= 10
print(f"Sum of digits of {num} is {sum_digits}")
