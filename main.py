name = input('What is your name? ')
print(f'Hey {name}, Welcome to Pass Locker!')
master_pwd = input('What is you master password? ')

# add functions
def view():
  with open('password.txt', 'r') as f:
      for line in f.readlines():
          print(line)
    



view()

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    # with key word closes file  automatically once its open.
    with open('password.txt','a') as f:
        f.write(name + '|' + pwd + '\n')


add()



while True:
    Mode = input('Woould you want to view existing passwords or create new password or quit?(View or Add or  quit) ').lower()
    if Mode== 'quit':
        break
    elif Mode == 'view':
        view()
    elif Mode == 'add':
        add()
    else:
        print('Invalid mode')
        continue
