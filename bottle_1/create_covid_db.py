import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
#conn.execute("CREATE TABLE covid (id INTEGER PRIMARY KEY, symtoms char(100) NOT NULL)")
conn.execute("INSERT INTO covid (symtoms) VALUES ('Fever')")
conn.commit()