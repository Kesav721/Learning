#Q Count both even and odd numbers bw the range 100 and 300

i=100
even_count=0
odd_count=0

while i<=300:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

    i+=1

print('The count of odd number is :',odd_count)
print('The count of even number is :',even_count)

