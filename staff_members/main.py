import sqlite3
daan = sqlite3.connect('voting.db')
d = daan.cursor()
conn = sqlite3.connect('staff.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS staff_member(username VARCHAR,password VARCHAR)')


username = input("Enter your username: ")
password = input("Enter your password: ")

c.execute("INSERT INTO staff_member(username, password)VALUES(?,?)",(username, password))  

def count_vote():
    for row in d.execute('SELECT * FROM voted'):
        empty_list = []
        appending = empty_list.append(row)
        print(empty_list)
        votes = list(appending)
        counting_votes = votes.count()
        print(counting_votes)


count_vote()