# Let's get some user involvement with some questions:
import sys
import time
from start import player
questions = [
    'who am i?',
    'who are you?',
    'why am i here?',
    'what is this?',
    'why am I here?',
    'what do you mean a "waiver"?',
    'where are we?',
    ]
question_for_mr_pendleton = input("Mr. Pendleton: We'll take a second for any questions you may have.\n")
if question_for_mr_pendleton.lower() == questions[0]:
    print("Mr. Pendleton: You're still " + player['name'] + ','
          "\tYou're just not in what we'd call your reality."
          "\tDon't worry though. The whole point is to get you back there.")

elif question_for_mr_pendleton.lower() == questions[1]:
    print("Mr. Pendleton: Why, I'm Mr. Pendleton of course. Dr. Pendleton if you're into those kinds of titles."
          "\tI study the grey stuff between people's ears. Particularly its defense mechanisms."
          "\tHa! That's why we're here actually.")
elif question_for_mr_pendleton.lower() == questions[2]:
    print('')
elif question_for_mr_pendleton.lower() == questions[3]:
    print('')
elif question_for_mr_pendleton.lower() == questions[4]:
    print('')
elif question_for_mr_pendleton.lower() == questions[5]:
    print('')
elif question_for_mr_pendleton.lower() == questions[6]:
    print('')