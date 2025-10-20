#Q Largest element without using max()


L = [4, 8, 1, 9, 2]
largest = L[0]
for i in L:
    if i > largest:
        largest = i
print("Largest element:", largest)
