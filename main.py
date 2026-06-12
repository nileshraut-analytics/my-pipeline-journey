import logging
import logger
from extract import load_data, get_timestamp
from time import time
from transform import validate_data, aggregate_data
from load import clean_output, errors_log
from report import data_quality_report


def run_pipeline():
    start_time = time()
    df = load_data()

    if df is None:
        return
    
    bad_rows, clean_rows = validate_data(df)
    final_df = aggregate_data(clean_rows)
    clean_output(final_df)
    errors_log(bad_rows)
    data_quality_report(df, bad_rows, clean_rows, final_df)
    end_time = time()
    execution_time = end_time - start_time
    print(f"{get_timestamp()} [PIPELINE] Completed successfully!")
    logging.info(f"[PIPELINE] Completed successfully!")
    print(f"{get_timestamp()} [PIPELINE] Total execution time: {execution_time:.2f} seconds")
    logging.info(f"[PIPELINE] Total execution time: {execution_time:.2f} seconds")

run_pipeline()