#Q Write a program to find the count of both even and odd numbers between 1 to 50


even_count=0
odd_count=0

for i in range(1,51):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)
