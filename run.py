import random
from user import User

def main():
    while True:
        print('Welcome to my PassWord Locker....' )
        print('\n')
        print('Please select a short code to navigate through the options: use nu for new user,lg for login and ex for exit: ')
        shortcode = input().lower()
        print('\n')
        if shortcode == 'nu':
            print('Create username: ')
            createdusername = input()

            print('Confirm Password: ')
            cornfirmpassword = input()


        


     


if __name__ == "__main__":
    main()
