import sqlite3
conn = sqlite3.connect("Voter.db")
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS voter(fName TEXT, sName TEXT, age INTEGER, id_number INTEGER)')
c.execute("INSERT INTO  voter (fName,age,id_number) VALUES('Nesh','18','12345678')")
conn.commit()

c.execute('SELECT * FROM voter')
