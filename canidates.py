import sqlite3
def candidates():
    conn = sqlite3.connect('candidates.db')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS candidate(fName TEXT,sName TEXT)')
    firstName = input("Enter your first name: ")
    if firstName == " ":
        print("You can't put spaces")
        candidates()
    else:
        secondName = input("Enter your second name: ")
        if secondName == " ":
            print("You can't put spaces")
        else:
            age = int(input("Enter your age:  "))
            
            id_number = int(input("Enter your id number(8 digits):  "))
            dub = str(id_number())
            if len(dub) >= 7 or len(dub) >= 8:
                c.execute("INSERT INTO candidate(fName, sName)VALUES(?,?)",(firstName, secondName))    
                c.execute('SELECT * FROM candidate')
                print(c.fetchall())
                conn.commit()
                exit()

            else:
                print("I did not understand you")

        
        
    
candidates()        

