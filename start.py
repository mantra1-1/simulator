# /// Establish player name and greeting:
player = {}
name = str(input('Enter your name: ')).title()
player['name'] = name

print('Hello', player['name'] + '.')

# /// Ask player if they want to play this game:
answer = ['yes', 'no']

willingness = input("We're going to play a game, does that sound fun?\n")

if willingness.lower() == answer[0]:
    import player_setup
elif willingness.lower() == answer[1]:
    print("That's okay " + player['name'] + ", come back when you're ready.")
else:
    print('Invalid input. Please answer yes or no.')
