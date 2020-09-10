import sqlite3
conn = sqlite3.connect('practise4.db')
c = conn.cursor()


c.execute('SELECT * FROM dub')

aa = c.fetchall()

cc = [lol for a in aa for lol in a]

cola = cc.count('Kalonzo')
dola = cc.count('Ruto')
print(cola)
print(dola)
print("Ruto wins")
