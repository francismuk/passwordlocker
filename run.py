#!/usr/bin/env python3.6
import pyperclip
import random
from user import User
from credentials import Credentials


def create_user(f_name, l_name, password):
    '''
    Function to create a new contact
    '''
    new_user = User(f_name, l_name, password)
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


def verify_user(first_name, password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credentials.check_user(f_name, password)
	return checking_user


def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credentials.generate_password()
	return gen_pass


def generate_password_six():
	'''
	Function to generate a six letter password automatically
	'''
	gen_pass_six = Credentials.generate_password_six()
	return gen_pass_six


def create_credentials(site_name, user_account_name, password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(site_name,user_account_name, password)
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
    return Credentials.display_credentials(account_user_name)

def copy_credentials(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credentials.copy_credentials(account_user_name)


def main():
    print("Hello, Welcome to your password locker. What is your First name?")
    print(f"Hello {f_name}What would you like to do?")
    print('\n')
    while True:
        print("Use these short codes: cu - create a new user, du - display users, fc -find a user, ex -exit the users list ")
short_code = input()


while short_code == 'ex':
        break

if short_code == 'cu':
        print("New Account")
        print("-"*10)

        print("First Name ...")
f_name = input()

print("Last Name ...")
l_name = input()

print("Enter password")
password = input()

save_user(create_user(f_name, l_name, password))

print("\n")
print(f'New Account: {f_name} {l_name} login password: {password}')
if short_code == 'du' :
	print('\n')
	print('To login, enter your first name and password:')
	f_name = input()
	password = str(input())
	user_exists = verify_user(f_name, password)
if user_exists == f_name:
        print(" ")
        print(f'Welcome {f_name}. Please choose an option to continue.')
        print(' ')
        while True:
                print("-"*60)
                print('\n')
                print('Navigation codes: cc-Create a Credential, dc-Display Credentials, copy-Copy Password, ex-Exit')
                short_code = input()
                print("-"*60)
                if short_code == 'ex':
                        print(" ")
                        print(f'Successfully logged out from account {f_name}')
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
                        save_credentials(create_credentials(
                                site_name, account_user_name, password))

                        print(
                                f'Credential Created: Site Name: {site_name} - Account Name: {account_user_name} - Password: {password}')
                        print(' ')
                elif short_code == 'dc':

                        if display_credentials(f_name):
                                print('Here is a list of all your credentials with passwords')

                                for credentials in display_credentials(f_name):
                                        print(f'Site Name: {credentials.site_name} - Account Name: {credentials.account_user_name} - Password: {credentials.password}')
                                print(' ')
                        else:
                                print(' ')
                                print("No credentials saved yet. Use code cc to create credentials")
                                print(' ')
                elif short_code == 'copy':
                        print(' ')
                        print('Enter the site name for the credential password to copy: ')
                        chosen_site = input()
                        copy_credentials(chosen_site)
                        print('')
                else:
                        print('Oops! Wrong option entered. Try again.')

else:
        print(' ')
        print('Oops! Wrong details entered. Try again or Create an Account.')

                # else:
                #         print("-"*60)
                #         print(' ')
                #         print('Oops! Wrong option entered. Try again.')


if __name__ == '__main__':
    main()
