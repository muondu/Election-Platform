import sqlite3

fan = sqlite3.connect('candidates.db')
f = fan.cursor()
daan = sqlite3.connect('voting.db')
d = daan.cursor()
conn = sqlite3.connect('staff.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS staff_member(username VARCHAR,password VARCHAR)')


username = input("Enter your username: ")
password = input("Enter your password: ")

c.execute("INSERT INTO staff_member(username, password)VALUES(?,?)",(username, password))  

def count_vote():
    fetch_all = c.fetchall()

    votes = [item for a in fetch_all for item in a]

    find_voter = list(f.execute('SELECT * FROM canidate'))

count_vote()