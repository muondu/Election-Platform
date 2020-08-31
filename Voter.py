import sqlite3
db = sqlite3.connect('new_person.db')
cursour  = cursour.cursor()
def new_user():
    found = 0
    while found == 0:
        fName = input("Enter your first name: ")
        sName = input("Enter your second name: ")
        age = input("Enter your age: ")
        password = input("Enter your password: ")
        with sqlite3.connect('new_person.db'):
            cursour = db.cursour()  
        cursour.execute(fName,sName,age,password)