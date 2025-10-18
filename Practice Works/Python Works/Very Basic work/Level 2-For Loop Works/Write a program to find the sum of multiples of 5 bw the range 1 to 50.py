#Q Write a program to find the sum of multiples of 5 between the range 1 to 50

sum=0
for i in range(1,51):
    if i%5==0:
        sum=sum+i

print('The sum is :',sum)
