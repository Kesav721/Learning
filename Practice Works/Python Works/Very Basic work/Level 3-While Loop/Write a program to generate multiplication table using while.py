#Q Write a program to generate multiplication table using while


number=int(input('Enter the number:'))
limit=int(input('Enter the limit:'))
i=1
product=1
while i<=limit:
    product=number*i
    print(f'{number}*{i} ={product}')
    i+=1

