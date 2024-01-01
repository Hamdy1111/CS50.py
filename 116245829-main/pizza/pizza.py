import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        print(pizza_py(sys.argv[1]))

def pizza_py(file):
    try:
        with open(file) as f:
            menu=tabulate(csv.reader(f), headers="firstrow", tablefmt="grid")
            return menu

    except (FileNotFoundError):
        sys.exit("File does not exist")


if __name__=="__main__":
    main()
