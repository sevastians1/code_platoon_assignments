# this will be the main file that keeps the program up and running
import random
from guessing_game import *


game = GuessingGame(random.randint(1, 100))

last_guess = None
last_result = None


while game.solved(last_guess) == False:

    if last_guess != None:
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    

    last_guess = int(input("Enter your guess: "))
    last_result = game.user_guess(last_guess)

print(f"{last_guess} was correct!")