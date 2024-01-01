in_put=input("Input: ")

print("Output: ",end="")

for c in in_put:
    if c=='a' or c=='A':
        c=c.lower()
        c=c.replace('a','')
    elif c=='e' or c=='E':
        c=c.lower()
        c=c.replace('e','')
    elif c=='i' or c=='I':
        c=c.lower()
        c=c.replace('i','')
    elif c=='o' or c=='O':
        c=c.lower()
        c=c.replace('o','')
    elif c=='u' or c=='U':
        c=c.lower()
        c=c.replace('u','')
    print(c, end="")
print()
