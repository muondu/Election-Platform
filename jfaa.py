import sqlite3

conn = sqlite3.connect('ko.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS ja(game TEXT)')
c.execute('INSERT INTO ja VALUES("Minceraft")')
# conn.commit()
def read_db():
    c.execute('SELECT * FROM ja')
    rob = c.fetchall()
    game = []
    for jailbrake in rob:
        print(jailbrake)
        for mad_city in jailbrake:
            game.append(mad_city)
    print(game)
    floor_lava = game.count('Roblox')
    floor_loa = game.count('Minecraft')
    print(floor_lava,floor_loa)

read_db()
def read2_db():
    c.execute('SELECT * FROM ja')
    rob = c.fetchall()
    game2 = [item for item in rob]
    print(game2)
    
# read2_db()
def read3_db():
    jakaa = [1,2,3,4]
    floor_is_lava = []
    for oof in jakaa:
        floor_is_lava.append(oof)
    print(floor_is_lava)
    
# read3_db()
def read4_db():

    jakaa = [1,2,3,4]
    floor_is_lava = [dub for dub in jakaa]
    floor_is_city = [dub * dub for dub in jakaa]
    print(jakaa)
    print(floor_is_lava)
    print(floor_is_city)
# read4_db()
