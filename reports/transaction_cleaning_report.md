# Transaction Cleaning Report

## Project: Banking Customer & Transaction Analytics

### 1. Objective

The objective of Day 5 was to validate and prepare the transaction dataset for further Data Analysis, SQL analysis, visualization, and Power BI reporting.

The cleaned transaction dataset from Day 4 was used as the input. The original raw transaction data was not modified.

---

## 2. Dataset Overview

| Attribute              | Details              |
| ---------------------- | -------------------- |
| Dataset                | Banking Transactions |
| Records                | 50,000               |
| Original Columns       | 9                    |
| Final Columns          | 12                   |
| Duplicate Transactions | 0                    |
| Missing Values         | 0                    |
| Invalid Amounts        | 0                    |

---

## 3. Data Validation

### 3.1 Duplicate Transactions

The transaction dataset was checked for duplicate records.

Result:

* Duplicate transactions: **0**

No duplicate transaction records were found.

---

### 3.2 Missing Values

All transaction columns were checked for missing values.

Result:

* Total missing values: **0**

No missing values were found in the transaction dataset.

---

### 3.3 Transaction Amount Validation

Transaction amounts were checked for zero and negative values.

The validation condition used was:

```python
amount <= 0
```

Result:

* Invalid transaction amounts: **0**

All transaction amounts are valid positive values.

---

### 3.4 Transaction Category Validation

Transaction categories were validated against the expected business categories:

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

Result:

* Invalid transaction categories: **0**

---

### 3.5 Transaction Type Validation

The `transaction_type` column was validated against:

* Debit
* Credit

Result:

* Invalid transaction types: **0**

---

### 3.6 Payment Mode Validation

The `payment_mode` column was validated against:

* UPI
* Debit Card
* Credit Card
* Net Banking
* ATM

Result:

* Invalid payment modes: **0**

---

### 3.7 Transaction Status Validation

The `transaction_status` column was validated against:

* Success
* Failed
* Pending

Result:

* Invalid transaction statuses: **0**

---

## 4. Transaction Date Validation

The `transaction_date` column was converted to Pandas `datetime` format.

The minimum and maximum transaction dates were checked to understand the time period covered by the dataset.

This will support future:

* Monthly analysis
* Yearly analysis
* Transaction trend analysis
* Debit vs Credit trend analysis

---

## 5. Feature Creation

Three analytical features were created from `transaction_date`:

### `transaction_year`

Stores the year of the transaction.

### `transaction_month`

Stores the numerical month of the transaction.

### `transaction_month_name`

Stores the month name, such as January, February, March, etc.

These features will make time-based analysis easier in Python, SQL, and Power BI.

---

## 6. Final Dataset

The prepared transaction dataset contains:

**50,000 rows × 12 columns**

The final columns are:

```text
transaction_id
account_id
transaction_date
transaction_type
category
amount
payment_mode
merchant_category
transaction_status
transaction_year
transaction_month
transaction_month_name
```

---

## 7. Output File

The prepared dataset was saved as:

```text
cleaned_data/transactions_prepared.csv
```

The original raw transaction dataset remains unchanged.

---

## 8. Conclusion

The Day 5 transaction cleaning and preparation process was completed successfully.

The transaction dataset has been validated for duplicates, missing values, invalid amounts, categories, transaction types, payment modes, and transaction statuses.

Additional date-based analytical features were also created.

The prepared transaction dataset is now ready for:

* Exploratory Data Analysis
* Transaction trend analysis
* Customer spending analysis
* Payment mode analysis
* Debit vs Credit analysis
* Transaction status analysis
* SQL analysis
* Power BI dashboard development

**Status: Transaction Cleaning & Preparation Completed**
