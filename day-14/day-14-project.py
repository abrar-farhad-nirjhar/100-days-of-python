import random
import os
from game_data import data


clear = lambda: os.system('clear')


def get_single_data():
    return data[random.randint(0, len(data)-1)]

def versus(data_a, data_b):
    print("Whos has more followers?")
    print(f"{data_a['name']}, {data_a['description']} from {data_a['country']}")
    print("VS")
    print(f"{data_b['name']}, {data_b['description']} from {data_b['country']}")

def check_answer(data_a, data_b, answer):
    if answer == "A":
        return data_a['follower_count'] > data_b['follower_count']
    else:
        return data_b['follower_count'] > data_a['follower_count']
def get_guess(data_a, data_b):
    return input(f"Enter 'A' for {data_a['name']} or 'B' for {data_b['name']}: ")

def game():
    still_playing = True
    current_score = 0
    data_a = get_single_data()
    data_b = get_single_data()
    while still_playing:
        clear()
        if current_score > 0:
            print(f"Correct! Your current score is : {current_score}")
            data_b = get_single_data()        
        versus(data_a, data_b)
        guess = get_guess(data_a, data_b)

        if not check_answer(data_a, data_b, guess):
            clear()
            print(f"Sorry, that's wrong. Final score: {current_score}")
            still_playing = False
        else:
            current_score +=1
            data_a = data_b

if __name__ == "__main__":
    game()




