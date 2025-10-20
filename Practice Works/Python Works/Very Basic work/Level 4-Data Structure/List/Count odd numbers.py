#Q Count odd numbers

L = [-2, -7, -8, 1, 2, 4]
count = 0
for i in L:
    if i % 2 != 0:
        count += 1
print("Count of odd numbers:", count)
