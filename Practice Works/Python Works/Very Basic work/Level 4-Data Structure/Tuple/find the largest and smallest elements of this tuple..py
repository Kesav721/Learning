#Q (1,2,3....10).find the largest and smallest elements of this tuple.

t2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
largest = t2[0]
smallest = t2[0]


for i in t2:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest element:", largest)
print("Smallest element:", smallest)


