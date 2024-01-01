name=input("camelCase: ")

print("snake_case: ",end="")

for c in name:
    if c.isupper():
        print("_",c.lower(),sep="", end="")
    else:
        print(c, end="")
print("")
