import sys

def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        print(Lines_Code(sys.argv[1]))

def Lines_Code(file):
    try:
        lines=0
        with open(file,"r") as code_file:
            for line in code_file :
                if not(line.rstrip()=="" or line.lstrip()[0]=="#"):
                    lines+=1
            return lines

    except (FileNotFoundError):
        return "File does not exist"


if __name__=="__main__":
    main()
