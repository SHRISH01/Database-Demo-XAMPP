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

