#!/usr/bin/env python3.6
import pyperclip
from user import User
from credentials import Credentials

def create_user(f_name,l_name,password):
    '''
    Function to create a new contact
    '''
    new_user = User(f_name,l_name,password)
    return new_user

def save_user(user):
    '''
    Function to save contact
    '''
    user.save_user()
    
def del_user(user):
    '''
    Function to delete a contact
    '''
    user.delete_user()
    
def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def generate_password_six():
	'''
	Function to generate a six letter password automatically
	'''
	gen_pass_six = Credential.generate_password_six()
	return gen_pass_six


def create_credentials(user_name,password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(user_name,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()
    
def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Hello, Welcome to your password locker. What is your First name?")
    f_name = input()
    print("Enter Last name")
    l_name = input()
    print(f"Hello {f_name}What would you like to do?")
    print('\n')
    while True:
        print("Use these short codes: cu - create a new user, du - display users, fc -find a user, ex -exit the users list ")
        short_code = input().lower()
if short_code == 'ex':
        break

elif short_code == 'cu':
                        print("New Account")
                        print("-"*10)

                        print("First Name ...")
			f_name = input()
			
                        print("Last Name ...")
                        l_name = input()
                        
                        print("Enter password")
			password = input()

			save_user(create_user(first_name,last_name,password))
   
			print("\n")
			print(f'New Account: {first_name} {last_name} login password: {password}')
elif short_code == 'du':
			print('\n')
			print('To login, enter your first name and password:')
			f_name = input()
			password = str(input())
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
                                        print('\n')
					print('Navigation codes: cc-Create a Credential, dc-Display Credentials, copy-Copy Password, ex-Exit')
					short_code = input()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Successfully logged out from account {user_name}')
						break
					elif short_code == 'cc':
						print('Enter your accout details:')
						site_name = input()
						account_user_name = input()
						while True:
							print("-"*60)
                                                        print('\n')
							print('Please choose an option for entering a password: ep-enter existing password, gp8-generate 8 digit password, gp6-generate 6 digit password ,ex-exit')
							psw_choice = input()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp8':
								password = generate_password()
								break
                                                        elif psw_choice == 'gp6':
								password = generate_password_six()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong you,entered a wrong option. Try again.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_credential(chosen_site)
						print('')
					else:
						print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
else:
			print("-"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again.')
        
    
if __name__ == '__main__':
    main()