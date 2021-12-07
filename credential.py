import random
import string

class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = []

    def __init__ (self, app_name, account_username, account_password):
        '''
        __init method that helps us define properties for our objects
        Args:
        app_name: New app name
        account_username: New account username
        account_password: New account password
        '''
        self.app_name = app_name
        self.account_username = account_username
        self.account_password = account_password
    def save_logins(self):
        '''
        save method to append credential objects to the credential list
        '''
        Credentials.credentials_list.append(self)
    def delete_logins(self):
        '''
        method to delete credential object
        '''
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_by_appName(cls,app_name):
        '''
        Method that takes in a application name and return a string that matches that name

        Args:
            appName: appName to search for
        Returns :
            matching account username
        '''
        for login in cls.credentials_list:
            if login.app_name == app_name:
                return login
    @classmethod
    def login_exists(cls,app_name,account_username,account_password):
        '''
        method checks if login exits from the credential list
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for login in cls.credentials_list:
            if login.app_name == app_name and login.account_username == account_username and login.account_password == account_password:
                return True
        return False
    @classmethod
    def display_logins(cls):
        '''
        method that returns login list
        '''
        return cls.credentials_list
    @staticmethod
    def generate_password(passwordLength):
        '''
        method that generates a random password for the user
        '''
        random_alphanumeric = string.ascii_letters + string.digits
        password = ''.join((random.choice(random_alphanumeric) for i in range(passwordLength)))
        return password