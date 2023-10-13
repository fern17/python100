import string
import random

print("Welcome to the PyPassword Generator!\n")
count_letters = int(input("How many letters would you like in your password? "))
count_symbols = int(input("How many symbols would you like in your password? "))
count_numbers = int(input("How many numbers would you like in your password? "))

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['$', '?', ';', ':', '!', '@', '#', '(', ')']

generated_password = []
for i in range(0, count_letters):
    generated_password += random.choice(letters)
for i in range(0, count_symbols):
    generated_password += random.choice(numbers)
for i in range(0, count_numbers):
    generated_password += random.choice(symbols)

random.shuffle(generated_password)
password = ""
password = password.join(generated_password)

print(f"Your new password is {password}")
