import uuid

def get_username(user_data, user_name):
    """Look for username in data to either login or reject to register."""
    for user in user_data:
        if user_name == user:
            return True
    return  False

def get_id(user_data, user_name):
    """Retrieves id of the user, to return it in the login function"""
    if user_name in user_data:
        return user_data[user_name].get("id")
    return None

def get_password(user_data, password):
    """Search for password of the user"""
    for user in user_data.values():
        if password == user["password"]:
            return True
    return False

def register(user_data):
    print("Welcome to the Bank LTD, please register new user!")
    user_name = input("Enter new user name: \n")
    if get_username(user_data, user_name) == False:
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
    TODO Learn DB
    """
    print("Please, enter your credentials in the terminal below:")
    user_name = input("User name: \n")
    if get_username(user_data, user_name):
        password = input("Provide your password: \n")
        if get_password(user_data, password):
            print("Login successful!")
            #assign ID to be returned with successful login
            id = get_id(user_data, user_name)
            return id
        else:
            print("Invalid password.")
            return False
    else:
        # Return msg if no user found   
        print("User name does not exist.")
        return False

