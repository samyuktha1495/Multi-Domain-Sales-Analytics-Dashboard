# Multi-Domain-Sales-Analytics-Dashboard
Data Analytics project using Python, SQL Server, and Power BI to analyze return abuse, discount effectiveness, suspicious reviews, and late delivery patterns.
# Multi-Domain Sales Analytics Dashboard

Data Analytics project using **Python, SQL Server, and Power BI** to analyze key e-commerce business problems including **return abuse, discount effectiveness, suspicious reviews, and late delivery patterns**.

## 📌 Project Overview

This project demonstrates an end-to-end data analytics workflow:

**Raw Data → Data Cleaning → SQL Analysis → Business Insights → Power BI Dashboard**

The project uses Python for data preprocessing, SQL Server for data storage and analysis, and Power BI for interactive visualization.

## 🎯 Business Problems

### 1. Return Abuse Analysis
Identifies customers with unusually high return activity and analyzes:
- Return frequency
- Number of returned items
- Total return value
- First and last return dates

### 2. Discount Effectiveness Analysis
Evaluates the performance of products with and without discounts using:
- Total sales
- Quantity sold
- Number of orders
- Average order value
- Discount performance

### 3. Suspicious Review Analysis
Analyzes reviewer behavior to identify potentially suspicious reviewing patterns based on:
- Number of reviews
- Rating diversity
- Minimum and maximum ratings
- Reviewer activity

> Suspicious patterns are indicators for further investigation and do not by themselves prove fraudulent activity.

### 4. Late Delivery Analysis
Analyzes delivery performance across customers and sellers using:
- Total orders
- Late orders
- Late delivery percentage
- Average delivery delay
- Customer location
- Seller location

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **SQL Server**
- **SQL**
- **Power BI**
- **Git & GitHub**

## 📂 Project Structure

```text
Multi-Domain-Sales-Analytics-Dashboard/
│
├── Python/
│   ├── deliveries_customers_cleaning.py
│   ├── deliveries_items_cleaning.py
│   ├── deliveries_orders_cleaning.py
│   ├── deliveries_sellers_cleaning.py
│   ├── discounts_cleaning.py
│   ├── returns_cleaning.py
│   └── reviews_cleaning.py
│
├── SQL/
│   ├── create_database.sql
│   ├── create_table.sql
│   ├── load_deliveries_customers.sql
│   ├── load_deliveries_orders.sql
│   ├── load_deliveries_order_items.sql
│   ├── load_deliveries_sellers.sql
│   ├── load_discounts.sql
│   ├── load_returns.sql
│   ├── load_reviews.sql
│   ├── returnabuse_view.sql
│   ├── returnabuse_finalquery.sql
│   ├── discounteffectiveness_view.sql
│   ├── discounteffectiveness_finalquery.sql
│   ├── suspiciousreviews_view.sql
│   ├── suspiciousreviews_finalquery.sql
│   ├── latedelivery_view.sql
│   └── latedelivery_finalquery.sql
│
├── DA2.pbix
└── README.md
