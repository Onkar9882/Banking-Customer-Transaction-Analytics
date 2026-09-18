import pandas as pd 

#Load raw datasets
customers_df = pd.read_csv("data/customers.csv")
accounts_df = pd.read_csv("data/accounts.csv")
transactions_df = pd.read_csv("data/transactions.csv")
branches_df = pd.read_csv("data/branches.csv")

print("Raw Dataset load successfully")

print("\n === Dataset Shape ===")
print("Customers: ",customers_df.shape)
print("Accounts: ", accounts_df.shape)
print("Transactions: ", transactions_df.shape)
print("Branches: ", branches_df.shape)

# Check duplicate customers before cleaning
duplicate_count = customers_df.duplicated().sum()

print("\nDuplicate customer before cleaning:",duplicate_count)

# Remove duplicate customer records
customers_df = customers_df.drop_duplicates().reset_index(drop=True)

# Check duplicates after cleaning
duplicate_count_after = customers_df.duplicated().sum()

print("Duplicate customers after cleaning :",duplicate_count_after)
print("Customer shape after removing duplicates :",customers_df.shape)

# Check missing income values
missing_income = customers_df["income"].isnull().sum()
print("\nMissing income values before cleaning: ",missing_income)

print("Customers with missing income:")
print(customers_df[customers_df["income"].isnull()][["customer_id","age","occupation","income"]])

median_income = customers_df["income"].median()
print("\nMedian income:",median_income)

customers_df["income"] = customers_df["income"].fillna(median_income)

print("Missing income values after cleaning:",customers_df["income"].isnull().sum())

# Check missing occupation values
missing_occupation = customers_df["occupation"].isnull().sum()
print("\nMissing Occupation before cleaning:",missing_occupation)

# Replace missing occupation values
customers_df["occupation"] = customers_df["occupation"].fillna("unknown")

# Verify
print("Missing occupations after cleaning :", customers_df["occupation"].isnull().sum())


missing_city = customers_df["city"].isnull().sum()
print("\nMissing city values before cleaning:",missing_city)

customers_df["city"] = customers_df["city"].fillna("unknown")

print("Missing city values after cleaning:", customers_df["city"].isnull().sum())

# Convert date columns to datetime format
customers_df["join_date"] = pd.to_datetime(customers_df["join_date"])
accounts_df["opening_date"] = pd.to_datetime(accounts_df["opening_date"])
transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"])

print("\nDate columns converted successfully")

print("Customer join date type:", customers_df["join_date"].dtype)
print("Account opening date type:",accounts_df["opening_date"].dtype)
print("Transaction transaction date type:", transactions_df["transaction_date"].dtype)


# Final validation after cleaning
print("\n ==== Final Data Quality Check ====")

print("\nMissing values:")
print("Customers:",customers_df.isnull().sum().sum())
print("Accoutns:", accounts_df.isnull().sum().sum())
print("Transactions:", transactions_df.isnull().sum().sum())
print("Branches:", branches_df.isnull().sum().sum())

print("\nDuplicate Rows:")
print("Customers:",customers_df.duplicated().sum())
print("Accounts:",accounts_df.duplicated().sum())
print("Transactions:", transactions_df.duplicated().sum())
print("Branches:", branches_df.duplicated().sum())

print("\nFinal Dataset Shape:")
print("Customers:",customers_df.shape)
print("Accounts:",accounts_df.shape)
print("Transactions:",transactions_df.shape)
print("Branches:",branches_df.shape)


# Save the Cleaned Datasets
customers_df.to_csv("cleaned_data/customers_cleaned.csv",index=False)
accounts_df.to_csv("cleaned_data/accounts_cleaned.csv",index=False)
transactions_df.to_csv("cleaned_data/transactions_cleaned.csv",index=False)
branches_df.to_csv("cleaned_data/branches_cleaned.csv",index=False)

print("\nCleaned datasets saved successfully")


