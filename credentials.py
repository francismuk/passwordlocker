import pyperclip
import string
class Credentials:


        credentials_list = []  # Empty credentials list

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
        def find_by_user_name(cls, password):
                for credentials in cls.credentials_list:
                        if credentials.password == password:
                         return credentials

        @classmethod
        def credentials_exist(cls, password):
                for credentials in cls.credentials_list:
                        if credentials.password == password:
                         return True

                return False

        @classmethod
        def display_credentials(cls):
                return cls.credentials_list

        @classmethod
        def copy_user_name(cls, user_name):
                credentials_found = Credentials.find_by_user_name(user_name)
                pyperclip.copy(credentials_found.user_name)
