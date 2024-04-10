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

def getKanbanBoard():
    qry = "SELECT * FROM tasks;"
    cur_obj.execute(qry)
    data = cur_obj.fetchall()
    return data


def getTask(taskname):
    qry = "SELECT * FROM tasks WHERE taskname = %s;"
    cur_obj.execute(qry, [taskname])
    data = cur_obj.fetchall()
    return data


def addTask(taskname, category, status, priority, assignees, reportees):
    qry = "INSERT INTO tasks VALUES(%s, %s, %s, %s, %s, %s);"
    vals = [taskname, category, status, priority, assignees, reportees]
    cur_obj.execute(qry, vals)
    con_obj.commit()


def removeTask(taskname):
    rem_data = getTask(taskname)
    print("Are you sure this is the task you want to remove : ")
    for i in rem_data:
        print(i)

    confirm = input("Enter 'Y' if you want to proceed : ")
    if confirm == "Y":
        vals = [taskname]
        qry = "DELETE FROM tasks WHERE taskname = %s;"
        cur_obj.execute(qry, vals)
        con_obj.commit()


table_data = getKanbanBoard()
for i in table_data:
    print(i)

con_obj.close()
print("Connection Closed")
