print('Welcome to the bid handler')
bids = {}
while True:
    name = input('what is your name? ')
    bid = int(input('what is your bid? $'))
    bids[name] = bid
    yesno = input('Are there more bidders? (yes/no) ').lower()
    if 'n' in yesno:
        break
    
max_bid = -1
winner = ""
for k,v in bids.items():
    if v > max_bid:
        winner = k
        max_bid = v
print(f'The winner is {winner} with ${max_bid}')