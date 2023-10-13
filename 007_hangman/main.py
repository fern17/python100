import random
import string

word_list = ["rat", "shark", "lion"]
secret_word = random.choice(word_list)

lives = len(secret_word)
current_word = ["_"] * lives

historic = []
while True:
    if lives == 0:
        print(f"You lose, the word was \"{secret_word}\"")
        break
    elif "_" not in current_word:
        print(f"You won! The word was \"{secret_word}\"")
        break
    else:
        print(f"{current_word}\n")
        letter = input("Guess a letter: ").lower()
        if historic.count(letter) != 0:
            print("You already picked that letter\n")
        else:
            historic.append(letter)
            did_replace = False
            for l in range(0, len(secret_word)):
                if secret_word[l] == letter:
                    current_word[l] = letter
                    did_replace = True
            if not did_replace:
                lives -= 1
                print(f"Letter not found. You lose one live. You have {lives} remaining\n")

