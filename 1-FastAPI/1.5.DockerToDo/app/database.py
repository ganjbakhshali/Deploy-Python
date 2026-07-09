import sqlite3

DB_NAME = "todo.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                time DATETIME NOT NULL,
                status TEXT NOT NULL
            )
        """)
        conn.commit()
        print("Table 'tasks' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

def add_task(title, description, time, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, time, status) VALUES (?, ?, ?, ?)",
        (title, description, time, status)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def update_task(id, title=None, description=None, time=None, status=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    if title is not None:
        cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (title, id))
    if description is not None:
        cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (description, id))
    if time is not None:
        cursor.execute("UPDATE tasks SET time = ? WHERE id = ?", (time, id))
    if status is not None:
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, id))

    conn.commit()
    conn.close()

def delete_task(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def read_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return [dict(task) for task in tasks]

def read_task_by_id(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    return dict(task) if task else None

if __name__ == "__main__":
    create_tables()
