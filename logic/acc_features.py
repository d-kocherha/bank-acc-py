
class BankAccount:

    def __init__(self):
        self.balance = 0

    def create_account(user_ID):
        """Function for creation of user bank account"""
        user_account = {'user_account' : user_ID,
                         'balance' : 0}     
        return user_account

    def retrieve_balance(self, account_data):
        """Fetch data from accounts for balance upd."""
        self.balance = account_data["balance"]
        return self.balance

    def withdrawal(self, withdrawal):
        # Withdrawal works okay. No changes required.
        if self.balance-withdrawal < 0:
            print("You don't have enough for withdrawal!")
            print(f"Current balance : {self.balance}")
        else:
            self.balance -= withdrawal
            print(f"You have withdrawn {float(withdrawal)}$.\n"\
                f"Your new balance is {float(self.balance)}$.")
            return self.balance

    def deposit(self, deposit):
        # Deposit works okay. No changes required.
        self.balance += deposit
        print(f"Your deposit of {float(deposit)}$ has been successful.\n"\
            f"Your new balance is {float(self.balance)}$")
        return self.balance
    


