# lets say run first 6 queries from overall 10 queries
import os
from urllib.parse import quote_plus

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Load database credentials from .env file
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")

ENCODED_PASSWORD = quote_plus(POSTGRES_PASSWORD)

# Create PostgreSQL connection
engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{ENCODED_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{DATABASE_NAME}"
)

# Create outputs folder if it does not exist
OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


queries = {
    "01_preview_customer_data": """
        SELECT *
        FROM customer_churn
        LIMIT 10;
    """,

    "02_customer_summary": """
        SELECT 
            COUNT(*) AS total_customers,
            SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
            SUM(CASE WHEN churn_status = 'No' THEN 1 ELSE 0 END) AS active_customers
        FROM customer_churn;
    """,

    "03_overall_churn_rate": """
        SELECT 
            COUNT(*) AS total_customers,
            SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
            ROUND(
                SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
                2
            ) AS churn_rate_percentage
        FROM customer_churn;
    """,

    "04_churn_by_region": """
        SELECT 
            region,
            COUNT(*) AS total_customers,
            SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
            ROUND(
                SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
                2
            ) AS churn_rate_percentage
        FROM customer_churn
        GROUP BY region
        ORDER BY churn_rate_percentage DESC;
    """,

    "05_churn_by_subscription_plan": """
        SELECT 
            subscription_plan,
            COUNT(*) AS total_customers,
            SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
            ROUND(
                SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
                2
            ) AS churn_rate_percentage
        FROM customer_churn
        GROUP BY subscription_plan
        ORDER BY churn_rate_percentage DESC;
    """,

    "06_top_churn_reasons": """
        SELECT 
            churn_reason,
            COUNT(*) AS churned_customers
        FROM customer_churn
        WHERE churn_status = 'Yes'
        GROUP BY churn_reason
        ORDER BY churned_customers DESC;
    """
}


for file_name, query in queries.items():
    output_path = os.path.join(OUTPUT_FOLDER, f"{file_name}.csv")

    df = pd.read_sql(query, engine)
    df.to_csv(output_path, index=False)

    print(f"Saved: {output_path}")

print("All churn analysis outputs saved successfully.")