import sqlite3

conn = sqlite3.connect('survey.db')
cur = conn.cursor()

#this command is to delete a response
#cur.execute("DELETE FROM responses;")
cur.execute('''
CREATE TABLE IF NOT EXISTS responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    facility TEXT,
    rating INTEGER,
    comment TEXT
)
''')


conn.commit()
conn.close()
