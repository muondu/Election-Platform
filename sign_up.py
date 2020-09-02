import sqlite3
conn = sqlite3.connect('new_person.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS new_user(fName TEXT, sName TEXT, age INTEGER, password VARCHAR)')

c.execute("INSERT INTO new_user VALUES('Munene','Muondu','11','12')")

c.execute('CREATE TABLE IF NOT EXISTS voted(vfName TEXT, vsName TEXT, vage INTEGER, vpassword VARCHAR)')
c.execute("INSERT INTO voted VALUES('John','Mathenge','19','1')")
