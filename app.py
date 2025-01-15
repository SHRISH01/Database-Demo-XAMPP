import sys
from dbhelper import dbhelper

class app:
    def __init__(self):
        # Connection to the database
        self.db = dbhelper()
        self.menu()

    def menu(self):
        user_input = input("""
                               1. Enter 1 to Register
                               2. Enter 2 to Login
                               3. Enter Any other Num to Quit the Application
                               """)
        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(420)  # Exit with custom code

    def register(self):
        # Implement user registration logic here
        # Prompt for details like username, password
        # Store them in the database using self.db
        name = input("Enter the Name.")
        address = input("Enter the Address Details Here.")
        password = input("Enter the Password.")

        response = self.db.register(name, address, password)

        if response == 1:  # Registration successful
            print("Registration Successful")
            self.menu()
        else:
            print("Registration Failed. Please try again.")
            self.menu()  # Return to menu for retry

    def login(self):
        id = input("ENTER YOUR ASSOCIATED ID")
        password = input("Enter your Login Password")

        # Fix the error: use authenticate instead of search
        authenticated = self.db.authenticate(id, password)

        if authenticated:
            print("Login Successful!")
            # Implement actions after successful login (e.g., display user profile)
            # ...
        else:
            print("Login Failed. Please check your credentials and try again.")
            self.menu()  # Return to menu for retry

obj = app()