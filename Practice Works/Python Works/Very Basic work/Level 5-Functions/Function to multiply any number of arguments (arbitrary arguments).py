#Q Function to multiply any number of arguments (arbitrary arguments)

def multiply_any(*num):
    result=1
    for n in num:
        result*= n
    return result

print("Product is:", multiply_any(2, 3, 4))
print("Product is:", multiply_any(5, 6))
print("Product is:", multiply_any(1, 2, 3, 4, 5))
