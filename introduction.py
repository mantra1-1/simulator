# Let's get some user involvement with some questions:
import sys
import time
from start import player
questions = [
    'who am i?',
    'who are you?',
    'why am i here?',
    'what is this?',
    'what do you mean a "waiver"?',
    'where are we?',
    'no',
    'yes',
    ]
question_for_mr_pendleton = input("Mr. Pendleton: Any questions?\n")
if question_for_mr_pendleton.lower() == questions[0]:
    print("Mr. Pendleton: You're still " + player['name'] + '!'
          "\n\t\t\t   You're just not in what we'd call your reality."
          "\n\t\t\t   Don't worry though. The whole point is to get you back there.")

elif question_for_mr_pendleton.lower() == questions[1]:
    print("Mr. Pendleton: Why, I'm Mr. Pendleton of course. Dr. Pendleton if you're into those kinds of titles."
          "\n\t\t\t   I study the grey stuff between people's ears. Particularly its defense mechanisms."
          "\n\t\t\t   Ha! That's why we're here actually.")
elif question_for_mr_pendleton.lower() == questions[2]:
    print("Mr. Pendleton: You have a unique brain wave we think "
          "will result in a favourable response to the treatment."
          "\n\t\t\t   If not...hey, it's all valuable information.")
elif question_for_mr_pendleton.lower() == questions[3]:
    print("Mr. Pendleton: Hopefully it's your way out but that's up to you.")
elif question_for_mr_pendleton.lower() == questions[4]:
    print("Mr. Pendleton: ...never you mind about that.")
elif question_for_mr_pendleton.lower() == questions[5]:
    print("Mr. Pendleton: I believe this the light rail heading to the University of Washington.")
elif question_for_mr_pendleton.lower() == questions[6]:
    print("Mr. Pendleton: Great! Let's get on with it then.")
elif question_for_mr_pendleton.lower() == questions[7]:
    print("Great! What are they?")
