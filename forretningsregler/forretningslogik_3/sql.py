import pandas as pd
from services.read_file import read_json
import sqlalchemy

forretningsregler = read_json()

database_1_path = forretningsregler["database_1"]["path"]
database_1_tabel = forretningsregler["database_1"]["tabel"]
database_1_værdier = forretningsregler["database_1"]["værdier"]
database_2_path = forretningsregler["database_2"]["path"]
database_2_tabel = forretningsregler["database_2"]["tabel"]
database_2_værdier = forretningsregler["database_2"]["værdier"]
værdi1 = forretningsregler["regel"]["hvis_værdier_er_ens"]
værdi2 = forretningsregler["regel"]["hvis_værdier_ikke_er_ens"]

def read_sql_query(db):
    df = pd.read_sql_query(f"PRAGMA table_info({database_1_tabel});", db)
    print(df)

def check_afsluttet_status(db):
    try:
        # SQL logik
        db.execute(f'''
            UPDATE {tabel}
            SET {column3} = CASE 
                WHEN {column1} = {column2} THEN '{værdi1}' 
                ELSE '{værdi2}' 
            END
        ''', {"værdi1": værdi1, "værdi2": værdi2})

        # Commit ændringer
        db.commit()
        print(f'Succes - tabel "{tabel}" er blevet opdateret')
        print(pd.read_sql_query(f"SELECT * FROM {tabel}", db))

    # Hvis der sker en fejl
    except sqlalchemy.exc.SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return None

