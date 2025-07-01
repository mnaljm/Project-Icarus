import random

def roll_die(sides=20):
    """Rolls a single die with 'sides' number of sides."""
    return random.randint(1, sides)

print('Type "roll" to rolle the die.')

user_input = input()  # Læs brugerens input

if user_input == 'roll':
    # Brugeren trykkede kun ENTER - rul terningen
    number = roll_die()
    print(f'You rolled: {number}')
else:
    print(f'Invalid input "{user_input}". Please type "roll" to roll the die.')