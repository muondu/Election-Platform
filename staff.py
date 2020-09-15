import sqlite3
def staff():
    doon = sqlite3.connect('candidates.db')
    d = doon.cursor()
    conn = sqlite3.connect('voting.db')
    c = conn.cursor()

    c.execute('SELECT * FROM voted')
    cal = c.fetchall()

    votes = []

    d.execute('SELECT * FROM candidate')
    print(d.fetchall())
    which_candidate_find = input("Which candidate are you searching for: ")
    nal = [item for a in cal for item in a]
    find_candidate = nal.count(which_candidate_find)
    print(find_candidate)
staff()
