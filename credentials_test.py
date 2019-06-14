import unittest #Import unittest module
import pyperclip
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    
    '''
    Test class that defines test cases for the credentials class behaviours
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("James","123456") # create credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.user_name,"James")
        self.assertEqual(self.new_credentials.password,"123456")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.credentials_list),1)
        
    # def tearDown(self):
    #     '''
    #     tearDown method that does clean up after each test case has run.
    #     '''
    #     Credentials.credentials_list = []
        
    # def test_save_multiple_credentials(self):
    #         '''
    #         test_save_multiple_credentials to check if we can save multiple credentials
    #         objects to our credentials_list
    #         '''
    #         self.new_credentials.save_credentials()
    #         test_credentials = Credentials("James","123456") # new contact
    #         test_credentials.save_credentials()
    #         self.assertEqual(len(Credentials.credentials_list),2)
            
    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("James","123456") # new contact
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a contact object
            self.assertEqual(len(Credentials.credentials_list),1)
      
    def test_find_contact_by_user_name(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("James","123456") # new contact
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_user_name("James")
        self.assertEqual(found_credentials.user_name, test_credentials.user_name)      
    # def test_credentials_exists(self):
    #     '''
    #     test to check if we can return a Boolean  if we cannot find the credentials.
    #     '''

    #     self.new_credentials.save_credentials()
    #     test_credentials = Credentials("James","123456") # new contact
    #     test_credentials.save_credentials()

    #     credentials_exists = Credentials.credentials_exist("123456")

    #     self.assertTrue(credentials_exists)
        
    # def test_copy_user_name(self):
    #     '''
    #     Test to confirm that we are copying the credde
    #     '''
    #     self.new_credentials.save_credentials()
        
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_user_name(self):
        '''
        Test to confirm that we are copying the username from a found credential
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_user_name("James")

        self.assertEqual(self.new_credentials.user_name,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
