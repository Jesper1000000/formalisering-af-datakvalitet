import pandas as pd
import json
import sqlite3

def apply_business_rule(df_studerende, df_studerende_status, regel):
    """
    Applies the business rule to the 'bestået' column of df_studerende and updates the 'status' column of df_studerende_status.

    Parameters:
    df_studerende (pd.DataFrame): DataFrame containing the 'bestået' column.
    df_studerende_status (pd.DataFrame): DataFrame to update the 'status' column.
    regel (dict): Dictionary containing the business rule.

    Returns:
    pd.DataFrame: Updated df_studerende_status DataFrame.
    """
    df_studerende_status['status'] = df_studerende['bestået'].apply(
        lambda x: regel['regel']['ja'] if x == 'ja' else regel['regel']['nej']
    )
    return df_studerende_status

# Connection til db 
df_studerende_connection = sqlite3.connect('/Users/jesper/Desktop/EAAA/Semester 7/Bachelor Opgave/PoC/database/db_studerende.db')
df_studerende = pd.read_sql_query('SELECT * FROM df_studerende', df_studerende_connection)


data_studerende_status_connection = sqlite3.connect('/Users/jesper/Desktop/EAAA/Semester 7/Bachelor Opgave/PoC/database/db_studerende_status.db')
df_studerende_status = pd.read_sql_query('SELECT * FROM data_studerende_status', data_studerende_status_connection)


# Indlæs forretningsregler
with open('forretningsregler.json', 'r') as f:
    forretningsregler = json.load(f)

df_studerende_status = apply_business_rule(df_studerende, df_studerende_status, forretningsregler['regel 1'])

# Skriv df_studerende_status til SQLite database
df_studerende_status.to_sql('studerende_status', data_studerende_status_connection, if_exists='replace', index=False)

print("\n",df_studerende_status.to_string(index=False),"\n")
print("\n",df_studerende.to_string(index=False),"\n")

df_studerende_connection.close()
data_studerende_status_connection.close()

