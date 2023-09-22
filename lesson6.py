# база данных субд sql
# ветки , git pull
# sql - язык
# cубд - система управления базами данных

# mySQL,posgreSQL,SQLite3

# float str int Boolean {}()[]

import sqlite3

db = sqlite3.connect('test.db')
c=db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students(
name TEXT,
age INTEGER,
view INTEGER,
hobby TEXT DEFAULT 0
) ''')
c.execute('''INSERT INTO students VALUES('beka',12,1,0) ''')


db.commit()
db.close()