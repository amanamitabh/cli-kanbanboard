class Task:
    def __init__(self, taskname, category, status, assignees, reporters):
        self.__taskname = taskname
        self.__category = category
        self.__status = status
        self.__assignees = assignees
        self.__reporters = reporters
    
    def getData(self):
        print(f"{self.__taskname}, {self.__category}, {self.__status}, {self.__assignees}, {self.__reporters}")

t1 = Task("Stop Aryan from Watching TV", "Marketing", "To-Do", ["Aditya N Menon"], ["Aman Amitabh"])
t1.getData()
