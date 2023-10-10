from random import randint
choice_str = input("What do you choose ? 1 for Rock, 2 for Paper, 3 for Scissors: ")
user_choice = 0
if choice_str == "1":
    user_choice = 1
elif choice_str == "2":
    user_choice = 2
elif choice_str == "3":
    user_choice = 3
else:
    print("Unknown choice. Defaulting to Rock")
    user_choice = 1

computer_choice = randint(1, 3)
computer_choice_str = ["Rock", "Paper", "Scissors"]

print(f"The computer choose {computer_choice_str[computer_choice-1]}")

if computer_choice == user_choice:
    print("This is a draw")
elif ((computer_choice == 1 and user_choice == 2) or
   (computer_choice == 2 and user_choice == 3) or
   (computer_choice == 3 and user_choice == 1)):
    print("The user won!")
else:
    print("The computer won")