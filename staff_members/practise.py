import sqlite3
conn = sqlite3.connect('practise.db')
c = conn.cursor()


# username = input("Enter your username: ")
# password = input("Enter your password: ")
def create():
    c.execute('CREATE TABLE IF NOT EXISTS practise(name TEXT)')
    c.execute("INSERT INTO practise VALUES('Core')")  
    conn.commit()
create()


def read():
    # dub = c.execute('SELECT * FROM practise')
    c.execute('SELECT * FROM practise')
    print(c.fetchall())
    # print(dub)
read()

def cont():
    for row in c.execute('SELECT * FROM practise'):
        list1 = []
        list1 = list(row)
        counting = list1.count('Core')
        print(counting)


    # print(list1)
    # coounting = list1.count("Core")
    # print(coounting)
cont()