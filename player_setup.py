from start import player
print('Welcome to the [name] simulator! This is a new type of '
      'simulator designed with the semi-deceased in mind!'
      '\nWhile simple in look and feel, what we are going to take you though' 
      '\nis bleeding edge software we truly believe is going to change the world.'
      "\nLet's start with some basic information.")

# I am going to try to set user input as player stats:
player['age'] = input("How old are you?\n")
player['gender'] = input("What gender do you identify as? Male/Female/Neither\n").lower()
player['city'] = input("What city are you from?\n").upper()

print("Alright, that should do it. This next part is a bit rough, but you'll live."
      "\nIn a sense, at least.\n")
import meeting_pendleton