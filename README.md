# Banking Customer & Transaction Analytics

## 📌 Project Overview

The **Banking Customer & Transaction Analytics** project is an end-to-end data analytics project focused on understanding customer profiles, account behavior, transaction patterns, payment methods, banking branches, and customer activity.

The project uses **Python, SQL, MySQL, and Power BI** to perform data cleaning, exploratory data analysis, business analysis, and visualization.

The dataset is **synthetically generated** for learning and portfolio purposes.

---

## 🎯 Business Objective

The main objective of this project is to analyze banking customer and transaction data and generate meaningful business insights.

The project focuses on:

* Understanding customer demographics
* Analyzing customer income and occupations
* Understanding account types and account balances
* Analyzing transaction behavior
* Identifying high-value transactions
* Analyzing payment methods
* Analyzing transaction categories
* Measuring transaction success and failure
* Evaluating branch performance
* Understanding customer activity
* Segmenting customers based on transaction behavior
* Performing advanced SQL business analysis
* Creating an interactive Power BI dashboard

---

## 🗂️ Dataset

The project contains four main datasets.

| Dataset      | Records | Description                                 |
| ------------ | ------: | ------------------------------------------- |
| Customers    |   5,000 | Customer demographic and income information |
| Accounts     |   5,000 | Customer account information                |
| Transactions |  50,000 | Banking transaction information             |
| Branches     |      30 | Banking branch information                  |

### Customers

Important columns:

* `customer_id`
* `name`
* `age`
* `gender`
* `city`
* `state`
* `occupation`
* `income`
* `join_date`

### Accounts

Important columns:

* `account_id`
* `customer_id`
* `branch_id`
* `account_type`
* `opening_date`
* `balance`
* `account_status`

### Transactions

Important columns:

* `transaction_id`
* `account_id`
* `transaction_date`
* `transaction_type`
* `category`
* `amount`
* `payment_mode`
* `merchant_category`
* `transaction_status`

### Branches

Important columns:

* `branch_id`
* `branch_name`
* `city`
* `state`
* `branch_type`

---

# 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **MySQL**
* **SQL**
* **Power BI**
* **Git**
* **GitHub**
* **VS Code**

---

# 📁 Project Structure

```text
banking_customer_transaction_analysis/
│
├── data/
│   ├── customers.csv
│   ├── accounts.csv
│   ├── transactions.csv
│   └── branches.csv
│
├── cleaned_data/
│   ├── customers_cleaned.csv
│   ├── accounts_cleaned.csv
│   ├── transactions_cleaned.csv
│   ├── transactions_prepared.csv
│   ├── customer_transaction_summary.csv
│   ├── customer_transaction_segments.csv
│   ├── branch_performance.csv
│   ├── account_type_performance.csv
│   ├── payment_mode_performance.csv
│   └── category_performance.csv
│
├── src/
│   ├── generate_data.py
│   ├── data_quality_analysis.py
│   ├── data_cleaning.py
│   ├── transaction_cleaning.py
│   ├── customer_eda.py
│   └── transaction_eda.py
│
├── sql/
│   ├── 01_database_setup.sql
│   ├── 02_customer_account_analysis.sql
│   ├── 03_transaction_analysis.sql
│   ├── 04_join_analysis.sql
│   ├── 05_subqueries_cte.sql
│   └── 06_window_functions.sql
│
├── visualizations/
├── powerbi/
├── reports/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🔄 Project Workflow

```text
Data Generation
       ↓
Data Quality Analysis
       ↓
Data Cleaning
       ↓
Feature Preparation
       ↓
Customer EDA
       ↓
Transaction EDA
       ↓
Customer & Transaction Analysis
       ↓
Branch Analysis
       ↓
Account Type Analysis
       ↓
Payment Mode Analysis
       ↓
Transaction Category Analysis
       ↓
SQL Business Analysis
       ↓
Power BI Dashboard
       ↓
Business Insights
       ↓
