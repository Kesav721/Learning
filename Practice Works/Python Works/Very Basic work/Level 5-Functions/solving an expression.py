#Q Solve a/b*c using lambda

expr=lambda a,b,c : (a/b)*c

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
print("Result is:", expr(a, b, c))
