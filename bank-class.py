class Bank_account:
    """Create bank account which accepts user-login, user-password,
    and account number. Provides services of withdrawal and depositing."""
    def __init__(self, user_login, user_password, account_number):
        # TODO get user credentials to access an account -> learn about it
        self.user_login = user_login
        self.user_password = user_password
        self.account_number = account_number
        self.balance = 0

    def withdrawal(self, withdrawal):
        # Withdrawal works okay. No changes required.
        self.balance -= withdrawal
        print(f"You have withdrawn {float(withdrawal)}$.\n"\
            f"Your new balance is {float(self.balance)}$.")

    def deposit(self, deposit):
        # Deposit works okay. No changes required.
        self.balance += deposit
        print(f"Your deposit of {float(deposit)}$ has been successful.\n"\
              f"Your new balance is {float(self.balance)}$")


