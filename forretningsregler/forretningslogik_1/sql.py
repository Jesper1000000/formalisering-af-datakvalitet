import pandas as pd
from services.read_file import read_json
import sqlalchemy

forretningsregler = read_json()

tabel = forretningsregler["tabel"]
column1 = forretningsregler["kolonner"]["værdier"]["kolonne_værdi_1"]
column2 = forretningsregler["kolonner"]["værdier"]["kolonne_værdi_2"]
column3 = forretningsregler["kolonner"]["påvirket_kolonne"]
værdi1 = forretningsregler["regel"]["hvis_værdier_er_ens"]
værdi2 = forretningsregler["regel"]["hvis_værdier_ikke_er_ens"]

def read_sql_query(db):
    df = pd.read_sql_query(f"PRAGMA table_info({tabel});", db)
    print(df)

def check_bestået_status(db):
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

