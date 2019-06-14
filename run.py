#!/usr/bin/env python3.6
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
    
# def find_user(user_name):
#     '''
#     Function that finds a contact by number and returns the contact
#     '''
#     return user.find_by_user_name(user_name)

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

def find_credentials(user_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_by_user_name(user_name)

def display_contacts():
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
        print("Use these short codes: cc - create a new user, dc - display users, fc -find a user, ex -exit the users list ")
    
    
if __name__ == '__main__':
    main()