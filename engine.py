from data.db_operator import Data_Operator
import logic.user_features as uf
from logic.acc_features import BankAccount

class Engine:

    def __init__(self):
        self.token = True

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
        connected_db.update_db(uf.register(connected_db.read_db()))
        

    def login(connected_db):
        """Login to the system."""
        user_id = uf.login(connected_db.read_db())
        return user_id
    
    def create_account(connected_db, user_id):
        new_account = BankAccount.create_account(user_id)
        connected_db.update_acc(new_account)


connection = Data_Operator('data/db', 'data/acc_db')

user_id = Engine.login(connection)
Engine.create_account(connection, user_id) #overrides the latest data in JSON. To be fixed.


