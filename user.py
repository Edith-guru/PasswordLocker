class User:

    # user creation

    user_list = []
    
    # the user will be stored in the list using the append method

    def __init__(self, user_name, password):
        self.username = user_name
        self.password = password
        
    def save_user(self):
        # save_user method saves an instance of the user to the user_list
        User.user_list.append(self)