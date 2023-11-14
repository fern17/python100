import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print('Welcome to the Number guessing Game')
print('I am thinking of a number between 1 and 100')
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempts = EASY_LEVEL_TURNS if difficulty == 'easy' else HARD_LEVEL_TURNS
secret_number = random.randint(1, 100)

while attempts > 0:
    num = int(input('Make a guess: '))
    if num == secret_number:
        print('You won')
        break
    elif num < secret_number:
        print('Too low')
    else:
        print('Too high')
    attempts -= 1
    print(f'You have {attempts} attempts remaining')