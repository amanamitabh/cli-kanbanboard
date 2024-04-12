from argparse import ArgumentParser
from qry_funcs import *

parser = ArgumentParser()   # Creating parser object
query_grp = parser.add_mutually_exclusive_group()

parser.add_argument("board_arg", 
                    help="Name of Kanban Board")

parser.add_argument("-v", "--version", action="version", version="KanBan? 1.0.0")
query_grp.add_argument("-p", "--prioritysorted", choices=["asc", "desc"], 
                       help="Displays tasks for a specified project sorted by priority")
query_grp.add_argument("-d", "--displaytasks",action="store_true", 
                       help="Displays tasks for a specified project.")
query_grp.add_argument("-a ", "--addtask", nargs=6, 
                       metavar=("taskname", "category", "status", "priority", "assignees", "reportees"),
                       help="Adds task to a specified Kanban Board.")
query_grp.add_argument("-m", "--modifytask", nargs=2, metavar=("taskname", "new_status"),
                       help="Modify the status of a task in a specified Kanban Board.")
query_grp.add_argument("-r", "--removetask", nargs=1, metavar = ("taskname"),
                       help="Deletes task from a specified taskname in specified Kanban Board.")

args = parser.parse_args()
if args.displaytasks:
    current_board = getKanbanBoard(args.board_arg)
    printData(current_board)

elif args.addtask:
    addTask(args.addtask[0], args.addtask[1], args.addtask[2], args.addtask[3], args.addtask[4], args.addtask[5], args.board_arg)

elif args.removetask:
    removeTask(args.removetask[0], args.board_arg)

elif args.modifytask:
    changeStatus(args.modifytask[0], args.modifytask[1], args.board_arg)

elif args.prioritysorted:
    getPrioritySorted(args.board_arg, args.prioritysorted)

closeConnection()