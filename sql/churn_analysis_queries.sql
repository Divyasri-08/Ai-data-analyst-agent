-- 1. View first 10 records
SELECT *
FROM customer_churn
LIMIT 10;


-- 2. Total customers and churned customers
SELECT 
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    SUM(CASE WHEN churn_status = 'No' THEN 1 ELSE 0 END) AS active_customers
FROM customer_churn;


-- 3. Overall churn rate
SELECT 
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn;


-- 4. Churn rate by region
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


-- 5. Churn rate by subscription plan
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


-- 6. Churn by contract type
SELECT 
    contract_type,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn
GROUP BY contract_type
ORDER BY churn_rate_percentage DESC;


-- 7. Top churn reasons
SELECT 
    churn_reason,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE churn_status = 'Yes'
GROUP BY churn_reason
ORDER BY churned_customers DESC;


-- 8. Average monthly charges by churn status
SELECT 
    churn_status,
    ROUND(AVG(monthly_charges), 2) AS avg_monthly_charges
FROM customer_churn
GROUP BY churn_status;


-- 9. Average tenure by churn status
SELECT 
    churn_status,
    ROUND(AVG(tenure_months), 2) AS avg_tenure_months
FROM customer_churn
GROUP BY churn_status;


-- 10. Support tickets by churn status
SELECT 
    churn_status,
    ROUND(AVG(support_tickets), 2) AS avg_support_tickets
FROM customer_churn
GROUP BY churn_status;