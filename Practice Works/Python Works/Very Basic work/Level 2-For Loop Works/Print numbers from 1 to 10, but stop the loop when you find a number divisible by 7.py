#Q Print numbers from 1 to 10, but stop the loop when you find a number divisible by 7


for i in range(1, 11):
    if i % 7 == 0:
        break
    print(i)
