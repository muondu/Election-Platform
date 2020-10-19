import sqlite3
conn = sqlite3.connect('candidates.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS candidate(fName TEXT,sName TEXT)')
c.execute("INSERT INTO candidate(fName, sName)VALUES('Sharon','Karimi')")        

conn.commit()