# import random
# import string

class User:
    
    # generates new instances of users
    
    userslist = []
    def __init__(self,firstname,lastname,username,password):
        
        # __init__ method helps us define properties for our objectsself.
        
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
    def save_user(self):
        
        #save_user method saves the user info to userlist using the append method
        User.userslist.append(self)
    def delete_user(self):
        
        #  delete_user method deletes a saved user from the userlist
        User.userslist.remove(self)
    @classmethod
    def display_users(cls):
        
        # method that returns info from the userlist
        
        return cls.userslist
    @classmethod
    def find_by_number(cls,number):
        
        # method that takes in a username and returnes a user that matches that number
        
        for user in cls.userslist:
            if user.password == number:
                return user
    @classmethod
    def user_exist(cls,number):
        for user in cls.userslist:
            if user.username ==number:
                return True
                return False
    
class Credentials:
    
    # class that generates new instances of credentials
    
    accounts=[]
    def __init__(self,accountusername,accountname,accountpassword):
        self.accountusername = accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword
    def save_account(self):
        
        # method that saves user info to accounts
        Credentials.accounts.append(self)
    def delete_account(self):
        
        # method that deletes a saved credential from accounts
        Credentials.accounts.remove(self)
    @classmethod
    def display_accounts(cls):
        
        # method that returns a list of the accounts
        
        for account in cls.accounts:
            return cls.accounts
    @classmethod
    def find_by_number(cls,number):
        
        # method that takes in a number and returns a contact that matches that number
        
        for account in cls.accounts:
            if account.accountusername ==number:
                return account
        