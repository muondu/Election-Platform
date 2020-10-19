import datetime as time

now = time.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 11 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Good night.')
def which_person_function():
    global which_person
    which_person = input("""
    Who do you want to be
    a Voter
    b Staff member

    Choose any of them:  
    """)
which_person_function()
if which_person == "a" or which_person == "A" or which_person == "Voter" or which_person == "a voter" or which_person == "A voter" or which_person == "A Voter":
    from Voter import *
    Voter() 
elif which_person == "b" or which_person == "B" or which_person == "Staff member" or which_person == "b staff member" or which_person == "B staff member" or which_person == "B Staff member":
    from staff import *

    staff()
else:
    print("I did not understand you")
    which_person_function()