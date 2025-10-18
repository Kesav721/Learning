#Q Write a program to find the count of even numbers bw 1050 and 1200


n=0
for i in range(1050,1201):
    if i%2==0:
        n+=1

print('the count of even numbers bw 1050 and 1200 :',n)
