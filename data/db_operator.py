import json
from pathlib import Path

class Data_Operator:

    def __init__(self, user_db, account_db):
        self.user_db = Path(f"{user_db}.json")
        self.account_db = Path(f"{account_db}.json")

    def read_db(self):
        """Read db to return values for further search."""
        db = json.loads(self.user_db.read_text()) #convert db to dictionary
        return db

    def update_db(self, user_data):
        """Save changes to db"""
        db = self.read_db()
        updated = {**db, **user_data}
        return self.user_db.write_text(json.dumps(updated, indent=4))

    def read_acc(self):
        open_acc_db = json.loads(self.account_db.read_text())
        return open_acc_db

    def update_acc(self, changes):
        open_db = self.read_acc()
        updated_acc = {**open_db, **changes}
        return self.account_db.write_text(json.dumps(updated_acc, indent=4))

    def retrieve_balance(self, user_id):
        """Fetch data from accounts."""
        open_db = self.read_acc()
        if user_id in open_db:
            get_balance = open_db[user_id].get("balance")
            balance = get_balance
            return balance
        else:
            print("There's no bank account for this user yet.")
        
    def update_balance(self, upd_balance, user_id):
        "Attempt to create function to change "
        open_db = self.read_acc()
        if user_id in open_db:
            open_db[user_id]["balance"] = upd_balance
            return self.account_db.write_text(json.dumps(open_db, indent=4))