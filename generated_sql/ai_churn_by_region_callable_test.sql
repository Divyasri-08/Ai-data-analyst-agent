SELECT region, 
       ROUND(SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END)::numeric / COUNT(*) * 100, 2) AS churn_rate
FROM customer_churn
GROUP BY region
ORDER BY churn_rate DESC
LIMIT 1;