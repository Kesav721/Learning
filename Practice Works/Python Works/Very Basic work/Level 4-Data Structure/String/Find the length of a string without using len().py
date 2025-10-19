#Q Find the length of a string without using len()

user_str = input("Enter a string: ")
count = 0
for i in user_str:
    count += 1
print("Length of string:", count)
