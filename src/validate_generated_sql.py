import re


VALID_TABLES = ["customer_churn"]

VALID_COLUMNS = [
    "customer_id",
    "customer_name",
    "region",
    "subscription_plan",
    "monthly_charges",
    "tenure_months",
    "contract_type",
    "payment_method",
    "support_tickets",
    "churn_status",
    "churn_reason"
]


BLOCKED_KEYWORDS = [
    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "truncate",
    "create",
    "grant",
    "revoke"
]


SQL_KEYWORDS_AND_FUNCTIONS = [
    "select", "from", "where", "group", "by", "order", "desc", "asc",
    "as", "case", "when", "then", "else", "end", "sum", "count",
    "round", "avg", "min", "max", "numeric", "and", "or", "not",
    "is", "null", "limit", "distinct"
]


def validate_sql(sql_query):
    """
    Validates AI-generated SQL before execution.
    Returns: (is_valid, message)
    """

    sql_lower = sql_query.lower().strip()

    if sql_query == "QUESTION_NOT_CLEAR":
        return False, "Question is unclear. Please rephrase the question."

    if sql_query.startswith("COLUMN_NOT_FOUND"):
        return False, sql_query

    if not sql_lower.startswith("select"):
        return False, "Invalid SQL: Only SELECT queries are allowed."

    for keyword in BLOCKED_KEYWORDS:
        if re.search(rf"\b{keyword}\b", sql_lower):
            return False, f"Unsafe SQL detected: {keyword.upper()} is not allowed."

    table_names = re.findall(r"\bfrom\s+([a-zA-Z_][a-zA-Z0-9_]*)", sql_lower)

    for table in table_names:
        if table not in VALID_TABLES:
            return False, f"TABLE_NOT_FOUND: {table}"

    possible_identifiers = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", sql_lower)

    allowed_words = set(VALID_COLUMNS + VALID_TABLES + SQL_KEYWORDS_AND_FUNCTIONS)

    for word in possible_identifiers:
        if word in allowed_words:
            continue

        # Ignore output aliases like churn_rate, total_customers, churn_count, etc.
        if word in [
            "churn_rate",
            "total_customers",
            "churned_customers",
            "active_customers",
            "average_monthly_charge",
            "avg_monthly_charges",
            "average_tenure",
            "avg_tenure_months",
            "avg_support_tickets",
            "churn_count"
        ]:
            continue

        # Ignore string values from SQL filters
        if word in ["yes", "no"]:
            continue

        return False, f"COLUMN_NOT_FOUND: {word}"

    return True, "SQL validation passed."