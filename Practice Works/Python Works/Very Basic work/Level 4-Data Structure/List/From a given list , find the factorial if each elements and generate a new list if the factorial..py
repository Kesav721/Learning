#Q From a given list [5,6,7] find the factorial if each elements and generate a new list if the factorial.expected output :[120,720,5040].


List=[5,6,7]
new_list=[]

for i in List:
    product=1
    n=i
    while n>0:
        product=product*n
        n-=1
    new_list.append(product)

print(new_list)
