# Amazon Sales ETL Pipeline

An end-to-end ETL pipeline built with **Python, Pandas, and PostgreSQL** that extracts raw sales data, validates and transforms it, aggregates product-level metrics, generates data quality reports, and loads processed results back into PostgreSQL.

This project is part of my Data Engineering learning journey, where I continuously improve a single pipeline by introducing more realistic ETL practices such as modular architecture, logging, reporting, and error handling.

---

# Project Overview

This pipeline simulates a simplified production ETL workflow.

Instead of simply cleaning data and exporting a CSV, the project focuses on building a maintainable pipeline that includes:

- Data extraction from PostgreSQL
- Data validation and cleaning
- Error logging
- Product-level aggregation
- CSV export
- PostgreSQL loading
- Data quality reporting
- Pipeline execution logging

---

# Pipeline Architecture

> *(Insert your architecture diagram here)*

---

# Pipeline Workflow

```
                PostgreSQL (amazon_sales)
                         │
                         ▼
                  Extract Sales Data
                         │
                         ▼
               Validate & Clean Data
                  ┌────────┴────────┐
                  ▼                 ▼
           Clean Records      Invalid Records
                  │                 │
                  ▼                 ▼
        Aggregate Product Sales   errors_log.csv
                  │
                  ▼
          Aggregated Results
        ┌─────────┼───────────┐
        ▼         ▼           ▼
 new_output.csv  PostgreSQL  data_quality_report.csv
          (aggregated_sales)

        pipeline.log (generated throughout)
```

---

# Features

- Extracts sales data directly from PostgreSQL
- Cleans and validates incoming records
- Standardizes product names
- Detects invalid records
- Separates bad records into an error log
- Aggregates sales metrics by product
- Exports processed data to CSV
- Loads aggregated results into PostgreSQL
- Generates data quality reports
- Tracks pipeline execution time
- Maintains timestamped execution logs
- Modular ETL architecture

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data transformation |
| PostgreSQL | Source & destination database |
| SQLAlchemy | Database loading |
| psycopg2 | PostgreSQL connectivity |
| Git | Version control |
| GitHub | Project hosting |

---

# Project Structure

```
project/

├── main.py
├── extract.py
├── transform.py
├── load.py
├── report.py
├── logger.py
├── config.py
├── requirements.txt
│
├── output/
│   ├── new_output.csv
│   ├── errors_log.csv
│   └── data_quality_report.csv
│
├── logs/
│   └── pipeline.log
│
└── README.md
```

---

# Pipeline Outputs

## Aggregated Sales Report

**new_output.csv**

Contains:

- Product
- Transaction Count
- Total Revenue
- Maximum Sale
- Minimum Sale

---

## Error Log

**errors_log.csv**

Stores all invalid or incomplete records removed during validation.

---

## Data Quality Report

**data_quality_report.csv**

Provides pipeline quality metrics including:

- Total Rows
- Bad Rows
- Clean Rows
- Unique Products

---

## PostgreSQL Output

**aggregated_sales**

Stores the final aggregated dataset back into PostgreSQL.

---

## Pipeline Log

**pipeline.log**

Records timestamped execution logs for every stage of the pipeline.

---

# Project Evolution

This repository reflects how the pipeline evolved over time rather than being built in a single version.

| Version | Improvement |
|----------|-------------|
| Version 1 | Basic Python data processing |
| Version 2 | Pandas-based transformations |
| Version 3 | Modular ETL architecture |
| Version 4 | PostgreSQL integration |
| Version 5 | Error handling & logging |
| Version 6 | Data quality reporting |
| Version 7 | Production-inspired pipeline organization |

The objective has been to continuously improve one project by introducing concepts commonly used in real-world data engineering workflows.

---

# Core Modules

### extract.py

Responsible for extracting data from PostgreSQL.

---

### transform.py

Performs:

- Validation
- Cleaning
- Aggregation

---

### load.py

Handles:

- CSV export
- PostgreSQL loading
- Error log generation

---

### report.py

Creates pipeline quality reports.

---

### logger.py

Configures centralized logging for the pipeline.

---

### main.py

Acts as the pipeline orchestrator by executing every ETL stage in sequence.

---

# Future Improvements

Planned enhancements include:

- PySpark implementation
- Docker containerization
- Apache Airflow orchestration
- AWS S3 integration
- Unit testing
- Environment variable configuration
- CI/CD pipeline

---

# Learning Goal

Rather than building many unrelated projects, this repository focuses on continuously improving a single ETL pipeline while gradually introducing more realistic engineering practices.

The goal is to strengthen my understanding of data pipelines before moving to distributed processing with PySpark, workflow orchestration with Airflow, and cloud-based data engineering.

---

# Author

**Nilesh Raut**

Aspiring Data Engineer

Currently learning Python, SQL, PostgreSQL, Pandas, and PySpark while building end-to-end data engineering projects.
