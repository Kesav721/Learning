#Q Count every letter except space (without len())


user_str = input("Enter a string: ")
count = 0
for ch in user_str:
    if ch != " ":
        count += 1
print("Count without spaces:", count)
