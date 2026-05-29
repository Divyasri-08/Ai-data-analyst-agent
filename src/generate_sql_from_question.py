import os
import re
from urllib.parse import quote_plus

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from sqlalchemy import create_engine


load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# PostgreSQL connection details
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")

ENCODED_PASSWORD = quote_plus(POSTGRES_PASSWORD)

engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{ENCODED_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{DATABASE_NAME}"
)


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_sql(question):
    schema_context = read_file("prompts/schema_context.txt")
    sql_generation_prompt = read_file("prompts/sql_generation_prompt.txt")

    final_prompt = f"""
{sql_generation_prompt}

Schema Context:
{schema_context}

Business Question:
{question}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=final_prompt,
        temperature=0
    )

    return response.output_text.strip()


def is_safe_select_query(sql_query):
    sql_lower = sql_query.lower().strip()

    blocked_keywords = [
        "insert", "update", "delete", "drop", "alter",
        "truncate", "create", "grant", "revoke"
    ]

    if sql_query in ["QUESTION_NOT_CLEAR"] or sql_query.startswith("COLUMN_NOT_FOUND"):
        return False

    if not sql_lower.startswith("select"):
        return False

    for keyword in blocked_keywords:
        if re.search(rf"\b{keyword}\b", sql_lower):
            return False

    return True


def save_query_output(sql_query, output_file_name):
    output_folder = "outputs/version_2_ai_generated_sql"
    os.makedirs(output_folder, exist_ok=True)

    df = pd.read_sql(sql_query, engine)

    output_path = f"{output_folder}/{output_file_name}.csv"
    df.to_csv(output_path, index=False)

    print(f"\nOutput saved to: {output_path}")
    print("\nQuery Result:")
    print(df)


if __name__ == "__main__":
    question = input("Enter your business question: ")

    generated_sql = generate_sql(question)

    print("\nGenerated SQL:")
    print(generated_sql)

    if not is_safe_select_query(generated_sql):
        print("\nThe generated response is not a safe SQL SELECT query.")
        print("Please rephrase the question using available columns from the schema.")
    else:
        output_file_name = input("\nEnter output file name without .csv: ")
        save_query_output(generated_sql, output_file_name)