class Bank_account:
    """Create bank account which accepts user-login, user-password,
    and account number. Starting balance established to 0. """
    def __init__(self, user_login, user_password):
        self.user_login = user_login
        self.user_password = user_password
        self.account_number = []
        self.balance = 0
        self.history = []

