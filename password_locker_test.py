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
        self.new_user = User("jgovish", "12345", "jgovish@gmail.com")
    def test_init(self):
        """
        Test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name,"jgovish")
        self.assertEqual(self.new_user.password, "12345")
        self.assertEqual(self.new_user.email, "jgovish@gmail.com")

    def tearDown(self):
        """
        Method that cleans up after each case has run.
        """
        User.user_list = []

    def test_user_save(self):
        """
        Test case to test if the user object is saved into the user_list.
        """
        self.new_user.user_save()
    
        self.assertEqual(len(User.user_list),1)
    def test_save_multiple_user(self):
        """
        Test to check whether we can save multiple user objects.
        """
        self.new_user.user_save()
        test_user = User("puppah","78945632","puppah@gmail.com")
        test_user.user_save()
        self.assertEqual(len(User.user_list),2)


if __name__ == '__main__':
  unittest.main(verbosity =2)

