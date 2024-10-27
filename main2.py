import pandas as pd
import sqlite3
import json

# Load configuration from JSON file
with open('config.json', 'r') as file:
    config = json.load(file)

# Use the variables from the JSON configuration
db_path = config['db_path']
db_table = config['db_table']
thresshold = config['thresshold']

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# Query the table and load it into a DataFrame
query = f'SELECT * FROM {db_table};'
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Display the DataFrame
print(df)
print('---- ---- ---- ---- ---- ---- ')

# Check for missing values
null_amount = df.isnull().sum() + (df == '').sum()
print('Missing values per column:')
print(null_amount)


# status = hvis thresshold er x

# Loop over columns to check for missing values
for column in null_amount.index:
    missing_count = null_amount[column]
    if missing_count > 0:
        print(f'Missing values in "{column}": {missing_count}')
        # Optionally: You could also calculate the percentage of missing values
        percent_missing = (missing_count / len(df)) * 100
        print(f'Percentage of missing values in "{column}": {percent_missing:.2f}%')
        if percent_missing > thresshold:
            print("nooo")
