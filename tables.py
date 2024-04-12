from rich.table import Table
from rich.console import Console

table1 = Table(title="TO DO", title_style="green", title_justify="left", show_lines=True)
table1.add_column("TASKNAME", header_style="red")
table1.add_column("CATEGORY", header_style="cyan")
table1.add_column("PRIORITY", header_style="magenta")
table1.add_column("ASSIGNEES", header_style="yellow")
table1.add_column("REPORTEES", header_style="blue")

table2 = Table(title="IN PROGRESS", title_style="green", title_justify="left", show_lines=True)
table2.add_column("TASKNAME", header_style="red")
table2.add_column("CATEGORY", header_style="cyan")
table2.add_column("PRIORITY", header_style="magenta")
table2.add_column("ASSIGNEES", header_style="yellow")
table2.add_column("REPORTEES", header_style="blue")

table3 = Table(title="DONE", title_style="green", title_justify="left", show_lines=True)
table3.add_column("TASKNAME", header_style="red")
table3.add_column("CATEGORY", header_style="cyan")
table3.add_column("PRIORITY", header_style="magenta")
table3.add_column("ASSIGNEES", header_style="yellow")
table3.add_column("REPORTEES", header_style="blue")

def tableFiller(data):
    for i in data:
        if i[2] == "To Do":
            table1.add_row(i[0], i[1], str(i[3]), i[4], i[5])

        elif i[2] == "In Progress":
            table2.add_row(i[0], i[1], str(i[3]), i[4], i[5])

        elif i[2] == "Done":
            table3.add_row(i[0], i[1], str(i[3]), i[4], i[5])

def tablePrinter():
    console = Console()
    console.print(table1)
    print("\n")
    console.print(table2)
    print("\n")
    console.print(table3)