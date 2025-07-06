def withdrawal(self, withdrawal):
    # Withdrawal works okay. No changes required.
    self.balance -= withdrawal
    print(f"You have withdrawn {float(withdrawal)}$.\n"\
        f"Your new balance is {float(self.balance)}$.")
    self.history.append(f"Withdrawal : -{float(withdrawal)}")

def deposit(self, deposit):
    # Deposit works okay. No changes required.
    self.balance += deposit
    print(f"Your deposit of {float(deposit)}$ has been successful.\n"\
          f"Your new balance is {float(self.balance)}$")
    self.history.append(f"Deposit : +{float(deposit)}")