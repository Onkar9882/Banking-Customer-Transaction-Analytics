# Power BI Dashboard

## Banking Customer & Transaction Analytics

This folder contains the Power BI dashboard developed for the Banking Customer & Transaction Analytics project.

## Dashboard Pages

### 1. Overview

Provides a high-level view of banking data using key performance indicators and summary visuals.

Key areas:

* Total Customers
* Total Accounts
* Total Transactions
* Total Transaction Amount
* Average Transaction Amount
* Total Account Balance
* Customer distribution
* Account type distribution
* Transaction category analysis

### 2. Customer Analysis

Analyzes customer demographics and financial characteristics.

Key areas:

* Gender distribution
* Age groups
* Occupation
* Income groups
* State-wise customer distribution
* Age vs Income analysis

### 3. Transaction Analysis

Analyzes transaction behavior and transaction performance.

Key areas:

* Transaction volume
* Transaction amount
* Transaction type
* Transaction category
* Payment mode
* Transaction status
* Success rate
* Monthly transaction trends
* High-value transactions

### 4. Branch & Account Analysis

Analyzes branch performance and account behavior.

Key areas:

* Accounts by branch
* Transactions by branch
* Transaction amount by branch
* Branch type analysis
* Account type distribution
* Account balance by account type
* Active and inactive accounts
* Account status by account type

### 5. Customer Segmentation

Analyzes customers based on transaction activity and spending behavior.

Segments used:

* Low Activity
* Medium Activity
* High Activity
* Low Spender
* Medium Spender
* High Spender

Key areas:

* Customer activity segments
* Customer spending segments
* Activity vs spending
* Average transactions by activity segment
* Transaction amount by spending segment
* Customer-level segmentation details

## Data Sources

The dashboard uses the cleaned datasets generated during the project:

* `customers_cleaned.csv`
* `accounts_cleaned.csv`
* `transactions_prepared.csv`
* `branches.csv`
* `customer_transaction_segments.csv`

## Power BI Features Used

* Data modeling
* Relationships
* DAX measures
* Calculated columns
* KPI cards
* Bar charts
* Column charts
* Donut charts
* Line charts
* Tables
* Slicers
* Filters

## Data Model

The main relationships are:

```text
Customers
    |
    | 1 : *
    ↓
Accounts
    |
    | 1 : *
    ↓
Transactions

Branches
    |
    | 1 : *
    ↓
Accounts
```

## Tools

* Power BI Desktop
* DAX
* CSV datasets

## Note

The dataset used in this project is synthetic and created for learning, portfolio, and demonstration purposes. The customer, transaction, branch, and demographic values do not represent real banking customers or real banking activity.
