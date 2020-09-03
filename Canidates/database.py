import sqlite3
conn = sqlite3.connect("canidates.db")
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS canidate(fName TEXT, sName TEXT, age INTEGER)')
c.execute("INSERT INTO  canidate (fName,sName,age) VALUES('Nesh','Muondu','18')")
conn.commit()

c.execute('SELECT * FROM canidate')
