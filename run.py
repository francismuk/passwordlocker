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

def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()
    
def del_contact(contact):
    '''
    Function to delete a contact
    '''
    contact.delete_contact()
