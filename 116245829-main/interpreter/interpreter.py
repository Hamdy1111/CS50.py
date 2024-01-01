expr=input("Expression: ")
x, y, z=expr.split(" ")
x=float(x)
z=float(z)
if y =='+':
    print(x+z)
elif y == '-':
    print(x-z)
elif y == '*':
    print(x*z)
elif y == '/':
    print(x/z)
