from data.db_operator import Data_Operator
import logic.user_features as uf
from logic.acc_features import BankAccount
from datetime import datetime

class Engine:

    def __init__(self):
        pass
    
    timestamp = datetime.now().isoformat()

    def connect_db():
        user_db = input("Provide user base file path: ")
        acc_db = input("Provide accounts file path: ")
        try: 
            linked_db = Data_Operator(user_db, acc_db)
            return linked_db
        except:
            print("Connection failed. Check used parameters.")

    def registration(connected_db):
        """Creates user and updates db."""
        new_user = uf.register(connected_db.read_db())
        connected_db.update_db(new_user)       

    def login(connected_db):
        """Login to the system."""
        user_id = uf.login(connected_db.read_db())
        return user_id
    
    def create_account(self, connected_db, user_id):
        """Creates new user"""
        new_account = BankAccount.create_checking(user_id)
        connected_db.update_acc(new_account)        

    def money_operator(self, connected_db, user_id):
        """Takes db of account and user ID to withdraw/deposit."""
        balance = connected_db.retrieve_balance(user_id)
        if user_id != None:
            account = BankAccount()
            option = input("What you would like to do (withdraw/deposit)? ")

            if option == "withdraw":
                new_balance, amount = account.withdrawal(balance)
                connected_db.update_balance(new_balance, user_id)
                if amount != 0:
                    new_transaction = account.record_transaction(self.timestamp, new_balance, option, amount)
                    connected_db.update_history(user_id, new_transaction)
                else:
                    print("Failed transaction would not be recorded.")

            elif option == "deposit":
                new_balance, amount = account.deposit(balance)                
                connected_db.update_balance(new_balance, user_id)
                new_transaction = account.record_transaction(self.timestamp, new_balance, option, amount)
                connected_db.update_history(user_id, new_transaction)
            else:
                print("Invalid input")
        else:
            print("User does not exist.")