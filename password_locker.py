import random


class User:
  """
  Class that generates new instances of user
  """
  def __init__(self, user_name, password):
    self.user_name = user_name
    self.password = password