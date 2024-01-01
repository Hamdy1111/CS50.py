 # YOUR PROJECT TITLE
    #### Video Demo:  <https://youtu.be/pSGvoi6YGw8>
    #### sign up check program
This Python script implements a simple user registration and authentication system. Users are prompted to enter a username and password. The program checks the uniqueness of the username by consulting a CSV file ("data.csv") that stores user credentials. If the username is available, the program proceeds to validate the password against defined criteria. A successful registration updates the CSV file with the new user's credentials.

Functions:
main():
The main function orchestrates the user registration process.
Users are prompted for a username, and the script checks for its uniqueness using the check_username function.
If the username is unique, the script prompts for a password, checks its validity using check_password, and registers the user using signUp.
If the username is already taken, the program exits with a notification.
check_username(name):
Reads the "data.csv" file using a CSV reader.
Checks if the provided username already exists in the file.
Returns True if the username exists and False otherwise.
check_password(password):
Uses a regular expression to validate the password against specific criteria.
Criteria include at least 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character.
Returns True if the password is valid and False otherwise.
signUp(name, password):
Opens the "data.csv" file in append mode and writes the new username and password.
If the file is empty, writes the header first.
Exits the program with a completion message.
Testing:
The project includes a set of pytest tests (test_password, test_username_isfound, and test_signUp) to validate the functionality of the password and username checks. These tests cover scenarios such as valid and invalid passwords, existing and non-existing usernames.
How to Run:
Users can run the script directly. Upon execution, they will be prompted to enter a username and password. The script will guide them through the registration process and notify them of the outcome.
Dependencies:
The script utilizes the csv module for file handling and the re module for regular expressions. No additional external dependencies are required.
    TODO
