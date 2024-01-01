#check if number is even
def is_even(number):
    return number % 2 == 0

if __name__ =="__main__":
    num=input("Enter Number")
    if is_even(num):
        print("Number Is Even")
    else:
        print("Number Is Odd")

