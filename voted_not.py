import sqlite3
conn = sqlite3.connect('voted_people.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS voted(fName TEXT sName TEXT age INTEGER password TEXT')
c.execute('INSERT INTO voted(James, Kitonge, 19,13')