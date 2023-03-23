import psycopg2
import os

from dotenv import dotenv_values
env = dotenv_values(".env")

# Set the database connection string
conn_string = f"host='{env['PGHOST']}' dbname='{env['PGDB']}' user='{env['PGUSER']}' password='{env['PGPWD']}'"

# Connect to the database
conn = psycopg2.connect(conn_string)

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Set the SQL statement to create the table
create_table_sql = """
CREATE TABLE IF NOT EXISTS money.money_supply (
    id SERIAL PRIMARY KEY,
    date DATE,
    value NUMERIC,
    type VARCHAR(2),
    country VARCHAR(3)
);
"""

cursor.execute(create_table_sql)

# Copy from csv
copy_table_sql = f'''COPY money.money_supply(id,date,value,type,country)
FROM '{os.getcwd()}/money_supply/csv_files/money_supply.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(copy_table_sql)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()