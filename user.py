import random
import pyperclip
class User:
    
    user_list = []

    def __init__(self,f_name,l_name,password):
    
        self.f_name = f_name
        self.l_name = l_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into users list
        '''
        
        User.user_list.append(self)
    
#     def verify_user(self,f_name,password):
#         '''
#         Function that verifies the existance of the user before creating credentials
#         '''
    
# checking_user =
#         Credentials.check_user(f_name,password)
#         return checking_user
        
    @classmethod
    def find_by_password(cls,f_name,password):
        '''
        Method that takes the password
        Args:
            password: password to search for
        Returns:
            User
        '''
        current_user = ''
        for user in cls.user_list:
             if user.f_name == f_name and user.password == password:
                current_user = user.f_name
                return current_user
            
