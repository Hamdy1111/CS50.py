from PIL import Image,ImageOps

from os.path import splitext

import sys


def main():
    check_argv()
    
    try:
        with Image.open(sys.argv[1]) as photo_Before :
            with Image.open("shirt.png") as shirt :
                image_size=shirt.size
                photo_after=ImageOps.fit(photo_Before,image_size)
                photo_after.paste(shirt , shirt)
                photo_after.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")



def check_argv():
    check_file=[".jpg",".jpeg",".png"]
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif splitext(sys.argv[1])[1] not in  check_file or splitext(sys.argv[2])[1] not in  check_file :
        sys.exit("Invalid output")
    elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
