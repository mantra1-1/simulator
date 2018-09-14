# /// Establish player name and greeting:
player = {}
name = input('Enter your name: ').title()
player['name'] = name
print('Hello', str(player['name']) + '.')

# /// Ask player if they want to play this game:
answer = ['yes', 'no']

willingness = input("We're going to play a game, does that sound fun?\n")

if willingness.lower() == answer[0]:
    print("That would have been a great choice if not for...")
    import meeting_pendleton
elif willingness.lower() == answer[1]:
    print("That's okay " + player['name'] + ", come back when you're ready.")
else:
    print('Invalid input. Please answer yes or no.')
