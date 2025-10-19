#Q Take 3 strings and find the largest (by length)


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s3 = input("Enter third string: ")

largest = s1
if len(s2) > len(largest):
    largest = s2
if len(s3) > len(largest):
    largest = s3

print("Largest string (by length):", largest)
