import uuid

def read_username(user_data, user_name):
    """Look for username in data to either login or regect to register."""
    for user in user_data:
        if user_name == user:
            return True
    return  False

def read_password(user_data, password):
    """Search for password of the user"""
    for user in user_data.values():
        if password == user["password"]:
            return True
    return False

def register(user_data):
    print("Welcome to the Bank LTD, please register new user!")
    user_name = input("Enter new user name: \n")
    if read_username(user_data, user_name) == False:
        password = input("Enter your password: \n")
        password_confirm = input("Enter your password to confirm: \n")
        if password == password_confirm:
            # TODO Implement hashing password
            password = password
            user_id = uuid.uuid4()
            user_data = {user_name : { "id" : str(user_id), "password" : password}}
            print(f"New user {user_name} has been created! Welcome.")
            print("Please, login to access your account.")
            return user_data
        else:
            print("Password does not match! Try again.")
            register(user_data)
    else:
        print("User exists. Try again.")
        register(user_data) 

def login(user_data):
    """Linear search function to look for user. Will get clunky once data expands.
    TODO Learn DB, potentially less husle.
    """
    print("Please, enter your credentials in the terminal below:")
    user_name = input("User name: \n")
    if read_username(user_data, user_name):
        password = input("Provide your password: \n")
        if read_password(user_data, password):
            print("Login successful!")
            return True
        else:
            print("Invalid password.")
            return False
    else:
        # Return msg if no user found   
        print("User name does not exist.")

