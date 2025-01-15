import mysql.connector
import sys

class dbhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database='test-db')
            self.mycursor = self.conn.cursor()
            print("Connection Successful")
        except Exception as e: 
            print(f"Error connecting to database: {e}")
            sys.exit(0)

    def register(self, name, address, password):
        try:
            sql = """
            INSERT INTO main-record (id, Name, Address, Password) 
            VALUES (NULL, %s, %s, %s)
            """
            self.mycursor.execute(sql, (name, address, password))
            self.conn.commit()
            return 1 
        except Exception as e:
            print(f"Error during registration: {e}")
            return -1

    def authenticate(self, id, password):
        try:
            sql = """
            SELECT * FROM `main-record` WHERE id = %s AND Password = %s
            """
            self.mycursor.execute(sql, (id, password)) 
            data = self.mycursor.fetchall()
            if data:
                return data  # Login successful
            else:
                return False  # Login failed
        except Exception as e:
            print(f"Error during login: {e}")
            return False

"""

# Example usage

if __name__ == "__main__":
    db = dbhelper()
    
    # Register a new user
    result = db.register("John Doe", "123 Main St", "secret")
    if result == 1:
        print("Registration successful")
    else:
        print("Registration failed")
    
    # Login with credentials
    result = db.login("John Doe", "secret") 
    if result == 1:
        print("Login successful")
    else:
        print("Login failed")

"""