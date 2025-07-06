import uuid

def register():
    print("Welcome to the Bank LTD, please register new user!")
    user_name = input("Enter new user name: \n")
    password = input("Enter your password: \n")
    password_confirm = input("Enter your password to confirm: \n")
    if password == password_confirm:
        # TODO Implement hashing password
        password = password
        user_id = uuid.uuid4()
        user_data = {str(user_id):{ "user_name" : user_name, "password" : password}}
        print(f"New user {user_name} has been created! Welcome.")
        return user_data
    else:
        print("Password does not match! Try again.")    

def login(user_data):
    """Linear search function to look for user. Will get clunky once data expands.
    TODO Learn DB, potentially less husle.
    """
    print("Please, enter your credentials in the terminal below:")
    user_name = input("User name: \n")
    for user in user_data.values():
        if user_name == user["user_name"]:
            password = input("Provide your password: \n")
            if password == user["password"]:
                print("Login successful!")
                return True
            else:
                print("Invalid password.")
                return False
    # Return msg if no user found   
    print("User name does not exist.")

