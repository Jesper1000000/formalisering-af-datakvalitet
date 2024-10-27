import pandas as pd
from forretningsregler.forretningslogik_1.sql import check_bestået_status
from forretningsregler.forretningslogik_2.sql import check

from services.db_connection import get_db_connection

# Get the database connection
db = get_db_connection()

# Forretningsregel som kaldes 
check_bestået_status(db)
