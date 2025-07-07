import data.db_operator as db
import logic.user_features as uf

data_path = db.db_path
data = db.read_db(data_path)

def registration():
    """Creates user and updates db."""
    db.update_db(uf.register(data))
    main()

def login():
    """Login to the system."""
    uf.login(data)
    main()

def main():
    """Main module for interactions from CLI."""

    options = {1 : registration,
               2 : login}

    print("Welcome to the Bank Simulator CLI.\n"\
        "Pick an option (1, 2, ...):\n"\
        "1. Register new user.\n"\
        "2. Login")
    choice = input("Pick your option: \n")
    return options[int(choice)]()

if __name__ == "__main__":
    main()