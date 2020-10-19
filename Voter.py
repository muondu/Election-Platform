import sqlite3
def Voter():
    candidate = sqlite3.connect('candidates.db')
    can = candidate.cursor()
    donn = sqlite3.connect('voter.db')
    d = donn.cursor()
    conn = sqlite3.connect('voting.db')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS voted(name TEXT)')
    d.execute('CREATE TABLE IF NOT EXISTS voter(fName TEXT,sName TEXT,id_number INTEGER)')
    firstName = input("Enter your first name: ")
    if firstName == " ":
        print("You cannot put spaces")
        Voter()
    else:
        def secondName():
            global second_name
            second_name = input("Enter your second name: ")
        secondName()
        if second_name == " ":
            print("You can't piut spaces")
            secondName()
        else:
            try:
                age = int(input("Enter your age: "))
                if age < 18:
                    print("You are not able to vote")
                    
                elif age > 18:
                    try:
                        id_number = int(input("Enter your id_number(8 digits): "))
                        id_num = str(id_number)
                        
                        if len(id_num) < 7 or len(id_num) > 9:
                            print("The id number does not reach the number of digits")
                        else:
                            d.execute("INSERT INTO voter(fName, sName,id_number)VALUES(?,?,?)",(firstName, second_name,id_number)) 
                            can.execute('SELECT * from candidate')
                            print(can.fetchall())
                            def voting_canidate():
                                # for row in can.execute('SELECT * from candidate'):
                                #     list1 = list(row)
                                #     print(list1)
                                #     which_canidate = input("Which canidate do you want:  ")
                                #     print("Thank you for voting. Good Bye")
                                #     c.execute('INSERT INTO voted VALUES(?)',(which_canidate,))
                                #     # c.execute('SELECT * FROM voted')
                                #     conn.commit()
                                #     exit()
                                #     break
                                which_canidate = input("Which canidate do you want:  ")
                                if which_canidate == " ":
                                    print("There are no spacebars")
                                    voting_canidate()
                                else:
                                    print("Thank you for voting. Good bye")
                               
                                    c.execute('INSERT INTO voted VALUES(?)',(which_canidate,))
                                    conn.commit()
                                    exit()
                                    
                                    
                            voting_canidate()
                    except ValueError:
                        print("That is not a number")
                        id_number_function()

            except ValueError:
                print("Pls input a number")
            
    



           

                
        
Voter()
