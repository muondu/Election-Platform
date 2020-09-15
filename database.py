import sqlite3
conn = sqlite3.connect("Voter.db")
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS voter(fName TEXT, sName TEXT, age INTEGER, id_number INTEGER)')
c.execute("INSERT INTO  voter(fName,sName,age,id_number) VALUES('Nero','Nesh','18','12345678')")
conn.commit()
conn.commit()

c.execute('SELECT * FROM voter')

c.execute('CREATE TABLE IF NOT EXISTS voted(fName,sName,id_number) VALUES()')