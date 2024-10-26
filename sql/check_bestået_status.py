import pandas as pd

def check_bestået_status(db, tabel, column1, column2, column3, værdi1, værdi2):
    # Step 1: Read and calculate bestået status
    db_select = pd.read_sql_query(f'''
        SELECT {column1}, {column2},
               CASE 
                   WHEN {column1} = {column2} THEN '{værdi1}' 
                   ELSE '{værdi2}' 
               END AS {column3}
        FROM {tabel}
    ''', db)

    # Display the results (optional)
    print(db_select)

    # Step 2: Write the results back to the database
    # Here, we assume the table has a column named 'bestået' to be updated
    db_select.to_sql(tabel, db, if_exists='replace', index=False)
    
    return db_select
