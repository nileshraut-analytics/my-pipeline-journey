import logging
import logger
import pandas as pd

def data_quality_report(df, bad_rows, clean_rows, final_df):
    report_df = pd.DataFrame({
        "metric" : ["total_rows", "bad_rows", "clean_rows", "unique_products"],
        "value" : [len(df), len(bad_rows), len(clean_rows), len(final_df)]
    })
    report_df.to_csv("data_quality_report.csv", index=False)
    print(f"[REPORT] Saved data_quality_report.csv\n")
    logging.info(f"[REPORT] Saved data_quality_report.csv")
    return report_df