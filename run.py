#!/usr/bin/env python3.6

from password_locker import User, Credentials

def create_user(user_name, password, email):
  """
  Function to create a new user.
  """
  new_user = User(user_name,password, email)
  return new_user

def save_user(user):
  """
  Function to save user.
  """
  user.user_save()

def create_credential(account_name, account_password):
  """
  Function to create a new credential.
  """
  new_credential = Credentials(account_name,account_username,account_password)
  return new_credential

def save_credential(credential):
  """
  Function to save new  credential.
  """
  Credentials.save_account()

def delete_account(credential):
  """
  Function to delete a credential.
  """
  Credentials.delete_account()

def dislplay_account():
  """
  Function that returns all the saved credential.
  """
  return Credentials.display_accounts()

def generate_password():
  """
  Function that generates random password.
  """
  password_gen = Credentials.generate_password()

  return password_gen
