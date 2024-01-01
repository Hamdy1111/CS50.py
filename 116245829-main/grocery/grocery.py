d={}
while True:
    try:
        item = input().strip().upper()
        if item in d:
            d[item]+=1
        else:
            d[item]=1
    except EOFError:
        for x in sorted(list(d)):
            print(d[x],x)
        break

'''
sortedkeys=sorted(d.keys())
sortedlist={key:d[key] for key in sortedkeys}
for x in sortedlist :
        print(sortedlist[x],x)

l=[]
l=d
l=sorted(l)
for x in l:
    print(l[x],x)


    else:
         if item in d:
            d[item]+=1
         else:
            d[item]=1


'''
'''
    except EOFError:
        for x in d:
            print(d[x],x)
        break

'''
'''
        for x in sorted(d.x()):
            print(d[x],x)
'''
