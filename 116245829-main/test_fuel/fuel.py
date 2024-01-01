def main():
    c=True
    while c==True :
        check=input("Fraction: ").strip()
        try:
            percent=convert(check)
            print(gauge(percent))
            c=False
        except (ZeroDivisionError,ValueError):
            pass

def convert(fraction):

    codomin,domin=fraction.split("/")
    if int(domin) == 0:
        raise ZeroDivisionError
    elif int(codomin) > int(domin):
        raise ValueError
    else:
        x=int(codomin) / int(domin)
        x=x*100
        return round(x)

def gauge(percentage):
    if percentage==100 or percentage==99:
        return "F"
    elif percentage==0 or percentage==1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
