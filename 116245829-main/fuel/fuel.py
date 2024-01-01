c=True
while c==True :
    try:
        check=input("Fraction: ").strip()
        f,s=check.split("/")
        x=int(f)/int(s)
        x=x*100
        x=round(x)
        if x>=0 and x<=100:
            if x==100 or x==99:
                print("F")
                c=False
            elif x==0 or x==1:
                print("E")
                c=False
            else:
                print(x,"%",sep='')
                c=False
    except (ValueError, ZeroDivisionError):
        pass