Final Report
```

---

# ✅ Project Progress

## Step 1–2 — Data Generation

Created synthetic banking datasets using Python, Pandas, NumPy and Faker.

Generated:

* 5,000 customers
* 5,000 accounts
* 50,000 transactions
* 30 branches

---

## Step 3 — Data Quality Analysis

Performed data quality checks on the raw datasets.

Checked:

* Missing values
* Duplicate records
* Invalid values
* Data types
* Date columns
* Referential integrity
* Transaction status
* Transaction type
* Transaction amount

Intentional data-quality issues were introduced into the customer dataset for cleaning practice.

---

## Step 4 — Data Cleaning

Performed cleaning on customer, account, transaction and branch datasets.

### Customer data cleaning

* Removed duplicate records
* Handled missing income values using median
* Replaced missing occupation with `Unknown`
* Replaced missing city with `Unknown`
* Converted date columns

### Final customer dataset

* 5,000 unique customers
* No duplicate records
* No missing values in important fields

---

## Step 5 — Transaction Data Preparation

Prepared transaction data for analysis.

Performed:

* Duplicate checks
* Missing-value checks
* Invalid amount checks
* Category validation
* Transaction type validation
* Payment mode validation
* Transaction status validation
* Date conversion

Added:

* `transaction_year`
* `transaction_month`
* `transaction_month_name`

---

# 📊 Python Exploratory Data Analysis

## Customer Analysis

Performed analysis of:

* Customer age distribution
* Gender distribution
* Occupation distribution
* Income distribution
* Income groups
* State distribution
* City distribution
* Customer joining trends
* Customer tenure
* Age vs income relationship
* Income group vs occupation

---

## Transaction Analysis

Performed analysis of:

* Transaction volume
* Transaction amount
* Transaction type
* Transaction category
* Payment mode
* Transaction status
* Monthly transaction patterns
* Yearly transaction analysis

---

## Customer & Transaction Analysis

Analyzed the relationship between:

```text
Customer
   ↓
Account
   ↓
