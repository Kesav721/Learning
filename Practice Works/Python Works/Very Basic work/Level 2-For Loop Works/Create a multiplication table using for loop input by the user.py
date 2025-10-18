#Q Create a multiplication table using for loop input by the user


number=(int(input('Enter the number:')))
x=(int(input('Enter the limit:')))

        
for i in range(1,x+1):
        product=number*i
        print(f'{number} x {i} ={product}')
