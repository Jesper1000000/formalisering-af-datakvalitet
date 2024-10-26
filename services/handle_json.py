import json
import configparser

# Indlæs forretningsregler
def read_json() -> dict:
    with open('config/config.json', 'r') as f:
        forretningsregler = json.load(f)
        return forretningsregler

def read_ini():
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    db = config['database']['path']
    print(db)
    