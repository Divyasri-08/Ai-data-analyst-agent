import os
import pandas as pd
import matplotlib.pyplot as plt


# Create charts folder if it does not exist
CHARTS_FOLDER = "charts"
os.makedirs(CHARTS_FOLDER, exist_ok=True)


# -----------------------------
# Chart 1: Churn by Region
# -----------------------------
region_df = pd.read_csv("outputs/04_churn_by_region.csv")

plt.figure(figsize=(8, 5))
plt.bar(region_df["region"], region_df["churn_rate_percentage"])
plt.title("Churn Rate by Region")
plt.xlabel("Region")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("charts/churn_by_region.png")
plt.close()

print("Saved: charts/churn_by_region.png")


# -----------------------------
# Chart 2: Churn by Subscription Plan
# -----------------------------
plan_df = pd.read_csv("outputs/05_churn_by_subscription_plan.csv")

plt.figure(figsize=(8, 5))
plt.bar(plan_df["subscription_plan"], plan_df["churn_rate_percentage"])
plt.title("Churn Rate by Subscription Plan")
plt.xlabel("Subscription Plan")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("charts/churn_by_subscription_plan.png")
plt.close()

print("Saved: charts/churn_by_subscription_plan.png")


# -----------------------------
# Chart 3: Top Churn Reasons
# -----------------------------
reason_df = pd.read_csv("outputs/06_top_churn_reasons.csv")

plt.figure(figsize=(8, 5))
plt.bar(reason_df["churn_reason"], reason_df["churned_customers"])
plt.title("Top Churn Reasons")
plt.xlabel("Churn Reason")
plt.ylabel("Number of Churned Customers")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/top_churn_reasons.png")
plt.close()

print("Saved: charts/top_churn_reasons.png")


print("All churn charts created successfully.")