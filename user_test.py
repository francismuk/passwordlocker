import unittest
from user import User


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
        
        self.new_user = User("Francis", "Mukuha", "1234")# create login credentials
        
    def test_init(self):
        
        '''
        test_init test case to test if the object is initialized properly
        
        '''

        self.assertEqual(self.new_user.f_name, "Francis")
        self.assertEqual(self.new_user.l_name, "Mukuha")
        self.assertEqual(self.new_user.password, "1234")

