from argparse import ArgumentParser
from qry_funcs import *

parser = ArgumentParser()   # Creating parser object
query_grp = parser.add_mutually_exclusive_group()

parser.add_argument("board_arg", help="Name of Kanban Board")
parser.add_argument("task_arg", help="Name of the task")
query_grp.add_argument("-d", "--displaytasks", action="store_true", help="Displays all tasks for a specified Kanban Board")
query_grp.add_argument("-a", "--addtask", action="store_true", help="Adds task to a specified Kanban Board")
query_grp.add_argument("-m", "--modifytask", action="store_true", help="Modify the status of a task in a specified Kanban Board")
query_grp.add_argument("-r", "--removetask", action="store_true", help="Deletes task from a specified taskname in specified Kanban Board")

args = parser.parse_args()

if args.displaytasks:
    pass

elif args.addtask:
    pass

elif args.removetask:
    pass

elif args.modifytask:
    pass


