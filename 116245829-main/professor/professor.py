import random


def main():
    lvl=get_level()
    q=10
    s=0
    z=3
    while q!=0:
        if z==3:
            x,y=generate_integer(lvl)
        try:
            r=x+y
            check=int(input(f"{x} + {y} = "))
            if check == r:
                s+=1
                q-=1
                z=3
                continue
            else:
                print("EEE")
                raise ValueError
        except(ValueError, NameError):
            z-=1
            pass
        if z == 0:
            print(x,"+",y,"=",r)
            z=3
            q-=1
    print("Score:",s)


def get_level():
    while True:
        try:
            l=int(input("Level: "))
            if l>=1 and l<=3:
                return l
        except:
            pass

def generate_integer(level):
    if level ==1:
        f=random.randint(0,9)
        s=random.randint(0,9)
    elif level ==2:
        f=random.randint(10,99)
        s=random.randint(10,99)
    elif level ==3:
        f=random.randint(100,999)
        s=random.randint(100,999)
    return f,s


if __name__ == "__main__":
    main()
