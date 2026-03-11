import sqlite3
from datetime import datetime, timedelta

def setup_database():
    """Builds the database schema (Two Tables)"""
    conn = sqlite3.connect('business_manager.db')
    cursor = conn.cursor()

    # Create Project Table (Parent)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            budget REAL
        )
    ''')

    # Create Tasks Table (Child with Date column)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            deadline DATE,
            priority INTEGER,
            project_id INTEGER,
            FOREIGN KEY (project_id) REFERENCES projects(id)
        )
    ''')
    conn.commit()
    conn.close()

def add_sample_data():
    """CRUD: Demonstrate INSERT"""
    conn = sqlite3.connect('business_manager.db')
    cursor = conn.cursor()
    
    # Check if data exists to avoid duplicates
    cursor.execute("SELECT COUNT(*) FROM projects")
    if cursor.fetchone()[0] == 0:
        # Insert Projects
        cursor.execute("INSERT INTO projects (name, budget) VALUES (?, ?)", ("Website Redesign", 5000))
        cursor.execute("INSERT INTO projects (name, budget) VALUES (?, ?)", ("Mobile App", 8000))
        
        # Insert Tasks with different dates
        today = datetime.now()
        tasks = [
            ('Write CSS', (today + timedelta(days=2)).strftime('%Y-%m-%d'), 5, 1),
            ('Database Setup', (today + timedelta(days=5)).strftime('%Y-%m-%d'), 4, 1),
            ('UI Mockups', (today + timedelta(days=12)).strftime('%Y-%m-%d'), 3, 2)
        ]
        cursor.executemany("INSERT INTO tasks (description, deadline, priority, project_id) VALUES (?, ?, ?, ?)", tasks)
        conn.commit()
    conn.close()

def run_reports():
    """Demonstrates JOIN, AGGREGATES, and DATE FILTERING"""
    conn = sqlite3.connect('business_manager.db')
    cursor = conn.cursor()

    print("\n--- REPORT 1: JOIN & AGGREGATES (Tasks per Project) ---")
    # Using JOIN, COUNT, and AVG
    query1 = """
        SELECT p.name, COUNT(t.id), AVG(t.priority)
        FROM projects p
        LEFT JOIN tasks t ON p.id = t.project_id
        GROUP BY p.name
    """
    cursor.execute(query1)
    for row in cursor.fetchall():
        print(f"Project: {row[0]} | Tasks: {row[1]} | Avg Priority: {row[2] if row[2] else 0:.1f}")

    print("\n--- REPORT 2: DATE RANGE FILTER (Due in next 7 days) ---")
    # Using DATE filtering with BETWEEN
    today = datetime.now().strftime('%Y-%m-%d')
    next_week = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    
    query2 = "SELECT description, deadline FROM tasks WHERE deadline BETWEEN ? AND ?"
    cursor.execute(query2, (today, next_week))
    
    results = cursor.fetchall()
    if not results:
        print("No urgent tasks!")
    for row in results:
        print(f"URGENT: {row[0]} is due on {row[1]}")

    conn.close()

def modify_data():
    """CRUD: Demonstrate UPDATE and DELETE"""
    conn = sqlite3.connect('business_manager.db')
    cursor = conn.cursor()
    
    # Update
    cursor.execute("UPDATE projects SET budget = budget + 500 WHERE name = ?", ("Website Redesign",))
    
    # Delete (Example: removing a specific task)
    cursor.execute("DELETE FROM tasks WHERE description = ?", ("UI Mockups",))
    
    conn.commit()
    print("\n[System] Database modified: Budget updated, UI Mockups task deleted.")
    conn.close()

if __name__ == "__main__":
    setup_database()
    add_sample_data()
    print("Welcome to the SQL Manager Software")
    run_reports()
    modify_data()
    # Run reports again to show changes
    run_reports()
