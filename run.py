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


def verify_user(f_name, password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credentials.check_user(f_name, password)
	return checking_user


def generate_password(Credentials):
	'''
	Function to generate a password automatically
	'''
	return Credentials.generate_password(Credentials)
 


def generate_password_six(Credentials):
    '''
	Function to generate a six letter password automatically
	'''
    return Credentials.generate_password_six(Credentials)


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

def credentials_exist(site_name):
    return Credentials.credentials_exist(site_name)

def display_accounts(site_name):
        '''
        method to display the credentials
        '''
        return Credentials.display_account(site_name)

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()



def copy_credentials(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credentials.copy_credentials(site_name)


def main():
        print('')
        print('Hello, Welcome to your password locker.')
        while True:
                print("-"*60)
                print("Use these short codes: cu - create a new user, log - login, ex -exit")
                short_code = input()


                if short_code == 'ex':
                           break

                if short_code == 'cu':
                   print("New Account")
                   print("-"*10)
                   f_name = input('Enter your first name - ').strip()
                   l_name = input('Enter Last name - ').strip()
                   password = input('Enter password -').strip()

                   save_user(create_user(f_name, l_name, password))

                   print("\n")
                   print(f'New Account: {f_name} {l_name} login password: {password}')
                elif short_code == 'log' :
                   print('\n')
                   print('To login, enter your first name as username and password:')
                   print('Enter first name/username')
                   print('-'*5)
                   f_name = input()
                   print('Enter Password')
                   print('-'*5)
                   password = str(input())
                   user_exists = verify_user(f_name, password)
                   if user_exists == f_name:
                      print("\n")
                      print(f'Welcome {f_name}. Please choose an option to continue.')
                      print('\n')
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
                                  print('Enter the site you want to save credentials for:')
                                  site_name = input()
                                  print('Enter user name:')
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
                                        save_credentials(create_credentials(site_name, account_user_name, password))
                                        print(f'Credential Created: Site Name: {site_name} - Account Name: {account_user_name} - Password: {password}')
                                        print('\n')
                                        break
                                      elif psw_choice == 'gp8':
                                        password = generate_password(Credentials)
                                        save_credentials(create_credentials(site_name, account_user_name, password))
                                        print(f'Credential Created: Site Name: {site_name} - Account Name: {account_user_name} - Password: {password}')
                                        print('\n')
                                        break
                                      elif psw_choice == 'gp6':
                                        new_password = generate_password_six(Credentials)
                                        save_credentials(create_credentials(site_name, account_user_name, new_password))
                                        print(f'Credential Created: Site Name: {site_name} - Account Name: {account_user_name} - Password: {new_password}')
                                        print('\n')
                                        break

                                      elif psw_choice == 'ex':
                                        break

                                      else:
                                        print('Oops! Wrong you,entered a wrong option. Try again.')

                              elif short_code == 'dc':
                                        print('Enter your site name')
                                        site_name = input()
                                        if credentials_exist(site_name):
                                           print(display_accounts(site_name))
                                           print('#'*30)
                                        else:
                                           print("Sorry....you do not have an account yet")

                              elif short_code == 'copy':
                                        print(' ')
                                        print('Enter the site name for the credential password to copy: ')
                                        chosen_site = input()
                                        copy_credentials(chosen_site)
                                        print('')


                   else:
                    print(' ')
                    print('Oops! Wrong details entered. Try again or Create an Account.')

                else:
                    print("-"*60)
                    print(' ')
                    print('Oops! Wrong option entered. Try again.')


if __name__ == '__main__':
    main()
