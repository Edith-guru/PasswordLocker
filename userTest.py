import unittest
from user import user

class test_user(unittest.TestCase):
    
    # Test class that defines cases for the user class behaviours. 
    # Args:
    #     unittest.TestCase: TestCase class that helps in creating test cases 
    def setUp(self):
        
        # set up method to run before each test cases.
        
        self.new_user = user('Edith', 'Nekesa', '2022') #create conct object
    def test_init(self):
        
        # test_init test cast to test if the object is initialized properly
        
        self.assertEqual(self.new_user.user_name, 'Edith')
        self.assertEqual(self.new_user.password, '2022')
    def test_save_user(self):
        
        # test_save_user test case to test if the user object is saved into the user list
        
        self.new_user.save_user() #saving the new contact
        self.assertEqual(len(user.user_list),1)
    def test_delete_user(self):
        
        # test_delete_user to test if we can remove a contact from the contact list 
        
        self.new_contact.save_contact()
        test_user = user('Test', 'user', '0712345678', 'test@user.com') #new contact
        test_user.save_user()
        
        self.new_user.delete_user() #Deleting a contact object
        self.assertEqual(len(user.user_list),1)

if __name__ == '__main__':
    unittest.main()
    