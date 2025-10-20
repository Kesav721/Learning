#Q Filter only even numbers

L = [1,2,3,4,5,6]
even=[]

for i in L:
    if i%2==0:
        even.append(i)

print(even)
