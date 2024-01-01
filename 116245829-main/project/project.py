import sys
import csv
import re

def main():
    while True:
        username = input("username: ")
        if not check_username(username):
            while True:
                password = input("password: ")
                if check_password(password):
                    signUp(username, password)
                    #sys.exit("Sign Up Is Complete")
                else:
                    print("Password Is Not Valid\nAt least 8 characters\nAt least one uppercase letter\nAt least one lowercase letter\nAt least one digit\nAt least one special character (e.g., !@#$%^&*()-_+=)")
        else:
            sys.exit("The Username Already used ,Please Change The Username")

def check_username(name):

    with open("data.csv", "r", newline='') as file:
        reader = csv.DictReader(file)
        for line in reader:
            if line["username"] == name:
                return True
        return False

def check_password(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&_-]{8,}$')
    return bool(pattern.match(password))

def signUp(name, password):
    with open("data.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({'username': name, 'password': password})
        sys.exit("Sign Up Is Complete")

if __name__ == "__main__":
    main()

