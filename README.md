# My Pipeline Journey 🚀

A hands-on Data Engineering project documenting my journey from basic Python scripts to a PostgreSQL-powered ETL pipeline.

---

## What It Does

* Extracts sales data from PostgreSQL
* Validates and cleans dirty records
* Separates bad records into an error log
* Aggregates sales metrics by product
* Exports aggregated results to CSV
* Loads aggregated results back into PostgreSQL
* Generates a data quality report
* Tracks total pipeline execution time

---

## Pipeline Flow

```text
PostgreSQL (amazon_sales)
            ↓
        Load Data
            ↓
      Validate Data
            ↓
   Separate Bad Records
            ↓
 Aggregate Product Sales
            ↓
   Export Results (CSV)
            ↓
Load Results to PostgreSQL
     (aggregated_sales)
            ↓
 Generate Data Quality Report
            ↓
   Track Execution Time
```

---

## Current Features

✅ PostgreSQL Integration

✅ Data Validation

✅ Error Logging

✅ Product-Level Aggregation

✅ CSV Export

✅ PostgreSQL Output Tables

✅ Data Quality Reporting

✅ Execution Time Tracking

✅ Timestamped Pipeline Logs

✅ Basic Error Handling

---

## Outputs Generated

### Aggregated Sales Report

```text
new_output.csv
```

Contains product-level sales metrics:

* Count
* Total Revenue
* Maximum Sale
* Minimum Sale

### Error Log

```text
errors_log.csv
```

Contains invalid or incomplete records removed during validation.

### Data Quality Report

```text
data_quality_report.csv
```

Contains pipeline monitoring metrics:

* Total Rows
* Bad Rows
* Clean Rows
* Unique Products

### PostgreSQL Output Table

```text
aggregated_sales
```

Stores aggregated sales metrics inside PostgreSQL.

---

## Project Evolution

| Version | Focus                   | Description                                |
| ------- | ----------------------- | ------------------------------------------ |
| v1      | Pure Python             | File handling, loops, dictionaries         |
| v2      | Pandas                  | Data cleaning and aggregation              |
| v3      | Modular Pipeline        | Reusable functions and structured workflow |
| v4      | PostgreSQL ETL          | Database extraction and loading            |
| v5      | Error Handling          | Database logging and failure handling      |
| v6      | Data Quality Monitoring | Reporting and execution tracking           |

---

## Core Functions

### load_data()

Extracts data from PostgreSQL into a Pandas DataFrame.

### validate_data()

Cleans data and separates valid and invalid records.

### aggregate_data()

Calculates product-level sales metrics.

### clean_output()

Exports results to CSV and loads aggregated data into PostgreSQL.

### errors_log()

Stores invalid records in a separate error log.

### data_quality_report()

Generates pipeline quality metrics and monitoring reports.

### run_pipeline()

Executes the complete ETL workflow from extraction to reporting.

---

## Tech Stack

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* psycopg2
* Git
* GitHub

---

## Learning Goal

This repository documents my progression toward becoming a Data Engineer by continuously improving a single pipeline and gradually introducing more realistic ETL practices.

Instead of building many disconnected projects, this repository focuses on evolving one pipeline through multiple versions and improvements.

---

## Built By

**Nilesh Raut**
Aspiring Data Engineer 🚀
