import sqlite3
conn = sqlite3.connect('new_person.db')
c  = conn.cursor()
donn = sqlite3.connect('voted_people.db')
d = donn.cursor()
def new_user():
        fName = input("Enter your first name: ")
        sName = input("Enter your second name: ")
        age = int(input("Enter your age: "))
        if age < 18:
            print("You are not allowed to vote")
        else:
            password = input("Enter your password: ")
        c.execute('INSERT INTO new_user VALUES(?,?,?,?)',(fName,sName,age,password))
new_user()
def login():
    for i in range(3):
        first_name = input("Enter your first name: ")
        second_name = input("Enter your second name: ")
        age_person = int(input("Enter your age: "))
        password_person = input("Enter your password: ")
        
        find_user = ('SELECT * FROM new_user WHERE fName = ?, sName = ?, age = ? AND password = ?')
        c.execute(find_user,[(first_name),(second_name),(age_person),(password_person)])
        results = c.fetchall()

        if results:
            for i in results:
                print("Welcome " + i[2])
                voted_or_not = input("Have you voted No(n) or yes(Y): ")
                if voted_or_not == "no" or voted_or_not == "n" or "No":
                    d