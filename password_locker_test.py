import unittest

from password_locker import User


class TestPassword_locker(unittest.TestCase):
  """
  Test that defines test cases for the user class bevaviours
  """
  
  def setUp(self):
   """
   set up method to run before each test cases
   """
   self.new_user = User("jgovish", "12345")

  def test_init(self):
   """
   Test case to test if the object is initialized properly
   """
   self.assertEqual(self.new_user.user_name,"jgovish")
   self.assertEqual(self.new_user.password, "12345")

   def test_user_save(self):
    """
    Test case to test if the user object is saved into the user_list.
    """
    self.new_user.user_save()

    self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
  unittest.main()

