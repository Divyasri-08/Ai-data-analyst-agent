import os
from urllib.parse import quote_plus

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


# Load environment variables from .env file
load_dotenv()

# PostgreSQL login details from .env
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

# Database and table details from .env
DATABASE_NAME = os.getenv("DATABASE_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")

# CSV file path
CSV_FILE_PATH = "Data/customer_churn_data.csv"

# Encode password to safely handle special characters like @, #, $, %
ENCODED_PASSWORD = quote_plus(POSTGRES_PASSWORD)


def create_database():
    default_engine = create_engine(
        f"postgresql+psycopg2://{POSTGRES_USER}:{ENCODED_PASSWORD}@"
        f"{POSTGRES_HOST}:{POSTGRES_PORT}/postgres",
        isolation_level="AUTOCOMMIT"
    )

    with default_engine.connect() as connection:
        result = connection.execute(
            text(f"SELECT 1 FROM pg_database WHERE datname = '{DATABASE_NAME}'")
        )

        database_exists = result.scalar()

        if not database_exists:
            connection.execute(text(f"CREATE DATABASE {DATABASE_NAME}"))
            print(f"Database created: {DATABASE_NAME}")
        else:
            print(f"Database already exists: {DATABASE_NAME}")


def load_csv_to_postgres():
    df = pd.read_csv(CSV_FILE_PATH)

    project_engine = create_engine(
        f"postgresql+psycopg2://{POSTGRES_USER}:{ENCODED_PASSWORD}@"
        f"{POSTGRES_HOST}:{POSTGRES_PORT}/{DATABASE_NAME}"
    )

    df.to_sql(TABLE_NAME, project_engine, if_exists="replace", index=False)

    print(f"CSV loaded successfully into table: {TABLE_NAME}")
    print(f"Total rows loaded: {len(df)}")


if __name__ == "__main__":
    create_database()
    load_csv_to_postgres()