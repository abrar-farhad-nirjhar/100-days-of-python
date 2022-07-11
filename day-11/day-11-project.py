import random


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4

already_picked = []

your_initial_cards = []

computer_initial_cards = []

def populate_cards():
    while len(your_initial_cards)<2:
        idx = random.randint(0,51)

        if idx not in already_picked:
            your_initial_cards.append(cards[idx])


    while len(computer_initial_cards)<2:
        idx = random.randint(0,51)

        if idx not in already_picked:
            computer_initial_cards.append(cards[idx])
            
while True:
    populate_cards()
    while True:
        print(f"Your cards: {your_initial_cards}")
        print(f"Computer's first card: {computer_initial_cards[0]}")
        choice = input("Do you want to get another card? y/n: ")

        if choice == 'y':
            while True:
                idx = random.randint(0,51)
                if idx not in already_picked:
                    your_initial_cards.append(cards[idx])
                    break

            print(f"Your current hand: {your_initial_cards}")
            if sum(your_initial_cards) == 21:
                print("You Win")
                break
            if sum(your_initial_cards) >21:
                print(f"Sum of your initial cards is {sum(your_initial_cards)}. You lose.")
                break
        
        else:
            print(f"Computers hand: {computer_initial_cards}")
            print(f"Your Hand: {your_initial_cards}")

            if 21 - sum(your_initial_cards) < 21 - sum(computer_initial_cards):
                print("You Win!")
            elif sum(your_initial_cards) == sum(computer_initial_cards):
                print("Computer Wins!")
            break
    choice = input("Would you like to play another round of blackjack? y/n: ")
    if choice=='y':
        your_initial_cards = []
        computer_initial_cards = []
        already_picked = []
    else:
        break
