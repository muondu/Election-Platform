import sqlite3
conn = sqlite3.connect('practise3.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS jam(name TEXT)')

c.execute('INSERT INTO jam VALUES("strawberry")')
conn.commit()

c.execute('SELECT * FROM jam')

yummy = c.fetchall()

delicious = [item for a in yummy for item in a]

tasty = delicious.count('strawberry')
print(tasty)