# My Pipeline Journey 🚀

A Python data pipeline built from scratch — processing raw sales data end to end.

## What it does
- Reads raw sales data from a CSV file
- Validates and cleans dirty data (missing values, invalid types)
- Aggregates sales by product (count, total, max, min)
- Saves clean results to output CSV
- Logs all bad records to a separate error log

## Pipeline Flow
Input (CSV) → Validation → Processing → Output (CSV) + Error Log

## Files
- `day1.py` to `day5.py` — daily progress building the pipeline
- `sales_input.csv` — raw input data
- `new_output.csv` — clean aggregated results
- `errors_log.csv` — logged bad records

## Tech Used
- Python 3
- CSV module

## Built by
Nilesh Raut — aspiring Data Engineer