Transaction
```

Created customer-level metrics such as:

* Transaction count
* Total transaction amount
* Average transaction amount
* Median transaction amount

---

## Customer Segmentation

Customers were segmented based on transaction behavior.

### Activity Segments

* Low Activity
* Medium Activity
* High Activity

### Spending Segments

* Low Spender
* Medium Spender
* High Spender

These segments are based on the project dataset and analytical thresholds and are not industry or regulatory standards.

---

# 🏦 Branch Performance Analysis

Analyzed banking branches using:

* Customer count
* Transaction count
* Total transaction amount
* Average transaction amount
* Median transaction amount
* Branch type

Also analyzed branch performance by:

* Urban
* Semi-Urban
* Rural

---

# 💳 Account Type Analysis

Analyzed different account types using:

* Customer count
* Account count
* Total balance
* Average balance
* Transaction count
* Total transaction amount
* Average transaction amount
* Active/inactive account status

---

# 💰 Payment Mode Analysis

Analyzed payment methods including:

* UPI
* Debit Card
* Credit Card
* Net Banking
* ATM

Analysis included:

* Transaction count
* Total transaction amount
* Average transaction amount
* Median transaction amount
* Success rate
* Failure rate

---

# 🛒 Transaction Category Analysis

Analyzed transaction categories including:

* Shopping
* Groceries
* Bills
* Travel
* Food
* Healthcare
* Entertainment
* Education
* Utilities
* Other

Analysis included:

* Transaction count
* Total transaction amount
* Average transaction amount
* Median transaction amount
* Transaction status
* Success rate

---

# 🗄️ SQL Business Analysis

SQL analysis was performed using **MySQL** and the queries were organized and stored in the `sql/` directory.

## SQL Topics Covered

### 1. Database and Table Creation

Created:

* `customers`
* `accounts`
* `branches`
* `transactions`

with appropriate primary keys and foreign-key relationships.

---

### 2. Customer & Account Analysis

Performed:

* Customer distribution by gender
* Customer distribution by occupation
* Customer distribution by state
* Account type analysis
* Unique customers by account type
* Average account balance
* Total account balance
* Active vs inactive accounts
* Account type and account status analysis

---

### 3. Transaction Analysis

Performed:

* Total transaction count
* Total transaction amount
* Average transaction amount
* Minimum transaction amount
* Maximum transaction amount
* Transaction type analysis
* Transaction category analysis
* Payment mode analysis
* Transaction status analysis
* Transaction success rate
* Payment mode success rate
* High-value transaction analysis
* Top transactions

---

### 4. JOIN Analysis

Used:

* `INNER JOIN`
* `LEFT JOIN`
* Multiple-table joins

Analyzed:

* Customer + account
* Customer + account + transaction
* Customer-wise transaction performance
* Branch performance
* Branch type performance
* State-wise performance
* Account type transaction performance
* Payment mode and customer behavior
* Successful transaction value by branch

---

### 5. Subqueries

Used subqueries to identify:

* Customers with above-average income
* Accounts with above-average balance
* Customers with above-average transaction value
* High-value customers

---

### 6. Common Table Expressions (CTEs)

Used CTEs for:

* Customer transaction summaries
* Branch transaction summaries
* Customer activity segmentation
* High-value customer analysis
* Customer transaction analysis

---

### 7. Window Functions

Implemented:

* `ROW_NUMBER()`
* `RANK()`
* `DENSE_RANK()`
* `COUNT() OVER()`
* `SUM() OVER()`
* `LAG()`

Used window functions for:

* Ranking transactions
* Finding top transactions
* Finding highest transaction for each customer
* Customer transaction counts
* Customer total transaction amounts
* Running totals
* Previous transaction comparison
* Top 3 transactions per customer
* Customer ranking
* Branch ranking

---

# 📌 SQL Project Files

| File                               | Purpose                           |
| ---------------------------------- | --------------------------------- |
| `01_database_setup.sql`            | Database and table creation       |
| `02_customer_account_analysis.sql` | Customer and account analysis     |
| `03_transaction_analysis.sql`      | Transaction analysis              |
| `04_join_analysis.sql`             | JOIN-based business analysis      |
| `05_subqueries_cte.sql`            | Subqueries and CTE analysis       |
| `06_window_functions.sql`          | Advanced window-function analysis |

SQL queries are developed and stored in **VS Code** and executed/tested using **MySQL Workbench**.

---

# 💡 Business Questions Answered

This project is designed to answer questions such as:

1. How are customers distributed across different states?
2. Which occupations have the highest number of customers?
3. Which account types have the highest customer base?
4. Which account types have the highest total balance?
5. What is the overall transaction volume?
6. Which transaction categories generate the highest transaction value?
7. Which payment modes are used most frequently?
8. What percentage of transactions are successful?
9. Which payment modes have higher transaction success rates?
10. Which branches generate higher transaction volumes?
11. Which branches generate higher transaction values?
12. Which account types have higher transaction activity?
13. Who are the high-value customers?
14. Which customers have high transaction activity?
15. What are the highest-value transactions?
16. How do customers compare based on their transaction behavior?

---

# 📈 Key Analytical Areas

The project focuses on four major business dimensions:

### Customer

```text
Demographics
Income
Occupation
Location
Tenure
Activity
```

### Account

```text
Account Type
Balance
Account Status
Branch
```

### Transaction

```text
Transaction Type
Category
Amount
Payment Mode
Status
Date
```

### Branch

```text
Branch Type
Location
Customers
Transactions
Transaction Value
```

---

# ⚠️ Data Disclaimer

This project uses **synthetically generated data** for educational and portfolio purposes.

The geographic, demographic and transaction behavior patterns in this dataset should not be interpreted as real-world banking trends or causal relationships.

---

# 🚀 Future Development

The next stage of the project is:

## Power BI Dashboard Development

Planned dashboard areas:

* Banking KPI Overview
* Customer Analysis
* Account Analysis
* Transaction Analysis
* Payment Mode Analysis
* Branch Performance
* Customer Segmentation
* Interactive filters and slicers

---

# 👨‍💻 Author

**Onkar Kadam**

Data Science / Data Analytics Enthusiast

Skills:

* Python
* SQL
* MySQL
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Power BI
* Machine Learning
* Data Analysis
* Git & GitHub

