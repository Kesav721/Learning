#Q Count uppercase and lowercase letters

sentence=input("Enter your sentence :")

upper=0
lower=0

for ch in sentence:
    if ch.isupper():
        upper+=1
    else:
        ch.islower()
        lower+=1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
