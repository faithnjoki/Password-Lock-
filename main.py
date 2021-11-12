name = input('What is your name? ')
print(f'Hey {name}, Welcome to Pass Locker!')

# add functions
def view():
    pass
def add():
    pass




while True:
    Mode = input('Woould you want to view existing passwords or create new password or quit?(View or Add or  quit) ').lower()
    if Mode== 'quit':
        break
    elif Mode == 'view':
        pass
    elif Mode == 'add':
        pass
    else:
        print('Invalid mode')
        continue
