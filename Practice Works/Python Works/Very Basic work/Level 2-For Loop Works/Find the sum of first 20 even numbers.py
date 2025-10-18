#Q Find the sum of first 20 even numbers

n=0
sum=0
for i in range(1,100):
    if i%2==0 and n<20:
        n+=1
        sum=sum+i
print(sum)
