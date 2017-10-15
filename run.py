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
  new_credential = Credentials(account_name,account_password)
  return new_credential