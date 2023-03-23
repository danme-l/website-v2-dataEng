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

# Set the SQL statements to create the table
create_subject_table_sql = """
CREATE TABLE IF NOT EXISTS weo.subjects (
    subject_id VARCHAR(12) PRIMARY KEY,
    descriptor VARCHAR(82),
    notes VARCHAR(1313),
    units VARCHAR(50),
    scale VARCHAR(8)
);
"""
create_countries_table_sql = """
CREATE TABLE IF NOT EXISTS weo.countries (
    country_id VARCHAR(6) PRIMARY KEY,
    country VARCHAR(32)
);
"""
create_series_table_sql = """
CREATE TABLE IF NOT EXISTS weo.series (
    id SERIAL PRIMARY KEY, 
    subject_id VARCHAR(12),
    country_id VARCHAR(6),
    estimates_start SMALLINT,
    notes VARCHAR(3264),
    year SMALLINT,
    value NUMERIC
);
"""
cursor.execute(create_subject_table_sql)
cursor.execute(create_countries_table_sql)
cursor.execute(create_series_table_sql)

# Copy from csv
copy_subjects_table_sql = f'''COPY weo.subjects(subject_id,descriptor,notes,units,scale)
FROM '{os.getcwd()}/world_economic_outlook/csv_files/subjects.csv'
DELIMITER ','
CSV HEADER;'''

copy_countries_table_sql = f'''COPY weo.countries(country_id,country)
FROM '{os.getcwd()}/world_economic_outlook/csv_files/countries.csv'
DELIMITER ','
CSV HEADER;'''

copy_series_table_sql = f'''COPY weo.series(id,subject_id,country_id,estimates_start,notes,year,value)
FROM '{os.getcwd()}/world_economic_outlook/csv_files/series.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(copy_subjects_table_sql)
cursor.execute(copy_countries_table_sql)
cursor.execute(copy_series_table_sql)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()