import sqlite3

conn = sqlite3.connect('numbers.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS number(name INTEGER)')
c.execute('INSERT INTO number VALUES("1")')
c.execute('INSERT INTO number VALUES("2")')
c.execute('INSERT INTO number VALUES("3")')
c.execute('INSERT INTO number VALUES("4")')
c.execute('INSERT INTO number VALUES("5")')
c.execute('INSERT INTO number VALUES("6")')
c.execute('INSERT INTO number VALUES("7")')
c.execute('INSERT INTO number VALUES("8")')
c.execute('INSERT INTO number VALUES("9")')
c.execute('INSERT INTO number VALUES("10")')
# conn.commit()
def youtuber():
    c.execute('SELECT * FROM number')
    hello = c.fetchall()
    # print(hello)

    dub = [value for a in hello for value in a] 
    adding = sum(dub)
    print(adding)
    c.execute('CREATE TABLE IF NOT EXISTS total(name INGEGER)')
    c.execute('INSERT INTO total VALUES(?)',(adding,))

youtuber()