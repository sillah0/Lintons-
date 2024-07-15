/*
    This query selects the top 5 products based on the total 
    quantity purchased in the last month.
*/

SELECT product_id, SUM(quantity) AS total_quantity
FROM customer_purchase
WHERE purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
GROUP BY product_id
ORDER BY total_quantity DESC
LIMIT 5;
