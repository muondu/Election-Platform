import sqlite3
donn = sqlite3.connect('voter.db')
d = donn.cursor()
    
d.execute('CREATE TABLE IF NOT EXISTS voter(fName TEXT,sName TEXT,id_number INTEGER)')
firstName = input("Enter your first name: ")

second_name = input("Enter your second name: ")

id_number = int(input("Enter your id_number(8 digits): "))
d.execute("INSERT INTO voter(fName, sName,id_number)VALUES(?,?,?)",(firstName, secondName,id_number))