import sqlite3

def login():
    for i in range(4):
        username = input("Pls enter your username: ")
        password = input("Pls enter your password: ")
        with sqlite3.connect("Quiz.db") as db:
            cursour = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ? AND password = ?')
        cursour.execute(find_user,[(username),(password)])
        results = cursour.fetchall()

        if results:
            for j in results:
                print("Welcome "+j[0])
            return "exit"
            break
        else:
            print("Username and password not recognised")
            again = input("Do you want to try again Yes(y) or No(n)? ")
            if again.lower == "n":
                print("GoodBye.")
def newUser():
    found = 0
    while found ==0:
        username = input("Enter your username: ")
        with sqlite3.connect("Quiz.db") as db:
            cursour = db.cursor()
        findUser = ('SELECT * FROM user WHERE username = ?')
        cursour.execute(findUser,([username]))

        if cursour.fetchall():
            print("Username taken, please try again")
        else:
            found = 1
    password = input("Enter your password: ")
    password1 = input("renter your password: ")
    while password != password1:
        print("Your passwords did not match")
        password = input("Enter your password: ")
        password1 = input("renter your password: ")
    insertData = 'INSERT INTO user (username, password) VALUES(?,?)'
    cursour.execute(insertData,[(username),(password)])
    db.commit()
newUser()
# newUser()

# login()