import sqlite3
def sing_up():
    print("We are singing you up")
    found = 0
    while found == 0:
        fName = input("Enter your first name: ")
        # sName = input("Enter your second: ")                                                                                                                                                                                                                                                                                                                                                                                                11111111111111111111111`        11```````1``1   qqqqqq                                                                                                                                               name: ")
        age = int(input("Enter your age: "))
        if age != int():
            print("Please write a number.")
        else:
            if age < 18:
                print("Your age is not found")
                found = 1
            elif age > 18:
                global id_number
                id_number = int(input("Enter your id_number: "))
                with sqlite3.connect('Voter.db') as db:
                    global cursour
                    cursour = db.cursor()
                find_id = ('SELECT * from voter WHERE id_number = ?')
                cursour.execute(find_id,([id_number]))
                if cursour.fetchall():
                    print("ID_number taken")
                else:
                    found = 1
            else:
                print("You are not old enough.")
                found = 1
    insertData = 'INSERT INTO voter (fName, sName, age, id_number) VALUES(?,?,?)' 
    cursour.execute(insertData,[(fName),(age),(id_number)])
sing_up()
def login():
    while True:
        fName = input("Enter your first name: ")
        sName = input("Enter your first name: ")
        id_number = int(input("Enter your first name: "))
        with sqlite3.connect('Voter.db') as db:
            cursour =  db.cursor
        find_user = ('SELECT * FROM voter WHERE fName = ?, sName = ? AND id_number = ?')
        cursour.execute(find_user,[(fName,sName,id_number)])
        results = cursour.fetchall()
        
        if results:
            for i in results:
                print("Welcome "+i[0,2])
                print("These are the canidates")
                with sqlite3.connect('canidates.db') as db:
                    cursour = db.cursor()
                print("There are the canidates")
                results = print(cursour.fetchall())
                which_canidate = input("Which canidate do u want: ")
                if which_canidate in results:
                    print("You have voted for " + which_canidate)
                    print("Goodbye.")
                else:
                    print("The canidate you have voted for.")
                    break

