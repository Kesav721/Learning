#Q Write a program to find the square of each element in the given list [1,2,3,4] and generate a new list contains the squares.

Li=[1,2,3,4]

new_Li=[]

for i in Li:
    x=i*i
    new_Li.append(x)

print(new_Li)
