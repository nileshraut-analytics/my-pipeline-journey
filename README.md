# My Pipeline Journey 🚀

A hands-on Data Engineering project documenting my journey from basic Python scripts to a PostgreSQL-powered ETL pipeline.

## What It Does

* Extracts sales data from PostgreSQL
* Validates and cleans dirty records
* Separates bad records into an error log
* Aggregates sales metrics by product
* Exports aggregated results to CSV
* Loads aggregated results back into PostgreSQL

## Pipeline Flow

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
Load Results to PostgreSQL (aggregated_sales)

## Current Features

✅ PostgreSQL Integration

✅ Data Validation

✅ Error Logging

✅ Product-Level Aggregation

✅ CSV Export

✅ PostgreSQL Output Tables

✅ Timestamped Pipeline Logs

✅ Basic Error Handling

## Project Evolution

| Version | Focus            | Description                                |
| ------- | ---------------- | ------------------------------------------ |
| v1      | Pure Python      | File handling, loops, dictionaries         |
| v2      | Pandas           | Data cleaning and aggregation              |
| v3      | Modular Pipeline | Reusable functions and structured workflow |
| v4      | PostgreSQL ETL   | Database extraction and loading            |
| v5      | Error Handling   | Database logging and failure handling      |

## Core Functions

* `load_data()` — Extract data from PostgreSQL
* `validate_data()` — Separate clean and bad records
* `aggregate_data()` — Calculate product metrics
* `clean_output()` — Save CSV and load PostgreSQL output
* `errors_log()` — Save invalid records
* `run_pipeline()` — Execute the complete ETL workflow

## Tech Stack

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* psycopg2
* Git
* GitHub

## Learning Goal

This repository documents my progression toward becoming a Data Engineer by continuously improving a single pipeline and gradually introducing more realistic ETL practices.

Built by Nilesh Raut
