first = float(input('First number: '))

while True:
    op = input('Operation? (+,-,*,/): ')
    if op not in '+-*/':
        print('Operation invalid, retry')
    else:
        break

second = float(input('Second number: '))

operations = {
    "+": lambda f, s: f + s, 
    "-": lambda f, s: f - s, 
    "*": lambda f, s: f * s, 
    "/": lambda f, s: f / s, 
}

print(operations[op](first, second))
