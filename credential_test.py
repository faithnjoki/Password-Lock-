import unittest # Importing the unittest module
from credential import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for Credentials class behavior
    
    Args:
        unittest.TestCase: TestCase class that  helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_credentials = Credentials("Ig","Faith","easy1")
    def tearDown(self):
        '''
        tearDown does cleanup after every test case has run
        '''
        Credentials.credentials_list = []
    def test_init(self):
        '''
        Test initialization test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.app_name,"Ig")
        self.assertEqual(self.new_credentials.account_username,"Faith")
        self.assertEqual(self.new_credentials.account_password,"easy1")
    def test_save_credential(self):
        '''
        test case to check whether objects are saved to credential list
        '''
        self.new_credentials.save_logins()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_save_multi_accounts(self):
        '''
        test case to check if we can save multiple accounts
        '''
        self.new_credentials.save_logins()
        test_login = Credentials("Twitter","hello","123") #new login
        test_login.save_logins()
        self.assertEqual(len(Credentials.credentials_list),2)
    def test_delete_login(self):
        '''
        test case to test if we can delete credential object from our list
        '''
        self.new_credentials.save_logins()
        test_login = Credentials("Twitter","hello","123")
        test_login.save_logins()
        
        self.new_credentials.delete_logins()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_find_login_by_appName(self):
        '''
        test to check if we can retrieve username  by app name and display information
        '''
        self.new_credentials.save_logins()
        test_login = Credentials("Twitter","hello","123")
        test_login.save_logins()
        
        found_login = Credentials.find_by_appName("Twitter")
        self.assertEqual(found_login.account_username,test_login.account_username)
    def test_login_exists(self):
        '''
        test to check whether an object exists in a list
        '''
        self.new_credentials.save_logins()
        test_login = Credentials("Twitter","hello","123")
        test_login.save_logins()
        
        login_exists = Credentials.login_exists("Twitter","hello","123")
        self.assertTrue(login_exists)
    def test_show_login(self):
        '''
        method to return a list of all saved logins
        '''
        self.assertEqual(Credentials.display_logins(),Credentials.credentials_list)
if __name__ ==  '__main__':
    unittest.main()