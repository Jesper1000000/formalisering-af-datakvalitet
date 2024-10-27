import json
import logging

def read_json() -> dict:
    try:
        with open('forretningsregler/check_bestået_status/check_bestået_status.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return {}