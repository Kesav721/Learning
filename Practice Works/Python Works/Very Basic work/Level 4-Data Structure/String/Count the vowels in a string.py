#Q Count the vowels in a string

vowels='aeiouAEIOU'

Sentence=input("Enter the string :")
count=0

for ch in Sentence:
    if ch in vowels:
      count +=1

print("The number of vowels are :",count)
