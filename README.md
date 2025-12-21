# Data-Migration-Project-
 
**ETL Pipeline · Legacy → Target PostgreSQL · XSLT/XML · Data Quality · Java Migration Engine · Docker**

This project simulates a real enterprise data-migration workflow (insurance/finance).  
It demonstrates my ability to build **end-to-end migration pipelines**, work with **messy legacy data**, apply **XSLT transformations**, implement **data quality checks**, and run **Java-based post-migration logic** — all of which match the job requirements.

---

## Project Overview

The pipeline migrates customer records from a **legacy PostgreSQL schema** and optional **XML exports** into a **clean, normalized target database**.

Main components:

- **Python ETL** (Extract → Transform → Load)  
- **XSLT preprocessing** for XML-based legacy exports  
- **Data quality validation layer**  
- **Java Migration Engine** for post-load operations  
- **Dockerized environment** with Legacy DB + Target DB  

---

## Database Schemas

**Legacy (denormalized):** messy full names, text dates, unstructured addresses.  
**Target (normalized):** separated name fields, proper date types, cleaned address structure.

(SQL definitions are in the repository.)

---

## ETL Pipeline (Python)

**Extract (`extract.py`)**  
- Reads raw customer records from Legacy DB.

**Transform (`transform.py`)**  
- Splits full names  
- Normalizes addresses  
- Fixes phone formats  
- Parses inconsistent dates  
- Logs invalid records  

**Load (`load.py`)**  
- Inserts clean validated records into Target DB.

---

## XSLT Layer

Legacy customer data (XML) can be transformed via:

- `customer_transform.xslt`  
- `apply_xslt.py`  

Used to simulate enterprise systems that export data as XML.

---

## Data Quality Validation

`data_quality.py` checks:

- Missing mandatory fields  
- Invalid formats  
- Duplicates  
- Incorrect dates  

Outputs a validation report.

---

## Java Migration Engine

A small Java module that simulates enterprise post-migration logic:

- Runs final SQL adjustments  
- Inserts technical/service records  
- Handles controlled upserts  

Located in `/java-migration-engine`.

---

## Docker

`docker-compose.yml` starts:

- Legacy PostgreSQL  
- Target PostgreSQL  
- ETL pipeline container  

Run:

```bash
# 1. Start DBs
docker-compose up -d

# 2. Optional XML → Clean XML
python xslt/apply_xslt.py

# 3. Run ETL
python etl_pipeline.py

# 4. Run data quality checks
python validation/data_quality.py

# 5. Run Java engine
cd java-migration-engine
mvn compile
mvn exec:java

---