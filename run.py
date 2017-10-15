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
def display_users():
   return User.display_users()
  

def login_user(user_name,password):
  """
  function that checks whether a user exist and then login the user in.
  """
  check_user_exist = Credentials.check_user_exist(user_name,password)
  return check_user_exist

def create_credential(account_name,account_username, account_password):
  """
  Function to create a new credential.
  """
  new_credential = Credentials(account_name,account_username,account_password)
  return new_credential

def save_credential(credential):
  """
  Function to save new  credential.
  """
  credential.save_account()

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

def main():
  print("Welcome to password locker")
  print('\n')
  while True:
    short_code = input("Use this short codes: cu- create a new user account, ln - login into your account (if you already have a password locker account), ex - exit from password locker \n").lower()
    
    if short_code == "ex":
        print("Come back again.......Goodbye!!")
        break
    
    elif short_code == "cu":
        print("Sign Up")
        print('-' * 30)
        user_name = input("User_name: ")
        password = input("Password: ")
        email = input("Email: ")
        
        save_user(create_user(user_name,password,email))
        print('\n')
        
        print(f"Hello,{user_name} your account has been created")
        print('\n')
        print('-' * 30)
        
    elif short_code == "d":
        if display_users():
            print("Here's a list of the users")
            print('\n')
            for user in display_users():
                print(f"{user.user_name}")
                print('\n')
        else:
            print("There's no users saved yet")
                
        
    elif short_code == "ln":
        print("Please Enter your User name and your Password to log in")
        print('-' * 30)
        user_name = input("User name: ")
        password = input("password: ")
        sign_in = login_user(user_name,password)
        if sign_in == True:
            print(f"Hey,{user_name}. What would you like to do?")
            while True:
                break
                
        else:
            print("Ooops!You dnt have an account with us.Please create an account to proceed")
            
#    break
    



if __name__ == '__main__':
  main()