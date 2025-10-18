#Q Print all numbers from 1 to 10 except multiples of 3

for i in range(1,10):
    if i%3==0:
        continue
    print(i)
