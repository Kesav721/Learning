#Q Given tuple, count how many times 2 appears

t = (1, 2, 3, 2, 4, 2, 5)
count_2 = 0
for i in t:
    if i == 2:
        count_2 += 1
print("Number of times 2 appears:", count_2)
