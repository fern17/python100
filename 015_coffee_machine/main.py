
resources = {
    'water': 1000,
    'milk': 2000,
    'coffee': 1000
}

class Drink:
    def __init__(self, name, coffee, water, milk, ):
        self.name = name
        self.coffee = coffee
        self.water = water
        self.milk = milk

drinks = { 
    'expresso': Drink(name='expresso', coffee=50, water=100, milk=0), 
    'latte': Drink(name='latte', coffee=25, water=50, milk=100),
    'cappuccino': Drink(name='cappuccino', coffee=35, water=50, milk=50)
}

def print_report():
    for k, v in resources.items():
        print(f'{k} = {v}')

def check_availability(drink):
    if resources['water'] < drink.water:
        print('Not enough water')
        return False
    elif resources['milk'] < drink.milk:
        print('Not enough milk')
        return False
    elif resources['coffee'] < drink.coffee:
        print('Not enough coffee')
        return False
    return True

def prepare_drink(drink):
    resources['coffee'] -= drink.coffee
    resources['milk'] -= drink.milk
    resources['water'] -= drink.water

def show_and_process_prompt():
    choice = input('What would you like? (expresso/latte/cappuccino): ')
    if choice == 'report':
        print_report()
    elif choice != 'expresso' and choice != 'latte' and choice != 'cappuccino':
        print('Unknown drink')
    elif check_availability(drinks[choice]):
        # TODO: all drinks are free for the moment, the user should pay for them
        prepare_drink(drinks[choice])
        print('There you are')
        print_report()

print('Welcome to the coffee machine')
show_and_process_prompt()