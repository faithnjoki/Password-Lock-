import random
from user import User
import random
import string

def main():
    while True:

        print('Welcome to my PassWord Locker....' )
        name = input('What is your name?  ')
        print(f'Hey , {name}, Please select a short code to navigate through the options: use nu for new user,lg for login and ex for exit: ')
        shortcode = input().lower()
        if shortcode == 'nu':
            print('Create username: ')
            createdusername = input()

            print('Create Password: ')
            length = int(input('\nEnter the length of password: '))
            lower = string.ascii_lowercase
            upper = string.ascii_uppercase
            num = string.digits
            symbols = string.punctuation
            all = lower + upper + num + symbols
            temp = random.sample(all, length)
            createdpassword = "".join(temp)
            all = string.ascii_letters + string.digits + string.punctuation
            createdpassword = "".join(random.sample(all, length))
            print(createdpassword)
            createdpassword = input()

            print('Confirm Password: ')
            confirmpassword = input()

            while confirmpassword!=createdpassword:
                print('Invalid Password')
                print('Enter your Password; ')
                createdpassword = input()
                print('Confirm Password: ')
                confirmpassword = input()
            else:
                print(f'Congatulations {createdusername}! account creation was successful')
                print('Please, Proceede to login')
                print('Username: ')
                enteredusername = input()
                print('Enter your password: ')
                enteredpassword = input()
            while enteredusername != createdusername or enteredpassword != createdpassword:
                print('Invalid username or password')
                print('Enter username: ')
                enteredusername = input()
                print('Entered password: ')
                enteredpassword = input()
            else:
                print(f'Welcome {enteredusername} to your account')
                print('\n')

        elif shortcode == 'lg':
            print('Welcome')
            print('Enter Your username: ')
            defaultUsername = input()
            print('Enter Your Password: ')
            defaultpassword = input()
            print('/n')
            while defaultUsername != 'Faith' or defaultpassword !='leonbaby':
                print("wrong user name or password . username:'Faith' password:'leonbaby'")
                print('Enter username: ')
                defaultUsername = input()

                print('Enter password: ')
                defaultpassword = input()
               
            else:
                print('Login sucess')
        elif shortcode == 'ex':
            break
        else:
            print('Enter Valid code to continue')  


if __name__ == "__main__":
    main()
