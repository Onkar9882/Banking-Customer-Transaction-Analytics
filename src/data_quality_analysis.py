import pandas as pd 

## Load all 4 datasets
customers_df = pd.read_csv("data/customers.csv")
accounts_df = pd.read_csv("data/accounts.csv")
transactions_df = pd.read_csv("data/transactions.csv")
branches_df = pd.read_csv("data/branches.csv")

print("All datasets loaded successfully")

## Check dataset dimensions

print("\n--- Dataset shape ---")

print("Customers :", customers_df.shape)
print("Accounts :", accounts_df.shape)
print("Transactions :", transactions_df.shape)
print("Branches :", branches_df.shape)

## Inspect the first records
print("\n --- Customers ---")
print(customers_df.head())

print("\n --- Accounts ---")
print(accounts_df.head())

print("\n --- Transactions ---")
print(transactions_df.head())

print("\n --- Branches ---")
print(branches_df.head())


## Check Data Types

print("\n --- Customers Data Types ---")
print(customers_df.dtypes)

print("\n --- Accounts Data Types ---")
print(accounts_df.dtypes)

print("\n --- Transactions Data Types ---")
print(transactions_df.dtypes)

print("\n --- Branches Data Types ---")
print(branches_df.dtypes)

## Convert Date Columns
customers_df["join_date"] = pd.to_datetime(customers_df["join_date"])

accounts_df["opening_date"] = pd.to_datetime(accounts_df["opening_date"])

transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"])

print("\n --- Updated Date Types ---")
print("Customer join date :", customers_df["join_date"].dtype)
print("Accounts opening date :", accounts_df["opening_date"].dtype)
print("Transaction Date :", transactions_df["transaction_date"].dtype)


## Check Missing Values
print("\n ---- Missing Values ----")

print("\nCustomers:")
print(customers_df.isnull().sum())

print("\n Accounts:")
print(accounts_df.isnull().sum())

print("\n Transactions:")
print(transactions_df.isnull().sum())

print("\n Branches:")
print(branches_df.isnull().sum())


## Check Duplicate Records
print("\n ---- Duplicate Records ----")

print("Customers Duplicates:", customers_df.duplicated().sum())
print("Accounts Duplicates:", accounts_df.duplicated().sum())
print("Transactions Duplicates:", transactions_df.duplicated().sum())
print("Branches Duplicates:", branches_df.duplicated().sum())

#Validate Customer Data

print("\n --- Customer Data Validation ---")

#Age Validation
invalid_age = customers_df[(customers_df["age"]) < 18 | (customers_df["age"] > 100)]
print("Invalid Ages:", len(invalid_age))

## income Validation
invalid_income = customers_df[customers_df["income"] < 0]
print("Invalid Income:", len(invalid_income))

#Gender validation
valid_genders = ["Male", "Female"]
invalid_gender = customers_df[~customers_df["gender"].isin(valid_genders)]
print("Invalid Gender:", len(invalid_gender))


#Validate Account Data
print("\n --- Account Data validation ---")

# Negative balance check
invalid_balance = accounts_df[accounts_df["balance"] < 0]
print("Negative Balance:", len(invalid_balance))

# Account type validation
valid_account_types = ["Savings","Current","Salary","Business"]
invalid_account_types = accounts_df[~accounts_df["account_type"].isin(valid_account_types)]
print("Invalid account types:", len(invalid_account_types))

# Account status validation
valid_status = ["Active", "Inactive"]
invalid_status = accounts_df[~accounts_df["account_status"].isin(valid_status)]
print("Invalid Status:", len(invalid_status))


#Validate Transactions
print("\n --- Transaction Data Validation ---")

# Transaction amount validation
invalid_amount = transactions_df[transactions_df["amount"] <= 0]
print("Invalid Transaction Amount:", len(invalid_amount))

# Transaction type validation
valid_transaction_types = ["Debit", "Credit"]
invalid_transaction_type = transactions_df[~transactions_df["transaction_type"].isin(valid_transaction_types)]
print("Invalid transaction types:", len(invalid_transaction_type))

# Transaction status validation
valid_transaction_status = [
    "Success",
    "Failed",
    "Pending"
]
invalid_transaction_status = transactions_df[~transactions_df["transaction_status"].isin(valid_transaction_status)]
print("Invalid transaction statuses:", len(invalid_transaction_status))

#Validate Relationships
print("\n --- Referential Integrity Checks ---")

invalid_customer_id = accounts_df[~accounts_df["customer_id"].isin(customers_df["customer_id"])]
print("Accounts with invalid customer ids", len(invalid_customer_id))

invalid_branch_ids = accounts_df[~accounts_df["branch_id"].isin(branches_df["branch_id"])]
print("Accounts with Invalid branches ids:", len(invalid_branch_ids))

invalid_account_ids = transactions_df[~transactions_df["account_id"].isin(accounts_df["account_id"])]
print("Transactions with invalid account ids:", len(invalid_account_ids))


print("\n--- Final Data Quality Summary ---")

quality_summary = {
    "customers_rows": len(customers_df),
    "customer_duplicates": customers_df.duplicated().sum(),
    "customer_missing_values": customers_df.isnull().sum().sum(),
    "accounts_rows": len(accounts_df),
    "account_duplicates": accounts_df.duplicated().sum(),
    "transactions_rows": len(transactions_df),
    "transaction_duplicates": transactions_df.duplicated().sum(),
    "branches_rows": len(branches_df),
    "branch_duplicates": branches_df.duplicated().sum()
}

for key, value in quality_summary.items():
    print(f"{key}: {value}")