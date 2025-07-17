from data.db_operator import Data_Operator
import logic.user_features as uf
from logic.acc_features import BankAccount

class Engine:

    def __init__(self):
        pass

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
    
    def create_account(connected_db, user_id):
        """Creates new user"""
        new_account = BankAccount.create_checking(user_id)
        connected_db.update_acc(new_account)

    def money_operator(connected_db, user_id):
        """Takes db of account and user ID to withdraw/deposit."""
        balance = connected_db.retrieve_balance(user_id)
        #Write logic to prevent further running if returned None
        account = BankAccount()
        option = input("What you would like to do (withdraw/deposit)? ")
        if option == "withdraw":
            new_balance = account.withdrawal(balance)
            connected_db.update_balance(new_balance, user_id)
        elif option == "deposit":
            new_balance = account.deposit(balance)
            connected_db.update_balance(new_balance, user_id)
        else:
            print("Invalid input")


connection = Data_Operator('data/db', 'data/acc_db')
user = "Desmond"

Engine.money_operator(connection, user)


