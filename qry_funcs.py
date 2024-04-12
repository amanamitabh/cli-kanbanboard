import os
from dotenv import load_dotenv
import mysql.connector as mysql

# Environment Variable Management
load_dotenv()
DB_HOSTNAME = os.getenv('DB_HOST')
DB_USERNAME = os.getenv('DB_USER')
DB_PASSWD = os.getenv('DB_PASSWORD')
DB_DATABASENAME = os.getenv('DB_DBNAME')

# Establishing Connection and Cursor Object

try:
    con_obj = mysql.connect(host=DB_HOSTNAME, user=DB_USERNAME, password=DB_PASSWD, database=DB_DATABASENAME)
    cur_obj = con_obj.cursor()


except mysql.errors.ProgrammingError or mysql.errors.DatabaseError:
    print("Error: Could not access database. Verify connection object parameters.")
    quit()

def printData(fetched_data):
    if fetched_data == []:  # Checking whether data exists after fetching
        return 1
    for line in fetched_data:
        print(line)
        return 0


def confirmStatus():
    confirm = input("Enter 'Y' if you want to proceed : ")
    if confirm == "Y":
        return True
    else:
        return False


def getKanbanBoard(boardname):
    qry = "SELECT * FROM tasks where board = %s;"
    cur_obj.execute(qry, [boardname])
    data = cur_obj.fetchall()
    return data


def getTask(taskname, board):
    qry = "SELECT * FROM tasks WHERE taskname = %s and board = %s;"
    cur_obj.execute(qry, [taskname, board])
    data = cur_obj.fetchone()
    return data


def addTask(taskname, category, status, priority, assignees, reportees, board):
    try:
        qry = "INSERT INTO tasks VALUES(%s, %s, %s, %s, %s, %s, %s);"
        vals = [taskname, category, status, priority, assignees, reportees, board]
        cur_obj.execute(qry, vals)
        con_obj.commit()

    except mysql.errors.IntegrityError: # Prevents code crash when adding duplicate taskname
        print("The taskname already exists")
        

def removeTask(taskname, board):
    rem_data = getTask(taskname, board)
    if printData(rem_data) == 1:
        print("No Task Found")
        return
    print("Are you sure this is the task you want to remove? ")

    if confirmStatus():
        vals = [taskname, board]
        qry = "DELETE FROM tasks WHERE taskname = %s AND board = %s;"
        cur_obj.execute(qry, vals)
        con_obj.commit()


def changeStatus(taskname, new_status, board):
    upd_data = getTask(taskname, board)
    if printData(upd_data) == 1:
        print("No Task Found")
        return
    print("Are you sure this is the task whose status you want to change?")

    if confirmStatus():
        qry = "UPDATE tasks SET status = %s WHERE taskname = %s AND board = %s;"
        vals = [new_status, taskname, board]
        cur_obj.execute(qry, vals)
        con_obj.commit()


def closeConnection():
    con_obj.close()