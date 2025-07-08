def create_account(user_ID):
    """Function for creation of user bank account"""
    user_account = {user_ID : {"balance" : 0}}     
    return user_account

def retrieve_balance(account_data):
    """Fetch data from accounts for balance upd."""
    pass

def withdrawal(balance, withdrawal):
    # Withdrawal works okay. No changes required.
    balance -= withdrawal
    print(f"You have withdrawn {float(withdrawal)}$.\n"\
        f"Your new balance is {float(balance)}$.")


def deposit(balance, deposit):
    # Deposit works okay. No changes required.
    balance += deposit
    print(f"Your deposit of {float(deposit)}$ has been successful.\n"\
          f"Your new balance is {float(balance)}$")
