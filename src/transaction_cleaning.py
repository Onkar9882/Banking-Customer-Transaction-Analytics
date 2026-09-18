import pandas as pd

# Load cleaned transaction dataset
transactions_df = pd.read_csv("cleaned_data/transactions_cleaned.csv")
print("Cleaned Transaction dataset loaded successfully")

print("\nDataset shape:")
print(transactions_df.shape)

print("\nFirst 5 records:")
print(transactions_df.head())

print("\nData type:")
print(transactions_df.dtypes)

# Check duplicate transactions
duplicate_transactions = transactions_df.duplicated().sum()
print("\nDuplicate Transactions:",duplicate_transactions)

# Check missing values
missing_values = transactions_df.isnull().sum()
print("\nMissing values in each columns :",missing_values)
print("\nTotal Missing Values :",missing_values.sum())

# Check invalid transaction amounts
invalid_amounts = transactions_df[transactions_df["amount"] <= 0]
print("\nInvalid transaction amounts:",len(invalid_amounts))

if len(invalid_amounts) > 0:
    print("\nInvalid transactions records:")
    print(invalid_amounts[["transaction_id","account_id","amount"]])

# Validate transaction categories
valid_categories =["Shopping",
    "Groceries",
    "Bills",
    "Travel",
    "Food",
    "Healthcare",
    "Entertainment",
    "Education",
    "Utilities",
    "Other"]

invalid_categories = transactions_df[~transactions_df["category"].isin(valid_categories)]
print("Invalid categories:",len(invalid_categories))

if len(invalid_categories) > 0:
    print("\nInvalid category records:")
    print(invalid_categories[["transaction_id","category"]])

# Validate transaction types
valid_types = ["Debit","Credit"]
invalid_transaction_types = transactions_df[~transactions_df["transaction_type"].isin(valid_types)]
print("Valid transaction type:",len(invalid_transaction_types))

if len(invalid_transaction_types) > 0:
    print("Invalid transaction types:")
    print(invalid_transaction_types["transaction_id","transaction_type"])

# Validate payment modes

valid_payment_modes = [
    "UPI",
    "Debit Card",
    "Credit Card",
    "Net Banking",
    "ATM"
]

invalid_payment_modes = transactions_df[~transactions_df["payment_mode"].isin(valid_payment_modes)]
print("Invalid payment modes:",len(invalid_payment_modes))

if len(invalid_payment_modes) > 0:
    print("Invalid payment modes:")
    print(invalid_payment_modes["transaction_id","payment_mode"])


# Validate transaction status

valid_transaction_status = [
    "Success",
    "Failed",
    "Pending"
]

invalid_transaction_status = transactions_df[~transactions_df["transaction_status"].isin(valid_transaction_status)]
print("\nInvalid transaction status: ",len(invalid_transaction_status))

if len(invalid_transaction_status) > 0:
    print("Invalid transaction status:")
    print(invalid_transaction_status["transaction_id","transaction_status"])

# Check transaction date range
transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"])

minimum_date = transactions_df["transaction_date"].min()
maximum_date = transactions_df["transaction_date"].max()

print("\nTransaction date range:")
print("Minimum transaction date:",minimum_date)
print("Maximum trasaction date:",maximum_date)


# Create useful transaction date features

transactions_df["transaction_year"] = (
    transactions_df["transaction_date"].dt.year
)

transactions_df["transaction_month"] = (
    transactions_df["transaction_date"].dt.month
)

transactions_df["transaction_month_name"] = (
    transactions_df["transaction_date"].dt.month_name()
)

print("\nTransaction features created successfully!")

print(
    transactions_df[
        [
            "transaction_date",
            "transaction_year",
            "transaction_month",
            "transaction_month_name"
        ]
    ].head()
)

# Final transaction data validation

print("\n========== FINAL TRANSACTION VALIDATION ==========")

print("\nDataset Shape:")
print(transactions_df.shape)

print("\nMissing Values:")
print(transactions_df.isnull().sum())

print("\nTotal Missing Values:")
print(transactions_df.isnull().sum().sum())

print("\nDuplicate Transactions:")
print(transactions_df.duplicated().sum())

print("\nTransaction Amount Check:")
print(
    "Invalid amounts:",
    (transactions_df["amount"] <= 0).sum()
)

print("\nTransaction Types:")
print(transactions_df["transaction_type"].value_counts())

print("\nTransaction Status:")
print(transactions_df["transaction_status"].value_counts())

print("\nPayment Modes:")
print(transactions_df["payment_mode"].value_counts())

print("\nCategories:")
print(transactions_df["category"].value_counts())

print("\nFinal Columns:")
print(transactions_df.columns.tolist())


# Save prepared transaction dataset

transactions_df.to_csv(
    "cleaned_data/transactions_prepared.csv",
    index=False
)

print("\nPrepared transaction dataset saved successfully!")