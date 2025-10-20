#Q From a given list ["hai","hello","welcome"] find the reverse of each element and generate a new list.


words = ["hai", "hello", "welcome"]
rev_list=[]
for w in words:
    element=w[::-1]
    rev_list.append(element)

print(rev_list)
