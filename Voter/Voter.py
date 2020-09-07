import sqlite3
canidate = sqlite3.connect('candidates.db')
can = canidate.cursor()
donn = sqlite3.connect('voter.db')
d = donn.commit()
conn = sqlite3.connect('voting.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS tryal(name TEXT)')
donn.execute('CREATE TABLE IF NOT EXISTS voter(fName TEXT,sName TEXT,id_number INTEGER)')
firstName = input("Enter your first name: ")
secondName = input("Enter your second name: ")
age = int(input("Enter your age: "))
id_number = int(input("Enter your id_number: "))

donn.execute("INSERT INTO voter(fName, sName,id_number)VALUES(?,?,?)",(firstName, secondName,id_number))  


canidates = can.execute('SELECT * from candidate')
canidate.commit()
print(can.fetchall())
which_canidate = input("Which canidate do you want:  ")
if which_canidate in canidates:

    conn.execute('INSERT INTO tryal VALUES(?)',which_canidate)
    conn.execute('SELECT * FROM tryal')
    conn.commit()
    print(c.fetchall())

    

