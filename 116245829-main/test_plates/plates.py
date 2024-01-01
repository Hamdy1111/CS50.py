def main():
    plate = input("Plate: ")
    plate=plate.lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for x in s:
        if x in['.',' ',',','!','?']:
            return False
    if len(s)>=2 and len(s)<=6:
        if s[:2].isalpha()==True :
            for c in s[2:]:
                if c.isdigit():
                    if int(c)!= 0 and s[s.index(c):].isdigit():
                        return True
                    else:
                        return False
            return True
        else:
            return False
    else:
        return False

if __name__=="__main__":
    main()
