import mysql.connector
import sys

class dbhelper:

    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host="localhost",user="root",password="",database='test-db')
            self.mycursor = self.conn.cursor()
        except:
            print("Oh NO! , Some error occured.")
            sys.exit(0)
        else:
            print("Connection Succesfull")

    def register(self,name,address,password):
        try:
            self.mycursor.execute("""
INSERT INTO main-record ('id' , 'Name' , 'Address' , 'Password') VALUES (NULL , '{}', '{}', '{}')
""".format(name , address, password))
            self.conn.commit()

        except:
            return -1
        else:
            return 1
