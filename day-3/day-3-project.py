print("Welcome to the python Treasure Island Game.")

direction_input = input(
    "You are at a crossroads, do you want to go left or right? ").lower()

if direction_input == "right":
    print("You've entered an unending desert. Game Over.")
else:
    will_swim = input(
        "You came across a river, would you like to swim or wait for a boat? ").lower()
    if will_swim == "swim":
        print("You were eaten by a crocodile. Game Over")
    else:
        chosen_door = input(
            "You crossed the river and came across three doors with the colors red, blue and green. Which door do you choose? ").lower()

        if chosen_door == "red":
            print("You walked into a room which is filled with fire. Game Over.")
        elif chosen_door == "blue":
            print("You walked into a room occupied by a hungry tiger. Game Over.")
        else:
            print("Congratulations!! You have found the treasure!!")
