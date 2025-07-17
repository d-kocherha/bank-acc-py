
class BankAccount:

    def __init__(self):
        pass

    def create_checking(user_ID):
        """Function for creation of user bank account"""
        user_account = {user_ID : {'type' : 'checking', 'balance' : 0}  }   
        return user_account

    def provide_amount(self):
        amount = int(input("Provide the amount"))
        try:
            return amount
        except:
            print("You should enter number value.")
            return self.provide_amount()

    def withdrawal(self, balance):
        # Withdrawal works okay. No changes required.
        withdrawal = self.provide_amount()
        if balance-withdrawal < 0:
            print("You don't have enough for withdrawal!")
            print(f"Current balance : {balance}")
            return balance 
        else:
            balance -= withdrawal
            print(f"You have withdrawn {float(withdrawal)}$.\n"\
                f"Your new balance is {float(balance)}$.")
            return balance

    def deposit(self, balance):
        # Deposit works okay. No changes required.
        deposit = self.provide_amount()
        balance += deposit
        print(f"Your deposit of {float(deposit)}$ has been successful.\n"\
            f"Your new balance is {float(balance)}$")
        return balance
    


