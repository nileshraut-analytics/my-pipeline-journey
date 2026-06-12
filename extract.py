import psycopg2
import pandas as pd
import logging
import logger
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_data():
    try:
        conn = psycopg2.connect(
        host = DB_HOST,
        database = DB_NAME,
        user = DB_USER,
        password = DB_PASSWORD
    )
        
        query = "SELECT * FROM amazon_sales"
        df = pd.read_sql(query, conn)
        print(f"{get_timestamp()} [LOAD]  Loaded {len(df)} rows from PostgreSQL\n")
        logging.info(f"[LOAD]  Loaded {len(df)} rows from PostgreSQL")
        return df
    except Exception as e:
        print(f"[LOAD]  failed to load data from PostgreSQL")
        print(f"Error : {e}")
        logging.error(f"[LOAD]  failed to load data from PostgreSQ. Error {e}")