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
            sys.exit(420)

    def register(self):
        # Implement user registration logic here
        # Prompt for details like username, password
        # Store them in the database using self.db
        name = input("Enter the Name.")
        address = input("Enter the Address Details Here.")
        password = input("Enter the Password.")

        response=self.db.register(name,address,password)

        if response:
            print("Registration Successful")
            self.menu()

        else :
            sys.exit(0)


obj = app()
