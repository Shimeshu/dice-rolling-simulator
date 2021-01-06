'''
Creating a Dice Rolling Simulator in Python
'''
import random

dice1 = '''
                     _ _ _ _
                    |       |
                    |       |
                    |   o   |
                    |       |
                    |       |
                    |_ _ _ _|
'''

dice2 = '''
                     _ _ _ _
                    |   o   |
                    |       |
                    |       |
                    |       |
                    |   o   |
                    |_ _ _ _|
'''

dice3 = '''
                     _ _ _ _
                    | o     |
                    |       |
                    |   o   |
                    |       |
                    |     o |
                    |_ _ _ _|
'''

dice4 = '''
                     _ _ _ _
                    | o   o |
                    |       |
                    |       |
                    |       |
                    | o   o |
                    |_ _ _ _|
'''

dice5 = '''
                     _ _ _ _
                    | o   o |
                    |       |
                    |   o   |
                    |       |
                    | o   o |
                    |_ _ _ _|
'''

dice6 = '''
                     _ _ _ _
                    | o o o |
                    |       |
                    |       |
                    |       |
                    | o o o |
                    |_ _ _ _|
'''

dice7 = r'''
        ----            ____    ____            ----
|    |  |       |      |       |    |   |\__/|  |
| /\ |  |---    |      |       |    |   |    |  |---
|/  \|  |       |___   |____   |____|   |    |  |
        ----                                    ----
'''

play_count = 0
run = True
win_count = 0
lost_count = 0
not_given_correct_value = 0
start = input("Enter [R] to roll the dice ---| ")

while run:

    if start == 'R':
        print("DICE ROLLING SIMULATOR")
        print(dice7)
        guess_dice = random.randrange(1, 6)


        try:
            roll = int(input("Guess the Dice Number ---| "))
            if roll == 1:
                print("Your Guess ---| \n" + dice1)
            elif roll == 2:
                print("Your Guess ---| \n" + dice2)
            elif roll == 3:
                print("Your Guess ---| \n" + dice3)
            elif roll == 4:
                print("Your Guess ---| \n" + dice4)
            elif roll == 5:
                print("Your Guess ---| \n" + dice5)
            elif roll == 6:
                print("Your Guess ---| \n" + dice6)
            else:
                print("Your Guess ---| None")

            if guess_dice == 1:
                print("Actual Dice Number ---| \n" + dice1)
            elif guess_dice == 2:
                print("Actual Dice Number ---| \n" + dice2)
            elif guess_dice == 3:
                print("Actual Dice Number ---| \n" + dice3)
            elif guess_dice == 4:
                print("Actual Dice Number ---| \n" + dice4)
            elif guess_dice == 5:
                print("Actual Dice Number ---| \n" + dice5)
            elif guess_dice == 6:
                print("Actual Dice Number ---| \n" + dice6)
            else:
                print("Actual Dice Number ---| None")

            if roll == guess_dice:
                print(f"Your Guess {roll} = Dice Number {guess_dice}")
                win_count += 1
                print("Congrats! You Won!")
            elif roll != guess_dice:
                print("Your Guess does not match the Dice Number! You Lose! ")
                lost_count += 1
                print(f"Dice Number ---| {guess_dice}")
        except ValueError:
            print("Enter Correct Value! ")
            not_given_correct_value += 1


        play_again = input("Wanna Play Again [Y/N] ---| ")

        if play_again == "N":

            run = False
            play_count += 1
            print("Thanks For Playing! :)")
            print(f'''
Number of Times Played ---| {play_count}
Won ---| {win_count}
Lost ---| {lost_count}
Incorrect Values Given ---| {not_given_correct_value}
            ''')

        elif play_again == "Y":

            play_count += 1
            print(f"Number of times played ---| {play_count}")
        else:
            run = False
            play_count += 1
            print("Thanks For Playing! :)")
            print(f'''
Number of Times Played ---| {play_count}
Won ---| {win_count}
Lost ---| {lost_count}
Incorrect Values Given ---| {not_given_correct_value}
            ''') 
        if play_count == 3:
            run = False
            print("Sorry! Your Chances are Over! ")
            print(f'''
Number of Times Played ---| {play_count}
Won ---| {win_count}
Lost ---| {lost_count}
Incorrect Values Given ---| {not_given_correct_value}
            ''')

    else:
        break
