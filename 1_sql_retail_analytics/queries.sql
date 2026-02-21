-- use Database 
use retail_db;

Select * from sales;

-- Total Revenue 
SELECT SUM(quantity * price) AS total_revenue
FROM sales;

-- Revenue by region 
SELECT region,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- Top 3 Products 
SELECT product,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 3;

-- Monthly revenue 
SELECT MONTH(order_date) AS month,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY MONTH(order_date);

-- Window Function Ranking 
SELECT product,
       SUM(quantity * price) AS revenue,
       RANK() OVER (ORDER BY SUM(quantity * price) DESC) AS ranking
FROM sales
GROUP BY product;

-- Create Index for Performance Optimization
CREATE INDEX idx_region
ON sales(region);


-- Verify Index
SHOW INDEX FROM sales;

