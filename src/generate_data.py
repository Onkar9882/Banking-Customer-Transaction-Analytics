import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker("en_IN")

random.seed(42)
np.random.seed(42)

## Generate customer ID
num_customers = 5000
customer_ids = [f"C{i:05d}" for i in range(1, num_customers + 1)]
print(customer_ids[:5])

customers = []

for customer_id in customer_ids:
    customer = {
        "customer_id": customer_id,
        "name": fake.name(),
        "age": random.randint(21, 65),
        "gender": random.choice(["Male", "Female"]),
        "city": fake.city(),
        "state": fake.state(),
        "occupation": random.choice([
            "Software Engineer",
            "Teacher",
            "Business Owner",
            "Doctor",
            "Accountant",
            "Government Employee",
            "Student",
            "Sales Executive",
            "Farmer",
            "Other"
        ]),
        "income": random.randint(20000, 200000),
        "join_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    }

    customers.append(customer)

customers_df = pd.DataFrame(customers)

print(customers_df.head())
print(customers_df.shape)

# Introduce some missing values
customers_df.loc[10:14, "occupation"] = np.nan
customers_df.loc[20:24, "income"] = np.nan
customers_df.loc[30:32, "city"] = np.nan

# Introduce duplicate records
duplicate_rows = customers_df.iloc[100:105].copy()

customers_df = pd.concat(
    [customers_df, duplicate_rows],
    ignore_index=True
)

print("Shape after data issues:", customers_df.shape)

## Save the customer dataset
customers_df.to_csv("data/customers.csv", index=False)
print("customers.csv is created successfully")


## Create branches.csv
num_branches = 30

branches = [] 

for i in range(1, num_branches + 1):

    branch = {
        "branch_id": f"B{i:03d}",
        "branch_name": f"Branch {i}",
        "city": fake.city(),
        "state": fake.state(),
        "branch_type": random.choice([
            "Urban",
            "Semi-Urban",
            "Rural"
        ])
    }

    branches.append(branch)

branches_df = pd.DataFrame(branches)
print(branches_df.head())
print(branches_df.shape)

branches_df.to_csv("data/branches.csv", index=False)
print("branches.csv created successfully")


## Generate Account IDs
num_accounts = 5000
account_ids = [f"A{i:05d}"for i in range(1, num_accounts + 1)]

print(account_ids[:5])


accounts = []

for i, account_id in enumerate(account_ids):
    account = {
        "account_id": account_id,
        "customer_id": customer_ids[i],
        "branch_id": random.choice(branches_df["branch_id"]),
        "account_type": random.choice([
            "Savings",
            "Current",
            "Salary",
            "Business"
        ]),
        "opening_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        ),
        "balance": round(random.uniform(5000, 500000), 2),
        "account_status": random.choice([
            "Active",
            "Active",
            "Active",
            "Inactive"
        ])
    }

    accounts.append(account)

accounts_df = pd.DataFrame(accounts)
print(accounts_df.head())
print(accounts_df.shape)


accounts_df.to_csv("data/accounts.csv", index=False)
print("accounts.csv created successfully")


## Create transactions.csv
num_transactions = 50000

transactions = []

transaction_categories = [
    "Shopping",
    "Groceries",
    "Bills",
    "Travel",
    "Food",
    "Healthcare",
    "Entertainment",
    "Education",
    "Utilities",
    "Other"
]

payment_modes = [
    "UPI",
    "Debit Card",
    "Credit Card",
    "Net Banking",
    "ATM"
]

merchant_categories = [
    "Retail",
    "Grocery",
    "Restaurant",
    "Fuel",
    "Healthcare",
    "Travel",
    "Online",
    "Education",
    "Utility",
    "Other"
]

for i in range(1, num_transactions + 1):

    transaction = {
        "transaction_id": f"T{i:06d}",
        "account_id": random.choice(account_ids),
        "transaction_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "transaction_type": random.choice([
            "Debit",
            "Credit"
        ]),
        "category": random.choice(transaction_categories),
        "amount": round(random.uniform(100, 100000), 2),
        "payment_mode": random.choice(payment_modes),
        "merchant_category": random.choice(merchant_categories),
        "transaction_status": random.choices(
            ["Success", "Failed", "Pending"],
            weights=[92, 5, 3],
            k=1
        )[0]
    }

    transactions.append(transaction)


transactions_df = pd.DataFrame(transactions)

print(transactions_df.head())
print(transactions_df.shape)

transactions_df.to_csv("data/transactions.csv", index=False)
print("transactions.csv created successfully")


## Verify all 4 datasets
print("\n--- Dataset Summary ---")

print("Customers:", customers_df.shape)
print("Accounts:", accounts_df.shape)
print("Transactions:", transactions_df.shape)
print("Branches:", branches_df.shape)

print("\n--- Missing Values ---")
print(customers_df.isnull().sum())

print("\n--- Duplicate Customers ---")
print(customers_df.duplicated().sum())

print("\n--- Transaction Status ---")
print(transactions_df["transaction_status"].value_counts())

## Check relationships
print("\n--- Relationship Checks ---")

print(
    "Invalid customer IDs:",
    (~accounts_df["customer_id"].isin(customers_df["customer_id"])).sum()
)

print(
    "Invalid branch IDs:",
    (~accounts_df["branch_id"].isin(branches_df["branch_id"])).sum()
)

print(
    "Invalid account IDs:",
    (~transactions_df["account_id"].isin(accounts_df["account_id"])).sum()
)

