import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

highscore = 0
computeroptions = [rock, paper, scissors]
i = 1
while i < 5:
    playerpick = str(input(
        "Pick rock, paper or scissors to begin the game with the computer: "))
    if playerpick == "rock":
        print('You choose:')
        print(rock)
        print('The computer chooses: ')
        x = computeroptions[random.randint(0, 2)]
        print(x)
        if x == rock:
            print("It's a draw!")
        elif x == paper:
            print("You loose!")
            highscore = highscore - 1
        elif x == scissors:
            print("You win!")
            highscore = highscore + 1
            i += 1
    if playerpick == "paper":
        print('You choose: ')
        print(paper)
        print('The computer chooses: ')
        x = computeroptions[random.randint(0, 2)]
        print(x)
        if x == rock:
            print("You win!")
            highscore = highscore - 1
            i += 1
        elif x == paper:
            print("It's a draw!")
        elif x == scissors:
            print("You loose!")
            highscore = highscore + 1
            i += 1
    if playerpick == "scissors":
        print('You choose: ')
        print(scissors)
        print('The computer chooses: ')
        x = computeroptions[random.randint(0, 2)]
        print(x)
        if x == rock:
            print("You loose!")
            highscore = highscore - 1
            i += 1
        elif x == paper:
            print("You win!")
            highscore = highscore + 1
            i += 1
        elif x == scissors:
            print("It's a draw!")
    print(f'Your score is: {highscore}')
print(f"Game Over! Your score is {highscore}")
