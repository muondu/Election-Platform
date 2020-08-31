import sqlite3
conn = sqlite3.connect('new_person.db')
c = conn.cursor()
new_person
c.execute('CREATE TABLE IF NOT EXISTS new_user(fName TEXT, sName TEXT, age INTEGER, password VARCHAR)')

c.execute("INSERT INTO new_user VALUES('Munene','Muondu','11','12')")
