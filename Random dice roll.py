import random

def roll_die(sides=20):
    """Ruller en enkelt terning med 'sides' antal sider."""
    return random.randint(1, sides)

print('Press ENTER to roll the die.')

if input() == '':
    number = roll_die()
    print(f'You rolled: {number}')