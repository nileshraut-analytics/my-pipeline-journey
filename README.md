# My Pipeline Journey 🚀

A production-grade Python data pipeline built from scratch — evolving from pure Python to a modular Pandas-powered pipeline.

## What it does
- Reads raw sales data from a CSV file
- Validates and cleans dirty data (missing values, invalid types)
- Aggregates sales by product (count, total, revenue, max, min)
- Saves clean results to output CSV
- Logs all bad records to a separate error log

## Pipeline Flow
Input (CSV) → Validation → Aggregation → Output (CSV) + Error Log

## Evolution
| Version | Approach | File |
|---|---|---|
| v1 — Pure Python | Manual loops, dicts, file handling | day1.py - day5.py |
| v2 — Pandas | Optimised with Pandas DataFrame | day12.py - day14.py |
| v3 — Modular | Clean functions, reusable pipeline | pipeline.py |

## Modular Pipeline (Final Version)
```python
run_pipeline("sales_input.csv")
```
One function call runs the entire pipeline end to end.

## Functions
- `load_data()` — reads CSV into DataFrame
- `validate_data()` — separates clean and bad records
- `aggregate_data()` — groups and aggregates by product
- `clean_output()` — saves results to CSV
- `errors_log()` — saves bad records to CSV

## Tech Used
- Python 3
- Pandas
- Git/GitHub

## Built by
Nilesh Raut — Aspiring Data Engineer
📂 [GitHub](https://github.com/nileshraut-analytics/my-pipeline-journey)
