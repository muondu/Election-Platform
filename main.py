import time
from Voter import * as vote
import datetime
now = datetime.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Good night.')

def canidate_or_voter():

    what_you__are = input("""Hello. I am the voting program of the future. These are the options available for login. Are you are 
    a Voter
    b Canidate

    """)
    if what_you__are == "a" or what_you__are == "voter" or what_you__are == "A" or what_you__are == "Voter":
        print(vote)
    elif what_you__are == "b" or what_you__are == "canidate" or what_you__are == "B" or what_you__are == "Candidate":
        print("Wohhoo")
    else:
        print("I did not understand you")
        canidate_or_voter()
canidate_or_voter()
