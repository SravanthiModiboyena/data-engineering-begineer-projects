\# SQL Retail Analytics Project



\## 📌 Project Overview

This project analyzes retail sales data using SQL. 

The goal is to generate business insights such as total revenue, top products, and regional performance.



---



\## 🛠 Tools Used

\- MySQL

\- SQL (Advanced Queries)



---



\## 📂 Dataset Description



The dataset contains the following columns:



\- order\_id

\- customer\_id

\- product

\- category

\- quantity

\- price

\- order\_date

\- region



---



\## 🔍 SQL Concepts Covered



\- Aggregation (SUM, GROUP BY)

\- Sorting (ORDER BY)

\- Filtering

\- Window Functions (RANK)

\- Indexing (Performance Optimization)



---



\## 📊 Analysis Performed



\### 1️⃣ Total Revenue

Calculated total revenue using:

quantity \* price



\### 2️⃣ Revenue by Region

Identified highest performing regions.



\### 3️⃣ Top Products

Ranked products based on revenue.



\### 4️⃣ Monthly Revenue

Analyzed sales trends by month.



\### 5️⃣ Indexing

Created index on `region` column to improve performance.



```sql

CREATE INDEX idx\_region ON sales(region);

```



---



\## 🚀 Key Insights



\- Electronics category generated highest revenue.

\- South and North regions performed strongly.

\- Laptop is one of the top-selling products.



---



\## 📁 Project Structure



```

1\_sql\_retail\_analytics/

│

├── sales\_data.csv

├── queries.sql

└── README.md

```



---



\## 👩‍💻 Author

Sravanthi



