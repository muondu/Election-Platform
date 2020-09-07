import sqlite3
conn = sqlite3.connect('tryal.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS tryal(name TEXT)')
c.execute('INSERT INTO tryal VALUES("Nesh")')
c.execute('SELECT * FROM tryal')
print(c.fetchall())