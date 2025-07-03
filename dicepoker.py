# IMPORTS 
from random import randint                        # Importerer modul til tilfældige tal
from collections import Counter       # Importerer Counter til at tælle terningekombinationer
from time import sleep
# Funktion til at rulle 5 terninger

"""
def roll_dice():
    return [randint(1, 6) for _ in range(5)]  # Returnerer en liste med 5 tilfældige tal mellem 1 og 6

# Funktion til at evaluere en hånd og give en beskrivelse
def evaluate_hand(dice):
    counts = Counter(dice)                  # Tæller forekomster af hver terningværdi
    values = list(counts.values())          # Udtrækker antallet som en liste

    # Tjekker håndens styrke ud fra klassiske pokerregler
    if 5 in values:
        return "Five of a kind" # 5 ens terninger
    elif 4 in values:
        return "Four of a kind" # 4 ens
    elif sorted(values) == [2, 3]:
        return "Full house" # 3 ens + 2 ens
    elif 3 in values:
        return "Three of a kind" # 3 ens
    elif values.count(2) == 2:
        return "Two pairs" # 2 par
    elif 2 in values:
        return "One pair" # 1 par
    else:
        return "High dice" # Ingen kombination — baseret på højeste tal

# Funktion til at spille Dice Poker
def play_dice_poker():
    print("Dice Poker Begins!") # Starter spillet med en besked
    player = roll_dice() # Spillerens terningekast
                               
    opponent = roll_dice() # Modstanderens terningekast

    # Viser spillerens og modstanderens kast og evaluering
    sleep(1)                       # Venter 1 sekund for spænding
    print(f"Opponent roll: {opponent} → {evaluate_hand(opponent)}")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)                       
    print(f"Your roll: {player} → {evaluate_hand(player)}")

# Starter spillet
play_dice_poker()"""


def play_dice_poker():
    def roll_dice():
        return [randint(1, 6) for _ in range(5)]

    # Funktion til at evaluere en hånd og give en beskrivelse
    def evaluate_hand(dice):
        counts = Counter(dice)          # Tæller forekomster af hver terningværdi
        values = list(counts.values())  # Udtrækker antallet som en liste

        if 5 in values:
            return "Five of a kind"
        elif 4 in values:
            return "Four of a kind"
        elif sorted(values) == [2, 3]:
            return "Full house"
        elif 3 in values:
            return "Three of a kind"
        elif values.count(2) == 2:
            return "Two pairs"
        elif 2 in values:
            return "One pair"
        else:
            return "High dice"

    print("Dice Poker Begins!")

    player = roll_dice()
    opponent = roll_dice()

    # Viser spillerens og modstanderens kast og evaluering
    sleep(1) #venter 1 sek for spænding
    print(f"Opponent roll: {opponent} → {evaluate_hand(opponent)}")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(f"Your roll: {player} → {evaluate_hand(player)}")


play_dice_poker()