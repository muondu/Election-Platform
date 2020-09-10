import sqlite3
def candidates():
    conn = sqlite3.connect('candidates.db')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS candidate(fName TEXT,sName TEXT)')
    firstName = input("Enter your first name: ")
    secondName = input("Enter your second name: ")
    c.execute("INSERT INTO candidate(fName, sName)VALUES(?,?)",(firstName, secondName))    
    c.execute('SELECT * FROM candidate')
    print(c.fetchall())
    conn.commit()
candidates()        

