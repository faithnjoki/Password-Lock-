#!/usr/bin/env python3.6
from user import User
from credential import Credentials

def create_user(username,password):
    '''
    Function to create new user
    '''
    myUser = User(username,password)
    return myUser
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
def delete_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()
def find_by_number(username):
    '''
    Function to find user by the username
    '''
    return User.find_by_username(username)
def user_exists(username,password):
    '''
    Function to authenticate user
    '''
    return User.user_exists(username,password)
def display_user():
    '''
    Function to show all saved users
    '''
    return User.display_users()
def create_credentials(app_name,account_username,account_password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(app_name,account_username,account_password)
    return new_credentials
def save_logins(new_credentials):
    '''
    Functions to save logins
    '''
    new_credentials.save_logins()
def delete_logins(new_credentials):
    '''
    Function to delete credentials
    '''
    new_credentials.delete_logins()
def find_by_app_name(app_name):
    '''
    Function to check if an application exists
    '''
    return Credentials.find_by_appName(app_name)
def login_exits(app_name,account_username,account_password):
    '''
    Function to check whether a login exists
    '''
    return Credentials.login_exists(app_name,account_username,account_password)
def display_logins():
    '''
    Function that returns Login credentials for an app
    '''
    return Credentials.display_logins()
def generate_a_password(passwordLength):
    '''
    Function that generates random password of 8 characters
    '''
    return Credentials.generate_password(passwordLength)
def main():
    print('*'*10 + "Welcome to Password Locker" + '*'*10)
    print('--'*22)
    print('We are Here to manage your passwords')
    while True:
        session_user=input("Tell us your name\n")
        if session_user.strip().capitalize !='':
            print(f"\nHello {session_user},")
            while True:
                print
                my_code = input("Use these short codes for navigation: \n CA - Create an Account \n SI - Sign into an existing account \n DA - Delete your account \n EX - Exit ")

                if my_code.upper() == 'CA':
                    print("\nCREATE AN ACCOUNT")
                    print("-"*10)
                    print("Enter name to use as your username")
                    print(" "*4 + "*the username contains alphabetical letters only and no spaces*")
                    
                    while True:
                        username = input().capitalize()
                        if username.isalpha():
                            print("Enter a password for your account")
                            print(" "*4 + "*the password must be 6 characters or longer*")
                            while True:
                                password = input()
                                if len(password) >= 6:
                                    save_user(create_user(username,password))
                                    print(f"\nAccount for {username} has been successfully created.\nProceed to sign in.\n")
                                    break
                                else:
                                    print("\nThe password you entered is too short.")
                                    print("Please use a password of 6 characters or more.")
                                    continue
                        
                        else:
                            print("\nThe username you entered is not valid.")
                            print("Please use alphabetical letters only with no spaces.")
                            continue
                        break

                elif my_code == 'SI':
                    print("\nSIGN IN")
                    print("-"*10)

                    print("Enter your username")
                    username = input().strip(' ').capitalize()
                    print("Enter your password")
                    password = input().strip(' ')

                    if user_exists(username, password):
                        print("\nLog in successful")
                        print("What would you like to do?")

                        while True:
                            print("\nUse these short codes for navigation: \n CC: create new credentials \n FC: find a credential \n DC: delete a credential \n SC: see all credentials \n LO: log out")
                            credentials_navigation = input().upper()

                            if credentials_navigation == 'CC':
                                print("\nCREATE NEW CREDENTIALS")
                                print("-"*10)
                                while True:
                                    print("Application name:")
                                    print(" "*4 + "*eg. Instagram/Tinder*")
                                    app_name = input().capitalize().strip(' ')
                                    if app_name != '':
                                        print(f"What is your current/desired username on {app_name}?")
                                        account_username = input()

                                        while True:
                                            print(f"\nDo you already have a password for your account on {app_name}? (Y/N)")
                                            has_password = input().upper()
                                            if has_password == 'Y':
                                                print(f"Enter your {app_name} password")
                                                account_password = input()
                                                save_logins(create_credentials(
                                                    app_name, account_username, account_password))
                                                print(f"\nAccount credentials for your {app_name} account have been successfully saved.")
                                                break

                                            elif has_password == 'N':
                                                while True:
                                                    print("Would you like a generated password? (Y/N)")
                                                    gen_pass = input().upper()
                                                    if gen_pass == 'Y':
                                                        print("How long would you like your password to be?")
                                                        print(" "*4 + "less than 8 characters: WEAK" + "\n" + " "*4 + "8 characters: STRONG" + "\n" + " "*4 + "8-26 characters: VERY STRONG")
                                                        while True:
                                                            try:
                                                                passwordLength = int(input())
                                                                if passwordLength in range(27):
                                                                    account_password = generate_a_password(passwordLength)
                                                                    print(
                                                                        f"Password generated is {account_password}")
                                                                    save_logins(create_credentials(
                                                                        app_name, account_username, account_password))
                                                                    print(f"Account credentials for your {app_name} account have been successfully saved.\n")
                                                                    break
                                                            except ValueError:
                                                                print("\nYou did not pick a valid password length")
                                                                print("Please pick a number between 0-26 and try again")
                                                                continue
                                                    elif gen_pass == 'N':
                                                        print(
                                                            f"Enter a password you wish to use for your {app_name} account")
                                                        print(" "*4 + "*password must be longer than 6 characters*")
                                                        while True:
                                                            account_password = input()
                                                            if len(account_password) >= 6:
                                                                save_logins(create_credentials(
                                                                    app_name, account_username, account_password))
                                                                print(f"Account credentials for your {app_name} have been successfully saved.\n")
                                                                break
                                                            else:
                                                                print("\nThe password you entered is too short.")
                                                                print("Please use a password of 6 characters or more.")
                                                                continue
                                                    else:
                                                        print("You did not select a valid option")
                                                        print("Please enter (Y/N) and try again")
                                                        continue
                                                    break
                                            
                                            else:
                                                print("You did not select a valid option")
                                                print("Please enter (Y/N) and try again")
                                                continue

                                            break
                                        break
                                    else:
                                        print("\nSorry, I didn't quite get the application name. Please try again.")
                                        continue

                            elif credentials_navigation == 'FC':
                                if len(Credentials.credentials_list) >= 1:
                                    print("\nFIND CREDENTIALS")
                                    print("-"*16)
                                    print("Enter the application whose credentials you'd like to find:")
                                    print(" "*4 + "*eg. Instagram/Tinder*")
                                    searched_application = input().capitalize()

                                    if login_exits(searched_application):
                                        searched_credential = login_exits(searched_application)
                                        print(f"\nApplication name: {searched_credential.app_name}, \n username: {searched_credential.account_username} \n password: {searched_credential.account_password}")

                                    else:
                                        print(f"\nThe credentials for {searched_application} don't exist.")

                                    continue

                                else:
                                    print("\nYou don't seem to have any credentials saved.")
                                    continue

                            elif credentials_navigation == 'DC':
                                if len(Credentials.credentials_list) >= 1:
                                    print("\nDELETE CREDENTIALS")
                                    print("-"*18)
                                    print("Application name:")
                                    print(" "*4 + "*eg. Instagram/Tinder*")
                                    app_name = input().capitalize()
                                    
                                    if login_exits(app_name):
                                        while True:
                                            print(f"Are you sure you want to delete credentials for your {app_name}? (Y/N)")
                                            delete_credential = input().upper()
                                            if delete_credential == 'Y':
                                                delete_logins(delete_logins(app_name))
                                                print(f"\nCredentials for {app_name} have been successfully deleted")
                                                break
                                            elif delete_credential == 'N':
                                                print("\nPhew! Your credentials are still intact.")
                                                break
                                            else:
                                                print("You did not select a valid option")
                                                print("Please enter (Y/N) and try again\n")
                                                continue
                                    
                                    else:
                                        print(f"\nCredentials for {app_name} don't exist.")
                                        continue

                                else:
                                    print("\nYou don't seem to have any credentials saved.")
                                    continue

                            elif  credentials_navigation == 'SC':
                                if len(Credentials.credentials_list) >= 1:
                                    display_logins
                                    print("\nHERE ARE ALL YOUR CREDENTIALS")
                                    print("-"*29)
                                    for credential in display_logins():
                                        print(f"\nApplication name: {credential.app_name} \n Username: {credential.account_username} \n Password: {credential.account_password}")
                                    continue
                                else:
                                    print("\nYou don't seem to have any credentials saved.")
                                    continue

                            elif  credentials_navigation == 'LO':
                                print("\nYou have successfully logged out..\n")
                                break
                    
                            else:
                                print("\nYou did not select a valid option.")
                                print("Please try again.")
                                continue

                    else:
                        print("\nInvalid username and password")
                        print("Try again or create an account\n")
                        continue
                
                elif my_code == 'DA':
                    if len(User.users_list) >= 1:
                        print("\nDELETE YOUR ACCOUNT")
                        print("-"*19)
                        print("Enter your username")
                        username = input().capitalize()
                        print("Enter your password")
                        login_password = input()

                        if user_exists(username, login_password):
                            while True:
                                        print(f"Are you sure you want to delete your account? (Y/N)")
                                        delete_account = input().upper()
                                        if delete_account == 'Y':
                                            delete_user(find_by_number(username))
                                            print(f"\nYour account has been successfully deleted.\n")
                                            break
                                        elif delete_account == 'N':
                                            print("\nPhew! Your account is still active.\n")
                                            break
                                        else:
                                            print("You did not select a valid option")
                                            print("Please enter (Y/N) and try again")
                                            continue

                        else:
                            print("\nSeems like you do not have an active account or you entered the wrong details.")
                            print("Please try again.\n")
                            continue

                    else:
                        print("\nSorry, there are no active accounts at the moment.\n")
                        continue

                elif my_code == 'EX':
                    print("\nBye....")
                    break

                else:
                    print("\nYou did not select a valid option.")
                    print("Please try again.\n")
                    continue

        else:
            print("\nSorry, I didn't quite get your name. Please try again")
            continue
        
        break
if __name__ == '__main__':
    main()
            
