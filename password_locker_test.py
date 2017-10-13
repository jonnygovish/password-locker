import unittest

from password_locker import User, Credentials


class TestUser(unittest.TestCase):
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
class TestCredentials(unittest.TestCase):
    """
    Test that define test cases for credentials.
    """
    def setUp(self):
        """ 
        set up method to run before each test cases
        """
        self.new_credential = Credentials("facebook", "jon88")

    def test_init(self):
        """
        Test case to test if the object is initialized properly.
        """

        self.assertEqual(self.new_credential.account_name,"facebook")
        self.assertEqual(self.new_credential.account_password,"jon88")
    
    # def test_user_login(self):
    #     """
    #     Test case to test if we can find a user by password.
    #     """
    #     self.new_user.user_save()
    #     test_user = User("puppah","78945632","puppah@gmail.com")
    #     test_user.user_save()
    #     found_user = User.user_login("78945632")

    #     self.assertEqual(found_user.password,test_user.password)

    def tearDown(self):
        Credentials.credential_list = []

    def test_save_account(self):
        """
        Test case to test if the credential object is saved in to credential_list.
        """
        self.new_credential.save_account()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_save_multiple_account(self):
        """
        Test case to test if we can save multiple credential objects.
        """
        self.new_credential.save_account()
        test_account = Credentials("Twitter","tw89")
        test_account.save_account()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_account(self):
        """
        Test case to test if we can remove an account from credential list.
        """
        self.new_credential.save_account()
        test_credential = Credentials("instagram","4452ks")
        test_credential.save_account()

        self.new_credential.delete_account()

        self.assertEqual(len(Credentials.credential_list),1)

    def test_display_accounts(self):
        """
        Test case to test if lists of accounts are displayed.
        """
        self.assertEqual(Credentials.display_accounts(),Credentials.credential_list)
        



if __name__ == '__main__':
  unittest.main(verbosity = 2)

