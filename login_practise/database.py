import sqlite3
conn = sqlite3.connect("Quiz.db")
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user(username VARCHAR, password VARCHAR)')
c.execute("INSERT INTO  user (username, password) VALUES('NeroNesh','12')")
conn.commit()

c.execute('SELECT * FROM user')
print(c.fetchall())