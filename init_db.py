import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert a test user (username: test, password: test123)
try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('test', 'test123'))
    print("Test user created.")
except sqlite3.IntegrityError:
    print("Test user already exists.")

conn.commit()
conn.close()
