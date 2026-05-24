# AI Data Analyst Agent - Customer Churn Analysis

## Project Overview

This project is the first version of an AI-powered Data Analyst Agent.  
The goal is to build a data analysis workflow that starts with a customer churn dataset, loads the data into PostgreSQL, runs SQL-based churn analysis, saves query outputs, and generates visual charts.

This version focuses on building the foundation before adding AI-generated SQL, Claude Code, MCP servers, custom skills, automated storytelling, and slide deck generation.

## Project Objective

The objective of this project is to analyze customer churn patterns and identify key factors that may contribute to customer attrition.

The analysis answers questions such as:

- What is the overall churn rate?
- Which region has the highest churn rate?
- Which subscription plan has the highest churn?
- What are the top reasons customers churn?
- How do monthly charges, tenure, and support tickets relate to churn?

## Tech Stack

- Python
- PostgreSQL
- SQL
- pandas
- SQLAlchemy
- psycopg2
- matplotlib
- python-dotenv
- VS Code
- pgAdmin

## Project Structure

```text
ai-data-analyst-agent/
│
├── Data/
│   └── customer_churn_data.csv
│
├── outputs/
│   ├── 01_preview_customer_data.csv
│   ├── 02_customer_summary.csv
│   ├── 03_overall_churn_rate.csv
│   ├── 04_churn_by_region.csv
│   ├── 05_churn_by_subscription_plan.csv
│   └── 06_top_churn_reasons.csv
│
├── charts/
│   ├── churn_by_region.png
│   ├── churn_by_subscription_plan.png
│   └── top_churn_reasons.png
│
├── sql/
│   └── churn_analysis_queries.sql
│
├── src/
│   ├── load_churn_data.py
│   ├── run_churn_queries.py
│   └── create_churn_charts.py
│
├── business_insights.md
├── requirements.txt
├── .gitignore
└── README.md
```
## Workflow

### 1. Load Data into PostgreSQL

The script `load_churn_data.py` reads the churn dataset from the `Data` folder, creates a PostgreSQL database, and loads the CSV data into a table named `customer_churn`.

```bash
python src/load_churn_data.py
```
### 2. Run Churn Analysis Queries
The script `run_churn_queries.py` connects to PostgreSQL, runs pre-written SQL queries, and saves each query result as a CSV file in the `outputs` folder.

```bash
python src/run_churn_queries.py
```
### 3. Generate Charts
The script `create_churn_charts.py` reads the output CSV files and creates visual charts in the `charts` folder.

```bash
python src/create_churn_charts.py
```
## SQL Analysis Performed

The project includes SQL analysis for:

- Customer data preview
- Total customers, churned customers, and active customers
- Overall churn rate
- Churn rate by region
- Churn rate by subscription plan
- Top churn reasons

## SQL Analysis Performed

The project includes SQL analysis for:

- Customer data preview
- Total customers, churned customers, and active customers
- Overall churn rate
- Churn rate by region
- Churn rate by subscription plan
- Top churn reasons
## Key Outputs

The analysis generates CSV outputs such as:

- `03_overall_churn_rate.csv`
- `04_churn_by_region.csv`
- `05_churn_by_subscription_plan.csv`
- `06_top_churn_reasons.csv`

These outputs are used to support business insights and visualization.
## Charts Generated

The project creates the following charts:

- Churn Rate by Region
- Churn Rate by Subscription Plan
- Top Churn Reasons
## Business Insights

The business insights are documented in `business_insights.md`.

This file explains the key findings, business meaning, and recommendations based on the churn analysis.
## Current Project Status

Till now, this project has completed the first version of the analytics pipeline:

- Created a sample customer churn dataset
- Loaded the CSV data into a PostgreSQL database using Python
- Created the `customer_churn` table automatically
- Wrote pre-defined SQL queries for churn analysis
- Automated SQL query execution using Python
- Saved each query output as a separate CSV file in the `outputs` folder
- Generated basic churn analysis charts from the saved outputs

At this stage, the project follows this workflow:

```text
Pre-written SQL queries → run automatically → save outputs
```

The next version will add natural-language-to-SQL generation, where the AI will generate SQL queries from business questions.

## Security Note

Database credentials are stored in a local `.env` file and are not pushed to GitHub.  
The `.gitignore` file prevents sensitive credentials from being uploaded.
## Future Enhancements

This project will be extended into a full AI Data Analyst Agent by adding:

- Natural-language-to-SQL generation
- AI-generated SQL validation
- Claude Code integration
- MCP server connection
- Custom analysis skills
- Automated business storytelling
- Slide deck generation