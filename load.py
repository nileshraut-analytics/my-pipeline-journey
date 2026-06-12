from extract import get_timestamp
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from sqlalchemy import create_engine
import logging
import logger


def clean_output(final_df):
    print(f"{get_timestamp()} [OUTPUT] Saved aggregated data to new_output.csv\n")
    logging.info(f"[OUTPUT] Saved aggregated data to new_output.csv")
    final_df.to_csv("new_output.csv", index=False)

    try:
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
        final_df.to_sql(
            "aggregated_sales",
            engine,
            if_exists = "replace",
            index = False
        )
        print(f"{get_timestamp()} [DB] Loaded {len(final_df)} rows into aggregated_sales\n")
        logging.info(f"[DB] Loaded {len(final_df)} rows into aggregated_sales")
    except Exception as e:
        print(f"{get_timestamp()} [DB] Failed to load aggregated data.")
        print(f"Error: {e}")
    
def errors_log(bad_rows):
    print(f"{get_timestamp()} [OUTPUT] Saved bad rows to errors_log.csv\n")
    logging.info(f"[OUTPUT] Saved bad rows to errors_log.csv")
    return bad_rows.to_csv("errors_log.csv", index=False)
