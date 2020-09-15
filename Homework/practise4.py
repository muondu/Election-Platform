import sqlite3
conn = sqlite3.connect('practise4.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS dub(name1 TEXT,name2 TEXT)')

# c.execute('INSERT INTO dub(name1) VALUES("Ruto")')
c.execute('INSERT INTO dub(name2) VALUES("Kalonzo")')
conn.commit()


