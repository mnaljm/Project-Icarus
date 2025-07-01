def roll_die(sides=20):
    """Ruller en enkelt terning med 'sides' antal sider."""
    return random.randint(1, sides)  # Returnerer et tilfældigt tal mellem 1 og 'sides'

def roll_with_advantage(sides=20):
    """Ruller to terninger og returnerer den største (advantage)."""
    roll1 = roll_die(sides)
    roll2 = roll_die(sides)
    return max(roll1, roll2)
