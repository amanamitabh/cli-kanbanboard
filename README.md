# Kanban?

## Introduction

A Kanban Board is a visual project management tool to track status and priorities of various subtasks to be completed in a software project. It gives an overview of the current project status and simplifies team communication. This project aims to implement a command line interface based Kanban Board. Kanban? is a CLI based Kanban Board written in Python.

![intro](https://github.com/amanamitabh/cli-kanbanboard/assets/101924129/4933c095-4e68-47eb-adf9-aa2621832b21)

## Features
- Colourful and eye catching tables using the [rich](https://rich.readthedocs.io/en/stable/index.html) module in python.
- Secure data storage using Google Cloud SQL Database.
- Support for multiple projects across different boards.
- Sorting by Task priority.

## Setup

The prerequisites to run the python script can be found in the requirements.txt file and can be installed using 
'''
pip install -r requirements.txt
'''

The next step requires you to create a .env file in the same directory as the rest of the scripts. Paste the below code into the empty .env file:
'''
DB_HOST= <YOUR_SERVER_HOSTNAME>
DB_DBNAME= <YOUR_DATABASE_NAME>
DB_USER= <YOUR_USERNAME>
DB_PASSWORD= <YOUR_PASSWORD>
'''

## Usage

After following the steps in the setup part of the README.md, you are ready to use Kanban?.

### No Shame in Seeking Help

![help](https://github.com/amanamitabh/cli-kanbanboard/assets/101924129/ffabaf3d-bd78-4e14-b3e4-d2734c96f2b7)

'''
python main.py -h
'''
OR
'''
python main.py --help
'''

### Adding New Task

'''
python main.py <boardname> -a <taskname> <category> <status> <priority> <assignees> <reportees>
'''
OR
'''
python main.py <boardname> --addtask <taskname> <category> <status> <priority> <assignees> <reportees>
'''

### Modifying Task Status

'''
python main.py <boardname> -m <taskname> <new_status>
'''
OR
'''
python main.py <boardname> --modifytask <taskname> <new_status>
'''

### Removing a Task

'''
python main.py <boardname> -r <taskname>
'''
OR
'''
python main.py <boardname> --removetask <taskname>
'''

### Displaying Tasks for a Specific Board

'''
python main.py <boardname> -d
'''
OR
'''
python main.py <boardname> --displaytasks
'''

### Sorting by Priority

'''
python main.py <boardname> -p <asc/desc>
'''
OR
'''
python main.py <boardname> --prioritysorted <asc/desc>
'''

### Display Version

'''
python main.py -v
'''
OR
'''
python main.py --version
'''
