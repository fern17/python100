print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
direction = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\": ").lower()
if direction == "left":
    swim = input("There is a river. Do you want to \"swim\" or \"wait\": ").lower()
    if swim == "wait":
        door = input("You see a group of doors. Do you open the \"red\", \"blue\" or \"yellow\" one?: ").lower()
        if door == "yellow":
            print("You found the treasure! You are rich. You win")
        elif door == "red" or door == "blue":
            print("Fire! You lost. Game over")
        else:
            print("Unknown door, a crocodile ate you. Game over")
    elif swim == "swim":
        print("You drowned, bad luck. Game over")
    else:
        print("Don't know what to do. A crocodile ate you. Game over")
elif direction == "right":
    print("You fell into a hole. Game over")
else:
    print("Unknown direction. Game over")
