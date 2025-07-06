class User:
    """Initialize user class to register, login (more to come)."""

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.unique_id = []
        self.access = True
        
