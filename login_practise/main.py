import sqlite3
def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        find_user 