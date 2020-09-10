import sqlite3
conn = sqlite3.connect('practise2.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS games(game1 TEXT)')
c.execute('INSERT INTO games(game1) VALUES ("Fall Guys")')
c.execute('INSERT INTO games(game1) VALUES ("Minecraft")')
c.execute('INSERT INTO games(game1) VALUES ("Roblox")')
c.execute('INSERT INTO games(game1) VALUES ("Human fall flat")')
# c.execute('INSERT INTO car(car1) VALUES ("BMW")')
# c.execute('INSERT INTO car(car1) VALUES ("Toyota")')
# c.execute('INSERT INTO car(car1) VALUES ("Toyota")')
# c.execute('SELECT * FROM car')       
# db_catching = c.fetchall()
# # print(type(db_catching))
# # print(db_catching)
# conn.commit()
# conn.close()
# a = list(db_catching)
# store_value = input("Enter any name above: ")
# for new in a:
#     print(new)
#     # aa = list(a)
#     # print(aa)
#     # print(type(aa))
#     # if store_value == a:
#     #     print("Yaay")
#     # else:
#     #     print("Bye")
for row in c.execute('SELECT * FROM games'):
    # print(row)
    list1 = list(row)
    # print(list1)
    for fall_guys in list1:
        print(fall_guys)
        user_input = input("Enter any game above: ")
        if fall_guys == user_input:
            print("You are now playing "+ user_input)
            break
        else:
            print("HMMMM :() ")
            break