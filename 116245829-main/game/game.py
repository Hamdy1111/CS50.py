import random
import sys

while True:
    try:
        level = int(input("Level: "))
        num = random.randint(1, level)
        while True:
            check = input("Guess: ")
            if int(check) > num:
                print("Too large!")
            elif int(check) < num:
                print("Too small!")
            elif int(check) == num:
                sys.exit("Just right!")
    except ValueError:
        pass
    except EOFError:
        break
