import sqlite3

conn = sqlite3.connect("resume_history.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    resume_score INTEGER,
    ats_score INTEGER,
    role TEXT
)
""")

conn.commit()

def save_data(filename, resume_score, ats_score, role):
    c.execute(
        "INSERT INTO history (filename, resume_score, ats_score, role) VALUES (?, ?, ?, ?)",
        (filename, resume_score, ats_score, role)
    )
    conn.commit()

def view_data():
    c.execute("SELECT * FROM history")
    return c.fetchall()