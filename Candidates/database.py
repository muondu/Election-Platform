import sqlite3
conn = sqlite3.connect("candidates.db")
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS candidates(fName TEXT, sName TEXT, age INTEGER)')
c.execute("INSERT INTO  candidates (fName,sName,age) VALUES('Nesh','Muondu','18')")
conn.commit()

c.execute('SELECT * FROM candidates')
