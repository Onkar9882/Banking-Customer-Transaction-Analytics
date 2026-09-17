# Data Cleaning Report

## Project: Banking Customer & Transaction Analytics

### 1. Objective

The objective of this step was to clean the raw banking datasets and prepare them for further Data Analysis, SQL analysis, visualization, and Power BI reporting.

The raw datasets were kept unchanged, and the cleaned datasets were stored separately in the `cleaned_data` folder.

---

## 2. Datasets Cleaned

The following datasets were cleaned:

| Dataset      | Original Rows | Final Rows | Columns |
| ------------ | ------------: | ---------: | ------: |
| Customers    |          5005 |       5000 |       9 |
| Accounts     |          5000 |       5000 |       7 |
| Transactions |         50000 |      50000 |       9 |
| Branches     |            30 |         30 |       5 |

---

## 3. Data Cleaning Operations

### 3.1 Duplicate Removal

The customer dataset contained **5 duplicate rows**.

These duplicate records were removed using Pandas `drop_duplicates()`.

Result:

* Duplicates before cleaning: 5
* Duplicates after cleaning: 0

The final customer dataset contains **5,000 unique customer records**.

---

### 3.2 Missing Income Values

The customer dataset contained **5 missing income values**.

Since income is a numerical variable and can contain extreme values, the **median income** was used to fill the missing values.

This approach prevents missing income values from being treated as zero and is less affected by extreme income values than the mean.

Result:

* Missing income before cleaning: 5
* Missing income after cleaning: 0

---

### 3.3 Missing Occupation Values

The customer dataset contained **5 missing occupation values**.

Because occupation is a categorical variable and the actual occupation could not be determined reliably, the missing values were replaced with:

`Unknown`

Result:

* Missing occupation before cleaning: 5
* Missing occupation after cleaning: 0

---

### 3.4 Missing City Values

The customer dataset contained **3 missing city values**.

Since the actual city could not be determined from the available data, the missing values were replaced with:

`Unknown`

Result:

* Missing city before cleaning: 3
* Missing city after cleaning: 0

---

### 3.5 Date Conversion

The following columns were converted into Pandas `datetime` format:

* `customers.join_date`
* `accounts.opening_date`
* `transactions.transaction_date`

This will make it easier to perform time-based analysis such as monthly trends, yearly analysis, and transaction-date analysis.

---

## 4. Final Validation

After completing the cleaning process, all datasets were validated again.

### Missing Values

* Customers: 0
* Accounts: 0
* Transactions: 0
* Branches: 0

### Duplicate Records

* Customers: 0
* Accounts: 0
* Transactions: 0
* Branches: 0

The final validation confirmed that the identified missing values and duplicate records were successfully handled.

---

## 5. Cleaned Data Location

The cleaned datasets were saved in:

```text
cleaned_data/
├── customers_cleaned.csv
├── accounts_cleaned.csv
├── transactions_cleaned.csv
└── branches_cleaned.csv
```

The original raw datasets remain unchanged in:

```text
data/
```

---

## 6. Conclusion

The Day 4 data cleaning process was completed successfully. The datasets are now cleaned, validated, and ready for the next stages of the project.

The cleaned data will be used for:

* Exploratory Data Analysis
* Customer behavior analysis
* Transaction analysis
* SQL queries
* Business KPI analysis
* Data visualization
* Power BI dashboard development

**Status: Data Cleaning Completed**
