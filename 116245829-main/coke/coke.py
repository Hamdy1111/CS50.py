check=50

while check>0:
    print("Amount Due:",check)
    insert=int(input("Insert Coin: "))
    if insert==25 or insert==10 or insert==5:
        check =check-insert
       # print("Amount Due:",check)
if check<=0:
    check=check*-1
    print("Change Owed:",check)
