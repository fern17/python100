import random

card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    else:
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(random.choice(card_values))
    computer_cards.append(random.choice(card_values))

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f'User score: {user_score}, {user_cards}')
#print(f'Computer points: {cp}')
    
should_continue = True
while should_continue:
    yesno = input('Do you want another card? ').lower()
    if 'y' in yesno:
        user_cards.append(random.choice(card_values))
    else:
        should_continue = False
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(card_values))
        computer_score = calculate_score(computer_cards)
    print(f'User score: {user_score}, {user_cards}')


print('Finished')
print(f'User hand: {user_score}, {user_cards}')
print(f'Computer hand: {computer_score}, {computer_cards}')
if computer_score == user_score and user_score < 21:
    print('Draw')
elif user_score == 0:
    print('You won with Black Jack')
elif computer_score == 0:
    print('Computer won with Black Jack')
elif user_score > 21:
    print('Computer won because you went over 21')
elif computer_score > 21:
    print('You won because computer went over 21')
elif user_score > computer_score:
    print('You won')
else:
    print('Computer won')