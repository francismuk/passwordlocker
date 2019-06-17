import unittest
import random
from user import User
from credentials import Credentials


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User("Francis", "Mukuha", "1234") # create login credentials

    
        
    def test_init(self):
        
        '''
        test_init test case to test if the object is initialized properly
        
        '''

        self.assertEqual(self.new_user.f_name, "Francis")
        self.assertEqual(self.new_user.l_name, "Mukuha")
        self.assertEqual(self.new_user.password, "1234")
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the user has been saved inti the credentials list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
        
    def tearDown(self):
        '''
        teardown method that does clean up after each test case has run
        '''
        User.user_list = []


if __name__ == "__main__":
    unittest.main()
        

