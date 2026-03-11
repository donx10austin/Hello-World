# SQL Relational Database Project: Business Task Manager

## Overview
This software is a relational database management tool designed to track projects and their associated tasks. It demonstrates the ability to bridge a high-level programming language (Python) with a relational database (SQLite) to perform complex data manipulation and reporting.

The primary goal of this project was to move beyond flat-file storage and implement a normalized database structure that enforces data integrity through foreign keys and relational joins.



## Web Demo Video
[Link to your 4-5 minute demo video goes here]

## Relational Database Schema
The database consists of two tables with a **One-to-Many** relationship:

1.  **Projects Table**: Stores high-level project information.
    * `id`: Primary Key (Integer)
    * `name`: The title of the project (Text)
    * `budget`: Financial allocation (Real)
2.  **Tasks Table**: Stores individual actions linked to a project.
    * `id`: Primary Key (Integer)
    * `description`: Task details (Text)
    * `deadline`: Target completion date (Date)
    * `priority`: Urgency level 1-5 (Integer)
    * `project_id`: Foreign Key linking to the Projects table.

## Software Functionality
The software demonstrates full CRUD capability and advanced querying:

* **Create**: Automatically seeds the database with projects and tasks if they do not exist.
* **Read (Relational Join)**: Combines the `projects` and `tasks` tables to display which tasks belong to which project.
* **Read (Aggregate Functions)**: Uses `COUNT()` to total tasks per project and `AVG()` to calculate the average priority of a project's workload.
* **Read (Date Filtering)**: Uses a `BETWEEN` clause to filter and display only tasks due within the next 7 days.
* **Update**: Modifies project budgets dynamically through the software logic.
* **Delete**: Removes specific records from the database to demonstrate data cleanup.

## Development Environment
* **Language**: Python 3.x
* **Database**: SQLite3
* **Tools**: Visual Studio Code, SQLTools Extension, SQLite Viewer

## Useful Websites
* [SQLite Documentation](https://www.sqlite.org/docs.html)
* [Python sqlite3 Module Guide](https://docs.python.org/3/library/sqlite3.html)
* [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)

## Future Work
* Add a User table to assign specific team members to tasks (Many-to-Many relationship).
* Implement a Graphical User Interface (GUI) using Tkinter or PyQt.
* Add "Cascade Delete" functionality so that deleting a project automatically removes all its tasks.