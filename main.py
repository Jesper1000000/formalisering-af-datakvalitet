import pandas as pd
from forretningsregler.check_bestået_status.sql import check_bestået_status

from services.db_connection import get_db_connection

# Get the database connection
db = get_db_connection()

check_bestået_status(db)

# def select_all(db):
#     db_select = pd.read_sql_query(f'SELECT * FROM {tabel}', db)
#     print(db_select)