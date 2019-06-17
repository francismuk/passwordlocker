import pyperclip
import string
import random
from user import User
class Credentials:
        password_list = []
        credentials_list = []  # Empty credentials list
        user_credentials_list = []

        
        def __init__(self, site_name, account_user_name, password):

         self.site_name = site_name
         self.account_user_name = account_user_name
         self.password = password

        def save_credentials(self):
                '''
                save_credentials method saves user objects into credentials list
                '''

                Credentials.credentials_list.append(self)
                
        def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
                '''
		Function to generate an 8 character password for a credential
		'''
                gen_pass=''.join(random.choice(char) for _ in range(size))
                return gen_pass

        def generate_password_six(size=6, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
                '''
		Function to generate an 6 character password for a credential
		'''
                gen_pass_six=''.join(random.choice(char) for _ in range(size))
                return gen_pass_six
        

        def delete_credentials(self):
                '''
                delete_credentials method deletes a saved credentials from the credentials_list
                '''

                Credentials.credentials_list.remove(self)

        @classmethod
        def find_by_account_user_name(cls, account_user_name):
                for credentials in cls.credentials_list:
                        if credentials.account_user_name == account_user_name:
                         return credentials

        @classmethod
        def credentials_exist(cls, password):
            for credentials in cls.credentials_list:
                    if credentials.password == password:
                        return True

            return False

        # @classmethod
        # def display_credentials(cls, f_name):
        #         '''
        #         Class method that displays list of  credentials saved
        #         '''
        #         user_credentials_list = []
        #         for credential in credential.credentials_list:
        #              if credential.f_name == f_name:
        #                 user_credentials_list.append(credential)
        #                 return user_credentials_list
                
        @classmethod
        def display_credentials(cls):
          return cls.user_credentials_list
        
        @classmethod
        def find_by_site_name(cls, site_name):
         for credentials in cls.credentials_list:
             if credentials.site_name == site_name:
                 return credentials
        @classmethod
        def password_exist(cls,account_user_name):
         for password in cls.password_list:
            if password.account_name == account_user_name:
                return True
            return False

        @classmethod
        def copy_credentials(cls, site_name):
            credentials_found = Credentials.find_by_site_name(site_name)
            return pyperclip.copy(credentials_found.password)
