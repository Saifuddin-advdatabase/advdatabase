import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE intro (id INTEGER PRIMARY KEY, symtoms char(100) NOT NULL)")
conn.execute("INSERT INTO intro (symtoms) VALUES ('Fever')")
conn.execute("INSERT INTO intro (symtoms) VALUES ('Chills')")
conn.execute("INSERT INTO intro (symtoms) VALUES ('Difficulty in breathing')")

conn.commit()


