import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


if len(sys.argv)<1:
    f=input("Input: ")
    fonts=random.choice(figlet.getFonts())
    figlet.setFont(font=fonts)
    print("Output:")
    print(figlet.renderText(f))
elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font") and sys.argv[2] in figlet.getFonts() :
    f=input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print("Output: ")
    print(figlet.renderText(f))

else:
    sys.exit("Invalid usage")
