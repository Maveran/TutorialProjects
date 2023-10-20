############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from cardsAscii import cards2
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# print(random.randint(1, 10))


def player_hand():
    """Creates the initial set of two cards for the player"""
    player = []
    player.append(cards[random.randint(0, 12)])
    return player


def computer_hand():
    """Creates the initial set of two cards for the computer"""
    computer_hand = []
    computer_hand.append(cards[random.randint(0, 12)])
    return computer_hand


# def count_score(score):
#     """function for counting the sum of elements in a players set"""
#     current_score = 0
#     temp = []
#     for x in score:
#         temp.append(score(x))
#         current_score += x
def decision():
    decision_continue = input(
        "Do you want to draw another card? Type Y or N: ")
    if decision_continue == "Y":
        return True
    elif decision_continue == "N":
        return False


def gamestart():

    decide = True
    player1 = []
    computer_hand1 = []

    def generate_initial_player():

        player1.append(cards[random.randint(0, 12)])
        for x in player1:

            print(f'Player Hand: {cards2[x - 2]}')
        return player1

    def generate_initial_pc():

        computer_hand1.append(cards[random.randint(0, 12)])
        for x in computer_hand1:
            print(f'Computer hand: {cards2[x - 2]}')
        return computer_hand1

    computer = generate_initial_pc()
    player = generate_initial_player()

    computer_score = 0
    playerdeck = []
    computerdeck = []
    player_score = 0
    print("Welcome to the blackjack game, here is your initial set: ")
    while decide == True:

        print(f"Computer hand: {computer}")
        print(f"Player hand: {player}")

        computer_score = 0
        for x in computer:
            computer_score += x
        print(f"Computer score: {computer_score}")

        player_score = 0
        for x in player:
            player_score += x

        print(f"Player score: {player_score}")
        if player_score == 21:
            print("Player wins!")
            break
        if computer_score == 21:
            print("Computer wins!")
            break
        if player_score > 21:
            print("Player looses")
            break
        if computer_score > 21:
            print("Computer looses")
            break
        decide = decision()

        if decide == True:
            player1.append(cards[random.randint(0, 12)])
            print("Player hand :")
            for x in player1:
                print(cards2[x - 2])
                playerdeck.append(cards2[x - 2])
            computer_hand1.append(cards[random.randint(0, 12)])
            print("Computer Hand :")
            for x in computer_hand1:
                print(cards2[x - 2])


gamestart()
