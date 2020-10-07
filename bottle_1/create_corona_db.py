import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE corona (id INTEGER PRIMARY KEY, symtoms char(100) NOT NULL, severity bool NOT NULL)")
conn.execute("INSERT INTO corona (symtoms,severity) VALUES ('cough',1)")
conn.commit()