import sqlite3
conn = sqlite3.connect('newton.db')
c = conn.cursor()


# Create table
c.execute('''CREATE TABLE IF NOT EXISTS stocks (name text)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('NEWTON')")
c.execute("INSERT INTO stocks VALUES ('ADAMS')")

# Save (commit) the changes
conn.commit()


for row in c.execute('SELECT * FROM stocks'):
    new_list = list(row)
    print(new_list)
    
    for a in new_list:
        print(a)
        
        user = input('enter name: ')
        
        if a == user:
            print('it works')
        
            
        else:
            print('oops!')






