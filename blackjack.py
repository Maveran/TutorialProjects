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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# print(random.randint(1, 10))


def player_hand():
    """Creates the initial set of two cards for the player"""
    player = []
    player.append(cards[random.randint(1, 10)])
    player.append(cards[random.randint(1, 10)])
    return player


def computer_hand():
    """Creates the initial set of two cards for the computer"""
    computer_hand = []
    computer_hand.append(cards[random.randint(1, 10)])
    computer_hand.append(cards[random.randint(1, 10)])
    return computer_hand


def count_score():
    """function for counting the sum of elements in a players set"""


def gamestart():
    computer = computer_hand()
    player = player_hand()
    print("Welcome to the blackjack game, here is your initial set: ")
    print(f"Computer hand: {computer}")
    print(f"Player hand: {player}")


# player_hand()
gamestart()
