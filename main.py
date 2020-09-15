import datetime
now = datetime.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 17:
    print("Good afternoon")
elif hour > 17 and hour < 19:
    print("Good evening")
else:
    print('Good night.')

which_person = input("""
Hi. These are the options
a Voter
b Candidate
c Staff member

Choose any of them:  
""")
if which_person == "a" or which_person == "A" or which_person == "Voter" or which_person == "a voter" or which_person == "A voter" or which_person == "A Voter":
    from Voter import *
    Voter()
elif which_person == "b" or which_person == "B" or which_person == "Candidate" or which_person == "b candidate" or which_person == "B candidate" or which_person == "B Candidate":
    from canidates import *
    candidates()
elif which_person == "c" or which_person == "C" or which_person == "Staff member" or which_person == "c staff member" or which_person == "C staff member" or which_person == "C Staff member":
    from staff import *

    staff()
else:
    print("I did not understand you")