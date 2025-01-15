import mysql.connector

class dbhelper:

    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host="localhost",username="root",password="",database='test-db')
            self.mycursor = self.conn.cursor()
        except:
            print("Connection Successfull")
        else:
            print("Oh NO! , Some error occured.")

