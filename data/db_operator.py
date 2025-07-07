import json
from pathlib import Path

db_path = Path("data/db.json")

def read_db(db_path):
    """Read db to return values for further search."""
    db = json.loads(db_path.read_text()) #convert db to dictionary
    return db

def update_db(user_data):
    """Save changes to db"""
    db = read_db(db_path)
    updated = {**db, **user_data}
    return db_path.write_text(json.dumps(updated, indent=4))

