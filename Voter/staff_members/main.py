import sqlite3
conn = sqlite3.connect('staff.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS voter(username VARCHAR,password VARCHAR)')

username = input("Enter your username: ")
password = input("Enter your password: ")

c.execute("INSERT INTO voter(username, password)VALUES(?,?)",(username, password))  

