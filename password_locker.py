import random

user_name =""
user_password =""

class User:
  """
  Class that generates new instances of user
  """
  global user_name
  global user_password
  user_list = []
  def __init__(self, user_name, password,email):
    self.user_name = user_name
    self.password = password
    self.email = email
  
  def user_save(self):
    """
    saves user object into user object.
    """
    User.user_list.append(self)


class Credentials:
  """
  Class that generates new instances of credential object.
  """
  
