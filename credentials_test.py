import unittest #Import unittest module
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    
    '''
    Test class that defines test cases for the credentials class behaviours
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("App","password") # create credentials object
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.user_name,"James")
        self.assertEqual(self.new_credentials.password,"0712345678")
    
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("James","0712345678") # new contact
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)
            
    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("user","0712345678") # new contact
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a contact object
            self.assertEqual(len(Credentials.credentials_list),1)
            
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("user","0711223344") # new contact
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("0711223344")

        self.assertTrue(credentials_exists)


if __name__ == '__main__':
    unittest.main()
