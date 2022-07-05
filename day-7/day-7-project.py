import random
word_list = ["ardvaark", "baboon", "camel"]
lives = 6
chosen_word = word_list[random.randint(0, 2)]
result = ['_']*len(chosen_word)
won = False

while lives != 0:
    guess = input("Guess an alphabet in the chosen word: \n").lower()
    is_present = False
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            result[i] = guess
            is_present = True
    if is_present:
        print(
            f"You chose the alphabet {guess}. It is present in the chosen word")
    else:
        print(
            f"You chose the alphabet {guess}. It is present in the chosen word. Remaining life is {lives-1}")
        lives -= 1

    print(result)

    if '_' not in result:
        won = True
        break

if won:
    print("Congratulations you won the game.")
else:
    print("Sorry you lost the game")
