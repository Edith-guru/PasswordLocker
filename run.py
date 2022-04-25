import random
from user import user

def main():
    while True:
        print('Welcome to Password Locker!')
        print('\n')
        print("Select a short code to navigate through: to create a new user use 'nu: To login to your account 'lg or 'ex' to exit section")
        short_code = input().lower()
        print('\n')
        
        
        # creating new user using the short code 
        
        if short_code == 'nu':
            print('Create Username')
            created_user_name = input()
            
            print('Create Password')
            created_user_password = input()
            
            print('Confirm Password')
            confirm_password = input()
            
            # validation login
            
            while confirm_password != created_user_password:
                print('Invalid, Password did not match!')
                print('Enter your Password')
                created_user_password = input()
                print('Confirm your Password')
                confirm_password = input()
            else:
                print(f'Congratulations {created_user_name}! account creation successful')
                print('\n')
                print('Procees to login')
                print('Username')
                entered_username = input()
                print('Your password')
                entered_password = input()
            while entered_username != created_user_name or entered_username != created_user_password:
                print('Invalid username or password')
                print('Username')
                entered_username = input()
                print('Your Password')
                entered_password = input()
            else:
                print(f'Welcome {entered_username} to your account')
                print('\n')
        elif short_code == 'lg':
            print('Welcome')
            print('Enter username')
            default_user_name = input()
            print('Enter Password')
            default_user_password = input()
            print('\n')
            
            while default_user_name != 'testuser' or default_user_password != '09876':
                print("Wrong Username or Password. Username 'testuser' and password '09876'")
                print("Enter Username")
                default_user_name = input()
                print('Enter Password')
                default_user_password = input()
                print('\n')
            else:
                print('Login Success!')
                print('\n')
                print('\n')
                
        elif short_code == 'ex':
            break
        else:
            print('Enter valid code to continue')
            
            
# ensures the main function is executed everytime the file is run
if __name__ == '__main__':
    main()
            