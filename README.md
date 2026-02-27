# PyKan

## Overview

PyKan is a Command Line Interface (CLI) based Kanban board built in Python.
It allows users to manage software projects by tracking tasks, priorities, and statuses across multiple boards.
The tool provides a clear overview of project progress and simplifies task management directly from the terminal.

![intro](https://github.com/amanamitabh/cli-kanbanboard/assets/101924129/4933c095-4e68-47eb-adf9-aa2621832b21)

## Features
- Clean, color-coded tables powered by the [rich](https://github.com/Textualize/rich) Python module.
- Secure data storage using Google Cloud SQL (MySQL).
- Support for multiple boards.
- Task sorting based on priority.
- Add, modify, remove and display tasks using CLI commands.

## Setup

### 1. Clone the repository
```
git clone https://github.com/amanamitabh/cli-kanbanboard
cd cli-kanbanboard
```

### 2. Install the required dependencies
```
pip install -r requirements.txt
```

### 3. Set up the environment variables

Create a `.env` file in the root directory of the project and add the following environment variables with your database credentials

```
DB_HOST= <YOUR_SERVER_HOSTNAME>
DB_DBNAME= <YOUR_DATABASE_NAME>
DB_USER= <YOUR_USERNAME>
DB_PASSWORD= <YOUR_PASSWORD>
```

Ensure the MySQL database is configured properly before running the application

## Architecture and Implementation

The application was developed using Python with MySQL as the backend database.

### Database Layer
- MySQL database hosted on Google Cloud SQL
- Tables defined using SQL queries
- CRUD operations implemented using `mysql-connector`

### CLI Layer
- Command-line argument parsing implemented using `argparse`
- Output formatting and table rendering handle using `rich`

## Usage

After setting up the environment and database, you can use the following commands to manage your Kanban boards and tasks.

![help](https://github.com/amanamitabh/cli-kanbanboard/assets/101924129/ffabaf3d-bd78-4e14-b3e4-d2734c96f2b7)

### Help
```
python main.py -h
```
```
python main.py --help
```

### Adding New Task

```
python main.py <boardname> -a <taskname> <category> <status> <priority> <assignees> <reportees>
```
```
python main.py <boardname> --addtask <taskname> <category> <status> <priority> <assignees> <reportees>
```

### Modifying Task Status

```
python main.py <boardname> -m <taskname> <new_status>
```
```
python main.py <boardname> --modifytask <taskname> <new_status>
```

### Removing a Task

```
python main.py <boardname> -r <taskname>
```
```
python main.py <boardname> --removetask <taskname>
```

### Displaying Tasks for a Specific Board

```
python main.py <boardname> -d
```
```
python main.py <boardname> --displaytasks
```

### Sorting by Priority

```
python main.py <boardname> -p <asc/desc>
```
```
python main.py <boardname> --prioritysorted <asc/desc>
```

### Display Version

```
python main.py -v
```
```
python main.py --version
```