import sys
import csv

def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")
    else:
        edit_name(sys.argv[1],sys.argv[2])

def edit_name(before,after):
    try:
        with open(before,"r") as file:
            read=csv.DictReader(file)
            with open(after,"w") as csvfile:
                write=csv.DictWriter(csvfile , fieldnames=["first","last","house"])
                write.writerow({"first":"first","last":"last","house":"house"})
                for student in read:
                    name=student["name"].split(", ")
                    write.writerow({"first":name[1],"last":name[0],"house":student["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__=="__main__":
    main()
