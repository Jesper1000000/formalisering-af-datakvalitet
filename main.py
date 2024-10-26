import pandas as pd
from sql.check_bestået_status import check_bestået_status
from services.handle_json import read_json, read_ini
import json
import sqlite3

forretningsregler = read_json()

db = forretningsregler["database"]
table = forretningsregler["table"]
db = sqlite3.connect(db)


column1 = forretningsregler["kolonner"]["værdier"]["kolonne_værdi_1"]
column2 = forretningsregler["kolonner"]["værdier"]["kolonne_værdi_2"]
column3 = forretningsregler["kolonner"]["påvirket_kolonne"]
værdi1 = forretningsregler["regel"]["hvis_værdier_er_ens"]
værdi2 = forretningsregler["regel"]["hvis_værdier_ikke_er_ens"]
check_bestået_status(db, table, column1, column2, column3, værdi1, værdi2)


db.close()








# def select_all(db):
#     db_select = pd.read_sql_query(f'SELECT * FROM {tabel}', db)
#     print(db_select)