# Author: Matthew Armstrong
# Date: 6/29/21
# Description: program that prompts the user for an integer the player will try to guess,
# and then gives the correct amount of attempts.
print("Enter the integer for the player to guess.")
correct_guess = int(input())
print("Enter your guess.")
player_guess = 0
guesses_taken = 0
while player_guess != correct_guess:
    player_guess = int(input())
    guesses_taken = guesses_taken + 1
    if player_guess > correct_guess:
        print("Too high - try again:")
    elif player_guess < correct_guess:
        print("Too low - try again:")
    else:
        print("You guessed it in", guesses_taken, "tries.")
