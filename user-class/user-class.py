class User:
    """Initialize user class to register, login (more to come)."""

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def register():
        print("Welcome to the Bank LTD, please register new user!")
        user_name = input("Enter new user name: \n")
        password = input("Enter your password: \n")
        password_confirm = input("Enter your password to confirm: \n")
        if password == password_confirm:
            password = password
        else:
            print("Password does not match!")
        user_data = {"user_name" : user_name, "password" : password}
        return user_data
       
