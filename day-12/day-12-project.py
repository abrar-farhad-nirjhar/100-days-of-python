import random
print("Welcome to the Number Guessing Game!!")
print("I'm thinking of a number between 1 and 100.")
# Declaring the global variables
SELECTED_NUMBER = random.randint(1,100)
EASY_GUESSES = 10
HARD_GUESSES = 5


# Getting the difficulty as the input
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


# setting the number of guesses
if difficulty == 'easy':
    remaining_guesses = EASY_GUESSES
else:
    remaining_guesses = HARD_GUESSES

def input_guess():
    return int(input("Make a guess: "))

# GAME LOOP
while remaining_guesses != 0:
    print(f"You have {remaining_guesses} attempts remaining to guess the number.")
    guess = input_guess()
    if guess < SELECTED_NUMBER:
        print("Too low.")
        print("Guess again.")
        remaining_guesses-=1
    elif guess > SELECTED_NUMBER:
        print("Too high.")
        print("Guess again.")
        remaining_guesses-=1
    else:
        print("You guessed the number correctly!! You win!!")
        break
    if remaining_guesses == 0:
        print(f"The number was {SELECTED_NUMBER}, you failed to guess the number. You lose.")
        break



