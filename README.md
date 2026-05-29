# AI Data Analyst Agent - Customer Churn Analysis

## Project Overview

This project is an AI-powered Data Analyst Agent built for customer churn analysis.

The project starts with a customer churn dataset, loads the data into PostgreSQL, runs SQL-based churn analysis, saves query outputs, generates visual charts, and then extends the workflow to natural-language-to-SQL generation using OpenAI.

The project is being developed in versions:

* Version 1: Pre-written SQL queries are executed automatically using Python.
* Version 2: Natural-language business questions are converted into SQL using OpenAI, executed in PostgreSQL, and saved as output files.

Future versions will include SQL validation, MCP server integration, custom skills, automated storytelling, and slide deck generation.

## Project Objective

The objective of this project is to analyze customer churn patterns and identify key factors that may contribute to customer attrition.

The analysis answers questions such as:

* What is the overall churn rate?
* Which region has the highest churn rate?
* Which subscription plan has the highest churn?
* What are the top reasons customers churn?
* How do monthly charges, tenure, support tickets, contract type, and payment method relate to churn?

## Tech Stack

* Python
* PostgreSQL
* SQL
* OpenAI API
* pandas
* SQLAlchemy
* psycopg2
* matplotlib
* python-dotenv
* VS Code
* pgAdmin

## Project Structure

```text
ai-data-analyst-agent/
│
├── Data/
│   └── customer_churn_data.csv
│
├── outputs/
│   ├── version_1_predefined_sql/
│   │   ├── 01_preview_customer_data.csv
│   │   ├── 02_customer_summary.csv
│   │   ├── 03_overall_churn_rate.csv
│   │   ├── 04_churn_by_region.csv
│   │   ├── 05_churn_by_subscription_plan.csv
│   │   └── 06_top_churn_reasons.csv
│   │
│   └── version_2_ai_generated_sql/
│       ├── ai_overall_churn_rate.csv
│       ├── ai_highest_churn_by_region.csv
│       ├── ai_highest_churn_rate_by_subscription_plan.csv
│       ├── ai_top_churn_reasons.csv
│       ├── ai_avg_monthly_charge_by_churn_status.csv
│       ├── ai_avg_tenure_by_churn_status.csv
│       ├── ai_support_tickets_by_churn_status.csv
│       ├── ai_churn_by_contract_type.csv
│       └── ai_churn_by_payment_method.csv
│
├── charts/
│   ├── churn_by_region.png
│   ├── churn_by_subscription_plan.png
│   └── top_churn_reasons.png
│
├── prompts/
│   ├── business_questions.txt
│   ├── schema_context.txt
│   └── sql_generation_prompt.txt
│
├── sql/
│   └── churn_analysis_queries.sql
│
├── src/
│   ├── load_churn_data.py
│   ├── run_churn_queries.py
│   ├── create_churn_charts.py
│   └── generate_sql_from_question.py
│
├── business_insights.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Workflow

### Version 1: Pre-written SQL Automation

In Version 1, SQL queries were written manually and executed automatically using Python.

Workflow:

```text
CSV dataset → PostgreSQL database → pre-written SQL queries → Python execution → CSV outputs → charts
```

### 1. Load Data into PostgreSQL

The script `load_churn_data.py` reads the churn dataset from the `Data` folder, creates a PostgreSQL database, and loads the CSV data into a table named `customer_churn`.

```bash
python src/load_churn_data.py
```

### 2. Run Pre-written Churn Analysis Queries

The script `run_churn_queries.py` connects to PostgreSQL, runs pre-written SQL queries, and saves each query result as a CSV file.

```bash
python src/run_churn_queries.py
```

### 3. Generate Charts

The script `create_churn_charts.py` reads the output CSV files and creates visual charts in the `charts` folder.

```bash
python src/create_churn_charts.py
```

## Version 2: Natural Language to SQL

In Version 2, the project was extended to generate SQL queries from natural-language business questions using OpenAI.

Workflow:

```text
Business question → OpenAI generates SQL → Python checks safe SELECT query → PostgreSQL executes SQL → output saved as CSV
```

Example business question:

```text
What is the overall churn rate?
```

Example AI-generated SQL:

```sql
SELECT ROUND(SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END)::numeric / COUNT(*) * 100, 2) AS churn_rate
FROM customer_churn;
```

The script used for Version 2 is:

```bash
python src/generate_sql_from_question.py
```

## Prompt Files

The `prompts` folder contains the files used for natural-language-to-SQL generation:

* `business_questions.txt`: Stores sample business questions.
* `schema_context.txt`: Describes the database, table, columns, and business meaning of each field.
* `sql_generation_prompt.txt`: Provides instructions and safety rules for generating PostgreSQL SELECT queries.

## SQL Analysis Performed

The project includes analysis for:

* Customer data preview
* Total customers, churned customers, and active customers
* Overall churn rate
* Churn rate by region
* Churn rate by subscription plan
* Top churn reasons
* Average monthly charges by churn status
* Average tenure by churn status
* Support tickets by churn status
* Churn rate by contract type
* Churn rate by payment method

## Output Folder Structure

The `outputs` folder is divided into two parts:

* `version_1_predefined_sql/` contains outputs generated from manually written SQL queries.
* `version_2_ai_generated_sql/` contains outputs generated from natural-language questions where OpenAI generated the SQL and Python executed it in PostgreSQL.

## Charts Generated

The project creates the following charts:

* Churn Rate by Region
* Churn Rate by Subscription Plan
* Top Churn Reasons

## Business Insights

The business insights are documented in `business_insights.md`.

This file explains the key findings, business meaning, and recommendations based on the churn analysis.

## Current Project Status

The project has completed two stages:

### Version 1 Completed

```text
Pre-written SQL queries → run automatically → save outputs → generate charts
```

### Version 2 Completed

```text
Natural-language question → AI-generated SQL → PostgreSQL execution → save outputs
```

At this stage, the project demonstrates both SQL automation and AI-assisted SQL generation.

## Version 3: SQL Validation


So the correct Version 3 section should look like this:

````markdown
## Version 3: SQL Validation

In Version 3, SQL validation was added before executing AI-generated queries.

Version 3 workflow:

```text
Business question → AI-generated SQL → SQL validation → PostgreSQL execution → saved output

The validation step checks whether:

- The generated response is a valid PostgreSQL SELECT query
- Unsafe SQL commands such as INSERT, UPDATE, DELETE, DROP, ALTER, and TRUNCATE are blocked
- The generated SQL uses only allowed table names
- The generated SQL uses only valid columns from the `customer_churn` schema
- Missing or hallucinated columns are detected before execution

Example failed question:

```text
Which age group has the highest churn?
```

Since the dataset does not contain an `age_group` column, the system returns:

```text
COLUMN_NOT_FOUND: age_group
```

This prevents incorrect AI-generated SQL from running against the database.

## Security Note

Database credentials and API keys are stored in a local `.env` file and are not pushed to GitHub.

The `.gitignore` file prevents sensitive credentials from being uploaded.

## Future Enhancements

This project will be extended into a full AI Data Analyst Agent by adding:

* SQL column validation before execution
* AI-generated SQL error handling
* Generated SQL file saving
* Claude Code integration
* MCP server connection
* Custom analysis skills
* Automated business storytelling
* Slide deck generation

```
```
