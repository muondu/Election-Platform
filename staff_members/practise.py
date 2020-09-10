import sqlite3
conn = sqlite3.connect('practise.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS practise(name TEXT)')


username = input("Enter your username: ")
password = input("Enter your password: ")

c.execute("INSERT INTO practise(name)VALUES('Newton')")  

conn.commit()

# def count_vote():
for row in c.execute('SELECT * FROM practise'):
    print(row)
    votes = list(row)
    # print(votes)
    # for core in votes:
        # print(core)
    # empty_list = []
    # appending = empty_list.append(row)
    # print(empty_list)
    # counting_votes = votes.count()
    # print(counting_votes)


# count_vote()