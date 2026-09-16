# Data Quality Report

## Project

Banking Customer & Transaction Analytics

## 1. Dataset Overview

| Dataset | Rows | Columns |
|---|---:|---:|
| Customers | 5,005 | 9 |
| Accounts | 5,000 | 7 |
| Transactions | 50,000 | 9 |
| Branches | 30 | 5 |

## 2. Data Quality Findings

### Customers

- 5 duplicate records identified.
- 5 missing occupation values.
- 5 missing income values.
- 3 missing city values.
- Age values are within the expected range.
- Income values are non-negative.
- Gender values contain only valid categories.

### Accounts

- No duplicate records identified.
- No missing values identified.
- No negative account balances identified.
- Account types contain valid categories.
- Account status values contain valid categories.

### Transactions

- No duplicate records identified.
- No missing values identified.
- Transaction amounts are positive.
- Transaction types contain valid categories.
- Transaction statuses contain valid categories.

### Branches

- No duplicate records identified.
- No missing values identified.

## 3. Referential Integrity

The relationships between the datasets were validated.

- All accounts have valid customer IDs.
- All accounts have valid branch IDs.
- All transactions have valid account IDs.

## 4. Conclusion

The datasets contain a small number of intentionally introduced quality issues in the customer dataset. These issues will be addressed during the data-cleaning stage before performing exploratory analysis and business analysis.