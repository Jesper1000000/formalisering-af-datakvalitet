from services.read_file import read_json
import sqlite3
import logging

def get_db_connection():
    try: 
        db_connection = read_json()
        db = db_connection["database"]
        connection = sqlite3.connect(db)
        return connection
    except sqlite3.Error as e:
        logging.error(f"An error occurred: {e}")
        return None