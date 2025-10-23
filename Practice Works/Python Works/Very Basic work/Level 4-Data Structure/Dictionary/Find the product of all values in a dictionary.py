#Q Find the product of all values in a dictionary

marks = {"Math": 90, "Science": 85, "English": 88}
product = 1
for val in marks.values():
    product *= val
print(product)
