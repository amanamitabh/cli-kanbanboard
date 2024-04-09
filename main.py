import os
from dotenv import load_dotenv
import mysql.connector as mysql

load_dotenv()
DB_HOSTNAME = os.getenv('DB_HOST')
DB_USERNAME = os.getenv('DB_USER')
DB_PASSWD = os.getenv('DB_PASSWORD')
DB_DATABASENAME = os.getenv('DB_DBNAME')

con_obj = mysql.connect(host=DB_HOSTNAME, user=DB_USERNAME, password=DB_PASSWD, database=DB_DATABASENAME)
cur_obj = con_obj.cursor()
print("Connection Established")
'''
class Task:
    def __init__(self, taskname, category, status, priority, assignees, reporters):
        self.__taskname = taskname
        self.__category = category
        self.__status = status
        self.priority = priority
        self.__assignees = assignees
        self.__reporters = reporters

def getData(self):
        print(f"{self.__taskname}, {self.__category}, {self.__status}, {self.__assignees}, {self.__reporters}")
'''

con_obj.close()
print("Connection Closed")
