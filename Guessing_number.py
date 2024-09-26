from random import randint
from replit import clear

EASY = 10
HARD = 5

def validation(answer, val_list):
    if answer in val_list:
        return True
    else:
        print("\nUpss! You choose an invalid optsion! Try again!")

def is_number(value):
    if value.isdigit():
        value = int(value)
        if value > 100 or value < 1:
            print("Please choose a number between 1 and 100.")
            return False
        return True
    else:
        print("Please type an integer!")
        return False

def choose_level():
    while True:
        diff = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ").lower()
        if validation(diff, ["e","h"]):
            break

    lives= EASY if diff == "e" else HARD
    return lives

def guess_already(exist_numbers):
    print("\nYou already had choose this number! Please choose another one! Numbers guess:")
    for _ in exist_numbers:
        print(f"{_} : {exist_numbers[_]}")
    print()
    return True

def get_number(lives, exist_numers):
    while True:
        while True:
            numb_guess = input(f"You have {lives} attemps remaning to guess the number.\nMake a guess: ").lower()
            if is_number(numb_guess):
                numb_guess = int(numb_guess)
                break   
        if numb_guess in exist_numers:
            guess_already(exist_numers)
        else:
            break
    return exist_numers, numb_guess

def lose_win(lives, numb_guess, numb, exist_numers):          
    if numb_guess == numb:
        print(f"\nCongratulations! You got it! The number is {numb}.")
        lives= -1
    else:
        if numb < numb_guess:
            print("Too high.\nGuess again.")
            exist_numers[numb_guess] = "too high"
            lives-=1
        else:
            print("Too low.\nGuess again.")
            exist_numers[numb_guess] = "too low"
            lives-=1
    return lives, exist_numers

def guess_number(numb, lives):
    exist_numers={}

    while lives>0 :

        exist_numers, numb_guess = get_number(lives, exist_numers)
        
        lives, exist_numers = lose_win(lives, numb_guess, numb, exist_numers)
        
    if lives== 0:
        print(f"\nYou've run out of guesses, you lose.\nThe number is {numb}.")

def play_again():
    while True:
        play_again = input("\nDo you want to play again? Please type 'y' for yes or 'n' for no: ").lower()
        if validation(play_again, ["y", "n"]):
            return play_again == "y"


def number_game():
    clear()
    print("Welcom to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    number = randint(1, 100)
    # print(number)

    lives= choose_level()

    guess_number(number, lives)

    if play_again():
        number_game()
    else:
        print ("\nSee you next time!")


number_game()

