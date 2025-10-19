#Q Write a program to find the count of digits in a number

num= int(input('Enter a number :'))
count=0
n=num
while n!=0:
     n //= 10
     count += 1
print(f"Number of digits in {num} is {count}")
    
         
