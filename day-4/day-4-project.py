import random

print("Welcome to python Rock Paper Scissor!!")

plays = ['Rock', "Paper", 'Scissor']

your_play = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissor: "))

computer_play = random.randint(0, 2)


print(f"You played {plays[your_play]}.")
print(f"Computer played {plays[computer_play]}")

if your_play == 1 and computer_play == 0:
    print("You Win")
elif your_play == 1 and computer_play == 2:
    print("You Lost")
elif your_play == 0 and computer_play == 1:
    print("You Lost")
elif your_play == 0 and computer_play == 2:
    print("You Win")
elif your_play == 2 and computer_play == 0:
    print("You Lost")
elif your_play == 2 and computer_play == 1:
    print("You Win")
else:
    print("The match is a draw")
