import random  # Importerer random-biblioteket, som bruges til tilfældige tal

def roll_die(sides=20):
    """Ruller en enkelt terning med 'sides' antal sider."""
    return random.randint(1, sides)  # Returnerer et tilfældigt tal mellem 1 og 'sides'

print('Press ENTER to roll the die.')  # Beder brugeren om at trykke ENTER

if input() == '':  # Hvis brugeren trykker ENTER uden at skrive noget
    number = roll_die()  # Kald funktionen roll_die() for at rulle en d20
    print(f'You rolled: {number}')  # Udskriv resultatet af terningkastet
	