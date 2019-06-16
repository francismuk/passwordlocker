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
			
    
if __name__ == '__main__':
    main()