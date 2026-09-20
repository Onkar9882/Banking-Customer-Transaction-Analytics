import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

transactions_df = pd.read_csv("cleaned_data/transactions_prepared.csv")

transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"])

print("Transaction dataset load successfully")

print("\nShape:")
print(transactions_df.shape)

print("\nColumns:")
print(transactions_df.columns.tolist())

print("\nFirst 5 rows:")
print(transactions_df.head())

total_transactions = transactions_df["transaction_id"].nunique()

print("\nTotal Transactions:", total_transactions)


transaction_type_count = (
    transactions_df["transaction_type"]
    .value_counts()
)

print("\nTransactions by Type:")
print(transaction_type_count)


print("\nTransaction Amount Statistics:")

print("Minimum Amount:",
      transactions_df["amount"].min())

print("Maximum Amount:",
      transactions_df["amount"].max())

print("Average Amount:",
      round(transactions_df["amount"].mean(), 2))

print("Median Amount:",
      transactions_df["amount"].median())

print("Total Transaction Amount:",
      round(transactions_df["amount"].sum(), 2))

plt.figure(figsize=(10, 6))

sns.histplot(
    data=transactions_df,
    x="amount",
    bins=50,
    kde=True
)

plt.title("Transaction Amount Distribution")
plt.xlabel("Transaction Amount")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))

sns.countplot(
    data=transactions_df,
    x="transaction_type"
)

plt.title("Transaction Volume by Transaction Type")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.show()

amount_by_type = (
    transactions_df
    .groupby("transaction_type")["amount"]
    .agg(["count", "sum", "mean", "median"])
    .round(2)
)

print("\nTransaction Amount Analysis by Type:")
print(amount_by_type)


# Transaction Volume by Category
category_transaction_count = (transactions_df["category"].value_counts())
print("\nTransaction volume by category")
print(category_transaction_count)

# Transaction Amount by Category
category_transaction_amount = (transactions_df.groupby("category")["amount"].agg(["count", "sum", "mean", "median"])
.sort_values("sum", ascending=False).round(2))

print("\nTransaction Amount Analysis by Category:")
print(category_transaction_amount)


plt.figure(figsize=(10, 6))

sns.barplot(
    x=category_transaction_count.values,
    y=category_transaction_count.index
)

plt.title("Transaction Volume by Category")
plt.xlabel("Number of Transactions")
plt.ylabel("Category")

plt.tight_layout()
plt.show()


category_total_amount = (
    transactions_df
    .groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=category_total_amount.values,
    y=category_total_amount.index
)

plt.title("Total Transaction Amount by Category")
plt.xlabel("Total Transaction Amount")
plt.ylabel("Category")

plt.tight_layout()
plt.show()

top_category = category_transaction_amount["sum"].idxmax()
top_category_amount = category_transaction_amount["sum"].max()

print("\nHighest Transaction Value Category:")
print("Category:", top_category)
print("Total Amount:", round(top_category_amount, 2))

most_frequent_category = category_transaction_amount["count"].idxmax()
most_frequent_count = category_transaction_amount["count"].max()

print("\nMost Frequent Transaction Category:")
print("Category:", most_frequent_category)
print("Transactions:", most_frequent_count)


# Transaction Volume by Payment Mode
payment_mode_count = (transactions_df["payment_mode"].value_counts())
print("\nTransaction Volume by Payment Mode:")
print(payment_mode_count)

# Transaction Amount by Payment Mode
payment_mode_analysis = (
    transactions_df
    .groupby("payment_mode")["amount"]
    .agg(["count", "sum", "mean", "median"])
    .sort_values("sum", ascending=False)
    .round(2)
)

plt.figure(figsize=(9, 5))

sns.barplot(
    x=payment_mode_count.index,
    y=payment_mode_count.values
)

plt.title("Transaction Volume by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Number of Transactions")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()

payment_mode_total = (
    transactions_df
    .groupby("payment_mode")["amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))

sns.barplot(
    x=payment_mode_total.index,
    y=payment_mode_total.values
)

plt.title("Total Transaction Amount by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Total Transaction Amount")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()

# Find the Most Used Payment Mode
most_used_mode = payment_mode_count.idxmax()
most_used_count = payment_mode_count.max()

print("\nMost Used Payment Mode:")
print("Payment Mode:", most_used_mode)
print("Transactions:", most_used_count)

# Find the Highest-Value Payment Mode
highest_value_mode =  payment_mode_total.idxmax()
highest_value_amount = payment_mode_total.max()

print("\nHighest Transaction Value Payment Mode:")
print("Payment Mode:", highest_value_mode)
print("Total Amount:", round(highest_value_amount, 2)) 


# Transaction Count by Status
status_count = (transactions_df["transaction_status"].value_counts())
print("\nTransaction count by status:")
print(status_count)


status_percentage = (
    transactions_df["transaction_status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nTransaction Status Percentage:")
print(status_percentage)

plt.figure(figsize=(8, 5))

sns.countplot(
    data=transactions_df,
    x="transaction_status",
    order=["Success", "Failed", "Pending"]
)

plt.title("Transaction Count by Status")
plt.xlabel("Transaction Status")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 7))

plt.pie(
    status_percentage.values,
    labels=status_percentage.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Transaction Status Distribution")

plt.tight_layout()
plt.show()

success_rate = (
    (transactions_df["transaction_status"] == "Success").mean() * 100
)

failure_rate = (
    (transactions_df["transaction_status"] == "Failed").mean() * 100
)

pending_rate = (
    (transactions_df["transaction_status"] == "Pending").mean() * 100
)

print("\nTransaction Performance KPIs:")

print("Success Rate:", round(success_rate, 2), "%")
print("Failure Rate:", round(failure_rate, 2), "%")
print("Pending Rate:", round(pending_rate, 2), "%")

total_rate = success_rate + failure_rate + pending_rate

print("\nTotal Status Percentage:", round(total_rate, 2), "%")

# ==========================================
# Business Insight + Recommendation
# ==========================================

status_count = (
    transactions_df["transaction_status"]
    .value_counts()
)

status_percentage = (
    transactions_df["transaction_status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

success_rate = status_percentage.get("Success", 0)
failure_rate = status_percentage.get("Failed", 0)
pending_rate = status_percentage.get("Pending", 0)

print("\n========== BUSINESS INSIGHT ==========")

print(
    f"Out of all transactions, {success_rate}% were successful, "
    f"{failure_rate}% failed, and {pending_rate}% remained pending."
)

if success_rate > failure_rate and success_rate > pending_rate:
    print(
        f"The transaction system shows a high successful transaction rate "
        f"of {success_rate}%, indicating that most transactions were completed successfully."
    )

if failure_rate > 0:
    print(
        f"The failure rate of {failure_rate}% indicates that some transactions "
        f"were unsuccessful and should be monitored for operational issues."
    )

if pending_rate > 0:
    print(
        f"The pending rate of {pending_rate}% indicates that some transactions "
        f"require further processing or status resolution."
    )

print("\n========== BUSINESS RECOMMENDATION ==========")

print(
    "1. Monitor failed transactions regularly to identify recurring transaction issues."
)

print(
    "2. Analyze failed transactions by payment mode, category, and month "
    "to identify patterns."
)

print(
    "3. Monitor pending transactions and improve the process for resolving "
    "pending transactions."
)

print(
    "4. Provide clear customer notifications for failed and pending transactions."
)

print(
    "5. Track transaction success, failure, and pending rates as important "
    "operational KPIs."
)


# MONTHLY TRANSACTION ANALYSIS

transactions_df["transaction_month"] = (
    transactions_df["transaction_date"].dt.to_period("M")
)

# Monthly transaction volume and amount
monthly_transaction_analysis = (
    transactions_df
    .groupby("transaction_month")
    .agg(
        transaction_count=("transaction_id", "count"),
        total_amount=("amount", "sum"),
        average_amount=("amount", "mean"),
        median_amount=("amount", "median")
    )
    .round(2)
)

print("\nMonthly Transaction Analysis:")
print(monthly_transaction_analysis)

monthly_transaction_count = (
    transactions_df
    .groupby("transaction_month")["transaction_id"]
    .count()
)

print("\nMonthly Transaction Volume:")
print(monthly_transaction_count)

plt.figure(figsize=(14, 6))

plt.plot(
    monthly_transaction_count.index.astype(str),
    monthly_transaction_count.values,
    marker="o"
)

plt.title("Monthly Transaction Volume")
plt.xlabel("Month")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

monthly_transaction_amount = (
    transactions_df
    .groupby("transaction_month")["amount"]
    .sum()
)

print("\nMonthly Transaction Amount:")
print(monthly_transaction_amount.round(2))


plt.figure(figsize=(14, 6))

plt.plot(
    monthly_transaction_amount.index.astype(str),
    monthly_transaction_amount.values,
    marker="o"
)

plt.title("Monthly Transaction Amount Trend")
plt.xlabel("Month")
plt.ylabel("Total Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


highest_volume_month = monthly_transaction_count.idxmax()
highest_volume_count = monthly_transaction_count.max()

lowest_volume_month = monthly_transaction_count.idxmin()
lowest_volume_count = monthly_transaction_count.min()

highest_amount_month = monthly_transaction_amount.idxmax()
highest_amount = monthly_transaction_amount.max()

lowest_amount_month = monthly_transaction_amount.idxmin()
lowest_amount = monthly_transaction_amount.min()

print("\n========== MONTHLY TRANSACTION KPIs ==========")

print(
    "Highest Transaction Volume Month:",
    highest_volume_month,
    "| Transactions:",
    highest_volume_count
)

print(
    "Lowest Transaction Volume Month:",
    lowest_volume_month,
    "| Transactions:",
    lowest_volume_count
)

print(
    "Highest Transaction Amount Month:",
    highest_amount_month,
    "| Amount:",
    round(highest_amount, 2)
)

print(
    "Lowest Transaction Amount Month:",
    lowest_amount_month,
    "| Amount:",
    round(lowest_amount, 2)
)


# ==========================================
# STEP 18.8 — BUSINESS INSIGHT + RECOMMENDATION
# ==========================================

print("\n========== STEP 18.8 — BUSINESS INSIGHTS ==========")

print(
    f"The highest transaction volume was recorded in "
    f"{highest_volume_month}, with {highest_volume_count} transactions."
)

print(
    f"The lowest transaction volume was recorded in "
    f"{lowest_volume_month}, with {lowest_volume_count} transactions."
)

print(
    f"The highest total transaction amount was recorded in "
    f"{highest_amount_month}, with a total value of "
    f"{highest_amount:,.2f}."
)

print(
    f"The lowest total transaction amount was recorded in "
    f"{lowest_amount_month}, with a total value of "
    f"{lowest_amount:,.2f}."
)

# Compare highest transaction volume month
# with highest transaction amount month

if highest_volume_month == highest_amount_month:

    print(
        "\nInsight: The month with the highest transaction volume "
        "also recorded the highest transaction amount."
    )

else:

    print(
        "\nInsight: The month with the highest transaction volume "
        "was different from the month with the highest transaction amount."
    )

print("\n========== BUSINESS RECOMMENDATIONS ==========")

print(
    "1. Monitor monthly transaction trends to identify changes "
    "in customer activity."
)

print(
    "2. Investigate high-volume months to understand the factors "
    "driving increased transaction activity."
)

print(
    "3. Analyze high-value months separately because transaction "
    "value may not always follow transaction volume."
)

print(
    "4. Compare monthly trends by transaction category and payment "
    "mode to identify specific sources of growth."
)

print(
    "5. Use monthly transaction trends for operational planning, "
    "customer engagement, and transaction monitoring."
)


# YEAR AND MONTH ANALYSIS
transactions_df["transaction_year"] = transactions_df["transaction_date"].dt.year
transactions_df["transaction_month_number"] = transactions_df["transaction_date"].dt.month
transactions_df["transaction_month_name"] = transactions_df["transaction_date"].dt.month_name()

print("\nYear and Month column created")
print(transactions_df[["transaction_date", "transaction_year", "transaction_month_number", "transaction_month_name"]].head())


# Calculate transaction count and transaction amount for each year
yearly_transaction_analysis = (
    transactions_df
    .groupby("transaction_year")
    .agg(
        transaction_count=("transaction_id", "count"),
        total_amount=("amount", "sum"),
        average_amount=("amount", "mean"),
        median_amount=("amount", "median")
    )
    .round(2)
)

print("\n========== YEARLY TRANSACTION ANALYSIS ==========")
print(yearly_transaction_analysis)

yearly_transaction_count = (
    transactions_df
    .groupby("transaction_year")["transaction_id"]
    .count()
)

print("\nYearly Transaction Volume:")
print(yearly_transaction_count)

plt.figure(figsize=(9,5))
plt.plot(yearly_transaction_count.index, yearly_transaction_count.values, marker="o")
plt.title("Yearly transaction volumn")
plt.xlabel("year")
plt.ylabel("Number of transaction")
plt.xticks(yearly_transaction_count.index)
plt.tight_layout()
plt.show()

yearly_transaction_amount = (
    transactions_df
    .groupby("transaction_year")["amount"]
    .sum()
)

print("\nYearly Transaction Amount:")
print(yearly_transaction_amount.round(2))


plt.figure(figsize=(10, 5))

plt.plot(
    yearly_transaction_amount.index,
    yearly_transaction_amount.values,
    marker="o"
)

plt.title("Yearly Transaction Amount Trend")
plt.xlabel("Year")
plt.ylabel("Total Transaction Amount")
plt.xticks(yearly_transaction_amount.index)
plt.tight_layout()
plt.show()


yearly_transaction_analysis["volume_growth_%"] = (
    yearly_transaction_analysis["transaction_count"]
    .pct_change()
    .mul(100)
    .round(2)
)

yearly_transaction_analysis["amount_growth_%"] = (
    yearly_transaction_analysis["total_amount"]
    .pct_change()
    .mul(100)
    .round(2)
)

print("\n========== YEAR-OVER-YEAR GROWTH ==========")
print(
    yearly_transaction_analysis[
        [
            "transaction_count",
            "total_amount",
            "volume_growth_%",
            "amount_growth_%"
        ]
    ]
)


monthly_year_analysis = (
    transactions_df
    .groupby(
        [
            "transaction_year",
            "transaction_month_number",
            "transaction_month_name"
        ]
    )
    .agg(
        transaction_count=("transaction_id", "count"),
        total_amount=("amount", "sum")
    )
    .reset_index()
)

print("\n========== MONTHLY TRANSACTION PATTERN ==========")
print(monthly_year_analysis.head(15))


month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

monthly_pattern = (
    transactions_df
    .groupby("transaction_month_number")
    .agg(
        transaction_count=("transaction_id", "count"),
        total_amount=("amount", "sum")
    )
    .sort_index()
)

print("\n========== MONTHLY PATTERN ==========")
print(monthly_pattern)

# Find Highest and Lowest Year
highest_year_volume = yearly_transaction_count.idxmax()
highest_year_volume_count = yearly_transaction_count.max()

lowest_year_volume = yearly_transaction_count.idxmin()
lowest_year_volume_count = yearly_transaction_count.min()

highest_year_amount = yearly_transaction_amount.idxmax()
highest_year_amount_value = yearly_transaction_amount.max()

lowest_year_amount = yearly_transaction_amount.idxmin()
lowest_year_amount_value = yearly_transaction_amount.min()

print("\n========== YEARLY KPIs ==========")

print(
    "Highest Transaction Volume Year:",
    highest_year_volume,
    "| Transactions:",
    highest_year_volume_count
)

print(
    "Lowest Transaction Volume Year:",
    lowest_year_volume,
    "| Transactions:",
    lowest_year_volume_count
)

print(
    "Highest Transaction Amount Year:",
    highest_year_amount,
    "| Amount:",
    round(highest_year_amount_value, 2)
)

print(
    "Lowest Transaction Amount Year:",
    lowest_year_amount,
    "| Amount:",
    round(lowest_year_amount_value, 2)
)

# ==========================================
# BUSINESS INSIGHT + RECOMMENDATION
# ==========================================

print("\n========== BUSINESS INSIGHTS ==========")

# Highest and lowest transaction volume years
print(
    f"Highest transaction volume was recorded in "
    f"{highest_year_volume}, with "
    f"{highest_year_volume_count:,} transactions."
)

print(
    f"Lowest transaction volume was recorded in "
    f"{lowest_year_volume}, with "
    f"{lowest_year_volume_count:,} transactions."
)

# Highest and lowest transaction amount years
print(
    f"Highest total transaction amount was recorded in "
    f"{highest_year_amount}, with a total value of "
    f"{highest_year_amount_value:,.2f}."
)

print(
    f"Lowest total transaction amount was recorded in "
    f"{lowest_year_amount}, with a total value of "
    f"{lowest_year_amount_value:,.2f}."
)


# ==========================================
# YEAR-OVER-YEAR GROWTH INSIGHTS
# ==========================================

growth_data = yearly_transaction_analysis.dropna(
    subset=["volume_growth_%", "amount_growth_%"]
)

if not growth_data.empty:

    # Highest volume growth year
    highest_volume_growth_year = (
        growth_data["volume_growth_%"].idxmax()
    )

    highest_volume_growth = (
        growth_data.loc[
            highest_volume_growth_year,
            "volume_growth_%"
        ]
    )

    # Lowest volume growth year
    lowest_volume_growth_year = (
        growth_data["volume_growth_%"].idxmin()
    )

    lowest_volume_growth = (
        growth_data.loc[
            lowest_volume_growth_year,
            "volume_growth_%"
        ]
    )

    # Highest amount growth year
    highest_amount_growth_year = (
        growth_data["amount_growth_%"].idxmax()
    )

    highest_amount_growth = (
        growth_data.loc[
            highest_amount_growth_year,
            "amount_growth_%"
        ]
    )

    # Lowest amount growth year
    lowest_amount_growth_year = (
        growth_data["amount_growth_%"].idxmin()
    )

    lowest_amount_growth = (
        growth_data.loc[
            lowest_amount_growth_year,
            "amount_growth_%"
        ]
    )

    print("\n========== YEAR-OVER-YEAR GROWTH ==========")

    print(
        f"Highest transaction volume growth occurred in "
        f"{highest_volume_growth_year}: "
        f"{highest_volume_growth}%."
    )

    print(
        f"Lowest transaction volume growth occurred in "
        f"{lowest_volume_growth_year}: "
        f"{lowest_volume_growth}%."
    )

    print(
        f"Highest transaction amount growth occurred in "
        f"{highest_amount_growth_year}: "
        f"{highest_amount_growth}%."
    )

    print(
        f"Lowest transaction amount growth occurred in "
        f"{lowest_amount_growth_year}: "
        f"{lowest_amount_growth}%."
    )


# ==========================================
# BUSINESS RECOMMENDATIONS
# ==========================================

print("\n========== BUSINESS RECOMMENDATIONS ==========")

print(
    "1. Monitor year-over-year transaction volume and amount "
    "to identify changes in customer activity."
)

print(
    "2. Investigate years with strong transaction growth "
    "to understand which categories and payment modes "
    "contributed to the increase."
)

print(
    "3. Analyze years with lower or negative growth to identify "
    "areas requiring operational or customer engagement attention."
)

print(
    "4. Compare transaction volume growth with transaction "
    "amount growth because transaction frequency and transaction "
    "value may show different patterns."
)

print(
    "5. Use monthly patterns along with yearly trends for "
    "better transaction planning and customer engagement."
)



# CUSTOMER VS TRANSACTION ANALYSIS
customers_df = pd.read_csv("cleaned_data/customers_cleaned.csv")
accounts_df = pd.read_csv("cleaned_data/accounts_cleaned.csv")
transactions_df = pd.read_csv("cleaned_data/transactions_prepared.csv")

# Convert dates
customers_df["join_date"] = pd.to_datetime(customers_df["join_date"])
transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"])

print("\ncustomer shape:",customers_df.shape)
print("Account shape:", accounts_df.shape)
print("Transaction shape:", transactions_df.shape)

# Connect Customers with Accounts
customer_accounts_df = customers_df.merge(
    accounts_df,
    on="customer_id",
    how="left"
)

print("\nCustomer + Account Data:")
print(customer_accounts_df.head())

print("\nShape:", customer_accounts_df.shape)

# Connect Accounts with Transactions
customer_transaction_df = customer_accounts_df.merge(
    transactions_df,
    on="account_id",
    how="left"
)

print("\nCustomer + Account + Transaction Data:")
print(customer_transaction_df.head())

print("\nShape:", customer_transaction_df.shape)

customer_transaction_summary = (
    customer_transaction_df
    .groupby(
        [
            "customer_id",
            "name",
            "age",
            "gender",
            "occupation",
            "income"
        ]
    )
    .agg(
        transaction_count=("transaction_id", "count"),
        total_transaction_amount=("amount", "sum"),
        average_transaction_amount=("amount", "mean"),
        median_transaction_amount=("amount", "median")
    )
    .reset_index()
)

customer_transaction_summary[
    [
        "total_transaction_amount",
        "average_transaction_amount",
        "median_transaction_amount"
    ]
] = (
    customer_transaction_summary[
        [
            "total_transaction_amount",
            "average_transaction_amount",
            "median_transaction_amount"
        ]
    ].round(2)
)

print("\n========== CUSTOMER TRANSACTION SUMMARY ==========")
print(customer_transaction_summary.head(10))


# Most Active Customers
most_active_customers = (
    customer_transaction_summary
    .sort_values(
        "transaction_count",
        ascending=False
    )
    .head(10)
)

print("\n========== TOP 10 MOST ACTIVE CUSTOMERS ==========")

print(
    most_active_customers[
        [
            "customer_id",
            "name",
            "transaction_count",
            "total_transaction_amount"
        ]
    ]
)

# Highest-Spending Customers
highest_spending_customers = (
    customer_transaction_summary
    .sort_values(
        "total_transaction_amount",
        ascending=False
    )
    .head(10)
)

print("\n========== TOP 10 HIGHEST-SPENDING CUSTOMERS ==========")

print(
    highest_spending_customers[
        [
            "customer_id",
            "name",
            "transaction_count",
            "total_transaction_amount",
            "average_transaction_amount"
        ]
    ]
)

# Customer Transaction KPIs
total_customers = customers_df["customer_id"].nunique()

customers_with_transactions = (
    customer_transaction_summary[
        customer_transaction_summary["transaction_count"] > 0
    ]["customer_id"]
    .nunique()
)

customers_without_transactions = (
    total_customers - customers_with_transactions
)

average_transactions_per_customer = (
    customer_transaction_summary["transaction_count"].mean()
)

average_spending_per_customer = (
    customer_transaction_summary["total_transaction_amount"].mean()
)

print("\n========== CUSTOMER TRANSACTION KPIs ==========")

print(
    "Total Customers:",
    total_customers
)

print(
    "Customers With Transactions:",
    customers_with_transactions
)

print(
    "Customers Without Transactions:",
    customers_without_transactions
)

print(
    "Average Transactions per Customer:",
    round(
        average_transactions_per_customer,
        2
    )
)

print(
    "Average Transaction Amount per Customer:",
    round(
        average_spending_per_customer,
        2
    )
)



plt.figure(figsize=(10, 6))

sns.histplot(
    customer_transaction_summary[
        "total_transaction_amount"
    ],
    bins=30,
    kde=True
)

plt.title("Customer Total Transaction Amount Distribution")
plt.xlabel("Total Transaction Amount")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=customer_transaction_summary,
    x="income",
    y="total_transaction_amount"
)

plt.title("Customer Income vs Total Transaction Amount")
plt.xlabel("Customer Income")
plt.ylabel("Total Transaction Amount")

plt.tight_layout()
plt.show()



customer_transaction_summary.to_csv(
    "cleaned_data/customer_transaction_summary.csv",
    index=False
)

print(
    "\nCustomer transaction summary saved successfully."
)




# Customer Segmentation Based on Transaction Behavior

print("\n========== CUSTOMER SEGMENTATION ==========")

print(
    customer_transaction_summary[
        [
            "customer_id",
            "name",
            "transaction_count",
            "total_transaction_amount",
            "average_transaction_amount"
        ]
    ].head(10)
)


customer_transaction_summary["activity_segment"] = pd.cut(
    customer_transaction_summary["transaction_count"],
    bins=3,
    labels=[
        "Low Activity",
        "Medium Activity",
        "High Activity"
    ],
    include_lowest=True
)

print("\nTransaction Activity Segments:")
print(
    customer_transaction_summary["activity_segment"]
    .value_counts()
    .sort_index()
)

activity_analysis = (
    customer_transaction_summary
    .groupby(
        "activity_segment",
        observed=True
    )
    .agg(
        customer_count=("customer_id", "count"),
        total_transactions=("transaction_count", "sum"),
        total_transaction_amount=(
            "total_transaction_amount",
            "sum"
        ),
        average_customer_spending=(
            "total_transaction_amount",
            "mean"
        )
    )
    .round(2)
)

print("\n========== ACTIVITY SEGMENT ANALYSIS ==========")
print(activity_analysis)


plt.figure(figsize=(9, 5))

sns.countplot(
    data=customer_transaction_summary,
    x="activity_segment",
    order=[
        "Low Activity",
        "Medium Activity",
        "High Activity"
    ]
)

plt.title("Customer Distribution by Transaction Activity")
plt.xlabel("Activity Segment")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Create Spending Segments
customer_transaction_summary["spending_segment"] = pd.qcut(
    customer_transaction_summary[
        "total_transaction_amount"
    ],
    q=3,
    labels=[
        "Low Spender",
        "Medium Spender",
        "High Spender"
    ],
    duplicates="drop"
)

print("\nSpending Segments:")
print(
    customer_transaction_summary["spending_segment"]
    .value_counts()
    .sort_index()
)

spending_analysis = (
    customer_transaction_summary
    .groupby(
        "spending_segment",
        observed=True
    )
    .agg(
        customer_count=("customer_id", "count"),
        total_transactions=("transaction_count", "sum"),
        total_transaction_amount=(
            "total_transaction_amount",
            "sum"
        ),
        average_spending=(
            "total_transaction_amount",
            "mean"
        )
    )
    .round(2)
)

print("\n========== SPENDING SEGMENT ANALYSIS ==========")
print(spending_analysis)

plt.figure(figsize=(9, 5))

sns.countplot(
    data=customer_transaction_summary,
    x="spending_segment",
    order=[
        "Low Spender",
        "Medium Spender",
        "High Spender"
    ]
)

plt.title("Customer Distribution by Spending Segment")
plt.xlabel("Spending Segment")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Compare Activity vs Spending
activity_spending_matrix = pd.crosstab(
    customer_transaction_summary["activity_segment"],
    customer_transaction_summary["spending_segment"]
)

print("\n========== ACTIVITY VS SPENDING ==========")
print(activity_spending_matrix)

plt.figure(figsize=(9, 6))

sns.heatmap(
    activity_spending_matrix,
    annot=True,
    fmt="d"
)

plt.title(
    "Customer Segmentation: Transaction Activity vs Spending"
)

plt.xlabel("Spending Segment")
plt.ylabel("Activity Segment")

plt.tight_layout()
plt.show()

customer_transaction_summary.to_csv(
    "cleaned_data/customer_transaction_segments.csv",
    index=False
)

print(
    "\nCustomer transaction segmentation saved successfully."
)


# ==========================================
# CUSTOMER SEGMENT
# BUSINESS INSIGHT + RECOMMENDATION
# ==========================================

print("\n========== CUSTOMER SEGMENT BUSINESS INSIGHTS ==========")

# ------------------------------------------
# 1. Activity Segment Insights
# ------------------------------------------

activity_customer_count = (
    customer_transaction_summary["activity_segment"]
    .value_counts()
    .sort_index()
)

largest_activity_segment = (
    activity_customer_count.idxmax()
)

largest_activity_count = (
    activity_customer_count.max()
)

print(
    f"\nThe largest customer activity segment is "
    f"'{largest_activity_segment}' with "
    f"{largest_activity_count:,} customers."
)


# ------------------------------------------
# 2. Spending Segment Insights
# ------------------------------------------

spending_customer_count = (
    customer_transaction_summary["spending_segment"]
    .value_counts()
    .sort_index()
)

largest_spending_segment = (
    spending_customer_count.idxmax()
)

largest_spending_count = (
    spending_customer_count.max()
)

print(
    f"The largest customer spending segment is "
    f"'{largest_spending_segment}' with "
    f"{largest_spending_count:,} customers."
)


# ------------------------------------------
# 3. Highest Value Activity Segment
# ------------------------------------------

activity_value = (
    customer_transaction_summary
    .groupby(
        "activity_segment",
        observed=True
    )["total_transaction_amount"]
    .sum()
    .sort_values(ascending=False)
)

highest_value_activity_segment = (
    activity_value.idxmax()
)

highest_value_activity_amount = (
    activity_value.max()
)

print(
    f"\nThe '{highest_value_activity_segment}' segment "
    f"generated the highest total transaction value of "
    f"{highest_value_activity_amount:,.2f}."
)


# ------------------------------------------
# 4. Activity vs Spending Analysis
# ------------------------------------------

activity_spending_matrix = pd.crosstab(
    customer_transaction_summary["activity_segment"],
    customer_transaction_summary["spending_segment"]
)

largest_combination = (
    activity_spending_matrix.stack().idxmax()
)

largest_combination_count = (
    activity_spending_matrix.stack().max()
)

print(
    f"\nThe largest activity-spending customer group is "
    f"'{largest_combination[0]}' + "
    f"'{largest_combination[1]}', containing "
    f"{largest_combination_count:,} customers."
)


# ==========================================
# BUSINESS RECOMMENDATIONS
# ==========================================

print("\n========== BUSINESS RECOMMENDATIONS ==========")

print(
    "1. Focus customer engagement analysis on the largest "
    "activity segment to understand the behavior of the "
    "majority of customers."
)

print(
    "2. Monitor high-spending customers because they contribute "
    "a larger share of transaction value."
)

print(
    "3. Analyze low-activity customers to identify opportunities "
    "for improving customer engagement."
)

print(
    "4. Compare activity and spending segments regularly because "
    "transaction frequency and transaction value can represent "
    "different customer behaviors."
)

print(
    "5. Use customer segments in Power BI dashboards to monitor "
    "customer activity, spending patterns, and transaction value."
)


# Branch Performance Analysis
# Load the Required Data

# BRANCH PERFORMANCE ANALYSIS

branches_df = pd.read_csv("cleaned_data/branches_cleaned.csv")
accounts_df = pd.read_csv("cleaned_data/accounts_cleaned.csv")
customers_df = pd.read_csv("cleaned_data/customers_cleaned.csv")
transactions_df = pd.read_csv("cleaned_data/transactions_prepared.csv")
transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"])
print("\n===== Data Shapes =====")
print("Branches:",branches_df.shape)
print("Accounts:",accounts_df.shape)
print("Customers:",customers_df.shape)
print("Transactions:",transactions_df.shape)


# Connect Branches with Accounts
branch_accounts_df = branches_df.merge(accounts_df, on="branch_id", how="left")
print("\nBranch + Account data")
print(branch_accounts_df.head())
print("\nShape:",branch_accounts_df.shape)

# Connect Account with Transactions
branch_transactions_df = branch_accounts_df.merge(transactions_df, on="account_id", how="left")
print("\n===== Branch transaction Data =====")
print(branch_transactions_df.head())
print("\nShape:",branch_transactions_df.head())

# Branch Customer Count
branch_customer_count = (branch_accounts_df
.groupby(["branch_id", "branch_name", "city", "state", "branch_type"])
["customer_id"].nunique().reset_index(name="customer_count"))

print("\n ===== Customer By Branch =====")
print(branch_customer_count.sort_values("customer_count",ascending=False).head(10))

# calculate the number of transactions handled by each branch.
branch_transaction_count = (branch_transactions_df.groupby("branch_id")["transaction_id"].nunique().reset_index(name="transaction_count"))
print("\n ===== Transactions By Branch =====")
print(branch_transaction_count.sort_values("transaction_count",ascending=False).head(10))

# calculate the total transaction value handled by each branch.
branch_transaction_amount = (branch_transactions_df.groupby("branch_id")["amount"]
.agg(total_transaction_amount = "sum", average_transaction_amount = "mean", median_transaction_amount = "median").round(2).reset_index())
print("\n ===== Transaction Value By Branch =====")
print(
    branch_transaction_amount
    .sort_values(
        "total_transaction_amount",
        ascending=False
    )
    .head(10)
)

# Create Complete Branch Performance Dataset
branch_performance = (
    branch_customer_count
    .merge(
        branch_transaction_count,
        on="branch_id",
        how="left"
    )
    .merge(
        branch_transaction_amount,
        on="branch_id",
        how="left"
    )
)

print("\n========== BRANCH PERFORMANCE ==========")
print(branch_performance.head(10))

# Handle Branches With No Transactions
branch_performance[
    [
        "transaction_count",
        "total_transaction_amount",
        "average_transaction_amount",
        "median_transaction_amount"
    ]
] = (
    branch_performance[
        [
            "transaction_count",
            "total_transaction_amount",
            "average_transaction_amount",
            "median_transaction_amount"
        ]
    ]
    .fillna(0)
)

print("\nMissing values after branch analysis:")

print(
    branch_performance.isnull().sum()
)

# Top 10 Branches by Transaction Volume
top_branches_by_volume = (
    branch_performance
    .sort_values(
        "transaction_count",
        ascending=False
    )
    .head(10)
)

print("\n========== TOP 10 BRANCHES BY TRANSACTION VOLUME ==========")

print(
    top_branches_by_volume[
        [
            "branch_id",
            "branch_name",
            "branch_type",
            "customer_count",
            "transaction_count",
            "total_transaction_amount"
        ]
    ]
)

# Top 10 Branches by Transaction Value
top_branches_by_value = (
    branch_performance
    .sort_values(
        "total_transaction_amount",
        ascending=False
    )
    .head(10)
)

print("\n========== TOP 10 BRANCHES BY TRANSACTION VALUE ==========")

print(
    top_branches_by_value[
        [
            "branch_id",
            "branch_name",
            "branch_type",
            "customer_count",
            "transaction_count",
            "total_transaction_amount",
            "average_transaction_amount"
        ]
    ]
)


plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_branches_by_volume,
    x="transaction_count",
    y="branch_name"
)

plt.title("Top 10 Branches by Transaction Volume")
plt.xlabel("Number of Transactions")
plt.ylabel("Branch")

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_branches_by_value,
    x="total_transaction_amount",
    y="branch_name"
)

plt.title("Top 10 Branches by Transaction Value")
plt.xlabel("Total Transaction Amount")
plt.ylabel("Branch")

plt.tight_layout()
plt.show()

# Branch Type Analysis
branch_type_analysis = (
    branch_performance
    .groupby("branch_type")
    .agg(
        branch_count=("branch_id", "nunique"),
        customer_count=("customer_count", "sum"),
        transaction_count=("transaction_count", "sum"),
        total_transaction_amount=(
            "total_transaction_amount",
            "sum"
        ),
        average_transaction_amount=(
            "average_transaction_amount",
            "mean"
        )
    )
    .round(2)
)

print("\n========== BRANCH TYPE ANALYSIS ==========")
print(branch_type_analysis)

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=branch_performance,
    x="customer_count",
    y="transaction_count",
    hue="branch_type",
    s=100
)

plt.title("Branch Customer Count vs Transaction Volume")
plt.xlabel("Number of Customers")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.show()

# Branch Performance KPIs
highest_volume_branch = (
    branch_performance
    .loc[
        branch_performance["transaction_count"].idxmax()
    ]
)

highest_value_branch = (
    branch_performance
    .loc[
        branch_performance[
            "total_transaction_amount"
        ].idxmax()
    ]
)

highest_customer_branch = (
    branch_performance
    .loc[
        branch_performance[
            "customer_count"
        ].idxmax()
    ]
)

print("\n========== BRANCH PERFORMANCE KPIs ==========")

print(
    "Branch with Highest Customer Count:",
    highest_customer_branch["branch_name"],
    "| Customers:",
    int(highest_customer_branch["customer_count"])
)

print(
    "Branch with Highest Transaction Volume:",
    highest_volume_branch["branch_name"],
    "| Transactions:",
    int(highest_volume_branch["transaction_count"])
)

print(
    "Branch with Highest Transaction Value:",
    highest_value_branch["branch_name"],
    "| Amount:",
    round(
        highest_value_branch[
            "total_transaction_amount"
        ],
        2
    )
)


branch_performance.to_csv(
    "cleaned_data/branch_performance.csv",
    index=False
)

print(
    "\nBranch performance data saved successfully."
)

# ==========================================
# BRANCH PERFORMANCE
# BUSINESS INSIGHT + RECOMMENDATION
# ==========================================

print("\n========== BUSINESS INSIGHTS ==========")

# ------------------------------------------
# 1. Highest Customer Count Branch
# ------------------------------------------

highest_customer_branch = (
    branch_performance.loc[
        branch_performance["customer_count"].idxmax()
    ]
)

print(
    f"\nThe branch with the highest customer count is "
    f"{highest_customer_branch['branch_name']} "
    f"with {int(highest_customer_branch['customer_count']):,} customers."
)


# ------------------------------------------
# 2. Highest Transaction Volume Branch
# ------------------------------------------

highest_volume_branch = (
    branch_performance.loc[
        branch_performance["transaction_count"].idxmax()
    ]
)

print(
    f"The branch with the highest transaction volume is "
    f"{highest_volume_branch['branch_name']} "
    f"with {int(highest_volume_branch['transaction_count']):,} transactions."
)


# ------------------------------------------
# 3. Highest Transaction Value Branch
# ------------------------------------------

highest_value_branch = (
    branch_performance.loc[
        branch_performance[
            "total_transaction_amount"
        ].idxmax()
    ]
)

print(
    f"The branch with the highest transaction value is "
    f"{highest_value_branch['branch_name']} "
    f"with a total transaction value of "
    f"{highest_value_branch['total_transaction_amount']:,.2f}."
)


# ------------------------------------------
# 4. Highest Average Transaction Value
# ------------------------------------------

highest_average_branch = (
    branch_performance.loc[
        branch_performance[
            "average_transaction_amount"
        ].idxmax()
    ]
)

print(
    f"The branch with the highest average transaction amount is "
    f"{highest_average_branch['branch_name']} "
    f"with an average transaction value of "
    f"{highest_average_branch['average_transaction_amount']:,.2f}."
)


# ------------------------------------------
# 5. Branch Type Analysis
# ------------------------------------------

branch_type_analysis = (
    branch_performance
    .groupby("branch_type")
    .agg(
        branch_count=("branch_id", "nunique"),
        customer_count=("customer_count", "sum"),
        transaction_count=("transaction_count", "sum"),
        total_transaction_amount=(
            "total_transaction_amount",
            "sum"
        )
    )
    .round(2)
)

print("\n========== BRANCH TYPE INSIGHTS ==========")

print(branch_type_analysis)

highest_branch_type_by_value = (
    branch_type_analysis[
        "total_transaction_amount"
    ].idxmax()
)

highest_branch_type_value = (
    branch_type_analysis[
        "total_transaction_amount"
    ].max()
)

print(
    f"\nThe '{highest_branch_type_by_value}' branch type "
    f"generated the highest total transaction value of "
    f"{highest_branch_type_value:,.2f}."
)


# ==========================================
# BUSINESS RECOMMENDATIONS
# ==========================================

print("\n========== BUSINESS RECOMMENDATIONS ==========")

print(
    "1. Monitor branches with high transaction volume "
    "to ensure efficient transaction processing and service quality."
)

print(
    "2. Analyze high-value branches separately because "
    "transaction value can differ from transaction volume."
)

print(
    "3. Compare customer count with transaction activity "
    "to identify branches with high customer concentration "
    "but relatively lower transaction activity."
)

print(
    "4. Analyze branch performance by branch type to understand "
    "differences between Urban, Semi-Urban, and Rural branches."
)

print(
    "5. Investigate the categories and payment modes contributing "
    "to high transaction activity at individual branches."
)

print(
    "6. Use branch-level KPIs in the Power BI dashboard to "
    "monitor customer count, transaction volume, and transaction value."
)


# Account Type Analysis
customers_df = pd.read_csv("cleaned_data/customers_cleaned.csv")
accounts_df = pd.read_csv("cleaned_data/accounts_cleaned.csv")
transactions_df = pd.read_csv("cleaned_data/transactions_prepared.csv")

transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"])

# Merge Accounts with Transactions
account_transactions_df = accounts_df.merge(transactions_df, on="account_id", how="left")
print("\nAccount Transaction Data:")
print(account_transactions_df.head())

print("\nAccount Transaction Shape:")
print(account_transactions_df.shape)

# Customer Count by Account Type
account_type_customer_count = (accounts_df.groupby("account_type")["customer_id"].nunique().reset_index(name="customer_count")
.sort_values("customer_count",ascending=False))
print("\nCustomer count by account type")
print(account_type_customer_count)

# Transaction Volume by Account Type
account_type_transaction_count = (account_transactions_df.groupby("account_type")["transaction_id"].nunique()
.reset_index(name="transaction_count").sort_values("transaction_count", ascending=False))
print("\nTransaction count by account type")
print(account_type_transaction_count)

# Transaction Amount Analysis
account_type_transaction_amount = (account_transactions_df.groupby("account_type")["amount"]
.agg(total_transaction_amount="sum", average_transaction_amount="mean", median_transaction_amount="median").round(2)
.reset_index().sort_values("total_transaction_amount",ascending=False))
print("\nTransaction Amount By Account Type")
print(account_type_transaction_amount)

# Create One Final Account Type Performance Table
account_type_performance =(
account_type_customer_count.merge(account_type_transaction_count, on="account_type", how="left")
.merge(account_type_transaction_amount, on="account_type", how="left"))

account_type_performance = account_type_performance.fillna(0)
print("\n========================================")
print("ACCOUNT TYPE PERFORMANCE")
print("========================================")

print(account_type_performance)

# Account Status Analysis
account_status_analysis = (
    accounts_df
    .groupby(["account_type", "account_status"])
    .size()
    .reset_index(name="account_count")
)

print("\nAccount Status by Account Type:")
print(account_status_analysis)

plt.figure(figsize=(8, 5))

sns.barplot(
    data=account_type_customer_count,
    x="account_type",
    y="customer_count"
)

plt.title("Customer Count by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

sns.barplot(
    data=account_type_transaction_count,
    x="account_type",
    y="transaction_count"
)

plt.title("Transaction Volume by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

sns.barplot(
    data=account_type_transaction_amount,
    x="account_type",
    y="total_transaction_amount"
)

plt.title("Total Transaction Amount by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Total Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))

sns.barplot(
    data=account_type_transaction_amount,
    x="account_type",
    y="average_transaction_amount"
)

plt.title("Average Transaction Amount by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Average Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Account Type KPI Analysis
highest_customer_account_type = account_type_performance.loc[
    account_type_performance["customer_count"].idxmax(),
    "account_type"
]

highest_transaction_account_type = account_type_performance.loc[
    account_type_performance["transaction_count"].idxmax(),
    "account_type"
]

highest_value_account_type = account_type_performance.loc[
    account_type_performance["total_transaction_amount"].idxmax(),
    "account_type"
]

highest_average_account_type = account_type_performance.loc[
    account_type_performance["average_transaction_amount"].idxmax(),
    "account_type"
]

print("\n========================================")
print("ACCOUNT TYPE KPIs")
print("========================================")

print(
    f"Account type with highest customers: "
    f"{highest_customer_account_type}"
)

print(
    f"Account type with highest transaction volume: "
    f"{highest_transaction_account_type}"
)

print(
    f"Account type with highest transaction value: "
    f"{highest_value_account_type}"
)

print(
    f"Account type with highest average transaction amount: "
    f"{highest_average_account_type}"
)


account_type_performance.to_csv(
    "cleaned_data/account_type_performance.csv",
    index=False
)

print(
    "\nAccount type performance saved successfully."
)

# ==========================================
# BUSINESS INSIGHTS
# ==========================================

print("\n========================================")
print("ACCOUNT TYPE BUSINESS INSIGHTS")
print("========================================")

# 1. Highest customer count
highest_customer_row = account_type_performance.loc[
    account_type_performance["customer_count"].idxmax()
]

# 2. Highest transaction volume
highest_transaction_row = account_type_performance.loc[
    account_type_performance["transaction_count"].idxmax()
]

# 3. Highest transaction value
highest_value_row = account_type_performance.loc[
    account_type_performance["total_transaction_amount"].idxmax()
]

# 4. Highest average transaction amount
highest_average_row = account_type_performance.loc[
    account_type_performance["average_transaction_amount"].idxmax()
]

print(
    f"\n1. Highest customer count: "
    f"{highest_customer_row['account_type']} "
    f"({highest_customer_row['customer_count']:.0f} customers)"
)

print(
    f"2. Highest transaction volume: "
    f"{highest_transaction_row['account_type']} "
    f"({highest_transaction_row['transaction_count']:.0f} transactions)"
)

print(
    f"3. Highest transaction value: "
    f"{highest_value_row['account_type']} "
    f"({highest_value_row['total_transaction_amount']:.2f})"
)

print(
    f"4. Highest average transaction amount: "
    f"{highest_average_row['account_type']} "
    f"({highest_average_row['average_transaction_amount']:.2f})"
)


print("\n========================================")
print("FINAL BUSINESS SUMMARY")
print("========================================")

print(
    f"""
1. {highest_customer_row['account_type']} has the highest
   customer count.

2. {highest_transaction_row['account_type']} has the highest
   transaction volume.

3. {highest_value_row['account_type']} has the highest
   total transaction value.

4. {highest_average_row['account_type']} has the highest
   average transaction amount.

5. Account types should be compared using both transaction
   frequency and transaction value rather than using a
   single metric.

6. Account status analysis can help identify account types
   with active and inactive accounts.

7. Account type performance can be incorporated into the
   Power BI dashboard for interactive comparison.
"""
)

# ==========================================
# PAYMENT MODE ANALYSIS
# ==========================================

transactions_df = pd.read_csv(
    "cleaned_data/transactions_prepared.csv"
)

transactions_df["transaction_date"] = pd.to_datetime(
    transactions_df["transaction_date"]
)

print("\nTransaction Data:")
print(transactions_df.head())


payment_modes = transactions_df["payment_mode"].value_counts()

print("\nPayment Modes:")
print(payment_modes)


# Transaction Volume by Payment Mode
payment_mode_transaction_count = (
    transactions_df
    .groupby("payment_mode")["transaction_id"]
    .nunique()
    .reset_index(name="transaction_count")
    .sort_values("transaction_count", ascending=False)
)

print("\nTransaction Count by Payment Mode:")
print(payment_mode_transaction_count)

# Transaction Amount Analysis
payment_mode_amount_analysis = (
    transactions_df
    .groupby("payment_mode")["amount"]
    .agg(
        total_transaction_amount="sum",
        average_transaction_amount="mean",
        median_transaction_amount="median"
    )
    .round(2)
    .reset_index()
    .sort_values(
        "total_transaction_amount",
        ascending=False
    )
)

print("\nTransaction Amount by Payment Mode:")
print(payment_mode_amount_analysis)

# Create Payment Mode Performance Table
payment_mode_performance = (
    payment_mode_transaction_count
    .merge(
        payment_mode_amount_analysis,
        on="payment_mode",
        how="left"
    )
)

print("\n========================================")
print("PAYMENT MODE PERFORMANCE")
print("========================================")

print(payment_mode_performance)

# Transaction Status by Payment Mode
payment_mode_status = (
    transactions_df
    .groupby(
        ["payment_mode", "transaction_status"]
    )
    .size()
    .reset_index(name="transaction_count")
)

print("\nTransaction Status by Payment Mode:")
print(payment_mode_status)

# Calculate Success Rate by Payment Mode
payment_mode_success_rate = (
    transactions_df
    .assign(
        is_success=(
            transactions_df["transaction_status"] == "Success"
        ).astype(int)
    )
    .groupby("payment_mode")["is_success"]
    .mean()
    .mul(100)
    .round(2)
    .reset_index(name="success_rate")
    .sort_values("success_rate", ascending=False)
)

print("\nSuccess Rate by Payment Mode:")
print(payment_mode_success_rate)


# Calculate Failure Rate
payment_mode_failure_rate = (
    transactions_df
    .assign(
        is_failed=(
            transactions_df["transaction_status"] == "Failed"
        ).astype(int)
    )
    .groupby("payment_mode")["is_failed"]
    .mean()
    .mul(100)
    .round(2)
    .reset_index(name="failure_rate")
    .sort_values("failure_rate", ascending=False)
)

print("\nFailure Rate by Payment Mode:")
print(payment_mode_failure_rate)

# Create Final Payment Mode KPI Table
payment_mode_kpi = (
    payment_mode_performance
    .merge(
        payment_mode_success_rate,
        on="payment_mode",
        how="left"
    )
    .merge(
        payment_mode_failure_rate,
        on="payment_mode",
        how="left"
    )
)

print("\n========================================")
print("FINAL PAYMENT MODE KPI")
print("========================================")

print(payment_mode_kpi)

plt.figure(figsize=(8, 5))

sns.barplot(
    data=payment_mode_transaction_count,
    x="payment_mode",
    y="transaction_count"
)

plt.title("Transaction Volume by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))

sns.barplot(
    data=payment_mode_amount_analysis,
    x="payment_mode",
    y="total_transaction_amount"
)

plt.title("Total Transaction Amount by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Total Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))

sns.barplot(
    data=payment_mode_amount_analysis,
    x="payment_mode",
    y="average_transaction_amount"
)

plt.title("Average Transaction Amount by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Average Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))

sns.barplot(
    data=payment_mode_success_rate,
    x="payment_mode",
    y="success_rate"
)

plt.title("Transaction Success Rate by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Success Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Payment Mode KPIs
highest_volume_payment_mode = payment_mode_kpi.loc[
    payment_mode_kpi["transaction_count"].idxmax(),
    "payment_mode"
]

highest_value_payment_mode = payment_mode_kpi.loc[
    payment_mode_kpi["total_transaction_amount"].idxmax(),
    "payment_mode"
]

highest_average_payment_mode = payment_mode_kpi.loc[
    payment_mode_kpi["average_transaction_amount"].idxmax(),
    "payment_mode"
]

highest_success_payment_mode = payment_mode_kpi.loc[
    payment_mode_kpi["success_rate"].idxmax(),
    "payment_mode"
]

highest_failure_payment_mode = payment_mode_kpi.loc[
    payment_mode_kpi["failure_rate"].idxmax(),
    "payment_mode"
]

print("\n========================================")
print("PAYMENT MODE KPIs")
print("========================================")

print(
    f"Highest transaction volume: "
    f"{highest_volume_payment_mode}"
)

print(
    f"Highest transaction value: "
    f"{highest_value_payment_mode}"
)

print(
    f"Highest average transaction amount: "
    f"{highest_average_payment_mode}"
)

print(
    f"Highest success rate: "
    f"{highest_success_payment_mode}"
)

print(
    f"Highest failure rate: "
    f"{highest_failure_payment_mode}"
)


payment_mode_kpi.to_csv(
    "cleaned_data/payment_mode_performance.csv",
    index=False
)

print(
    "\nPayment mode performance saved successfully."
)


# ==========================================
# PAYMENT MODE BUSINESS INSIGHTS
# ==========================================

print("\n========================================")
print("PAYMENT MODE BUSINESS INSIGHTS")
print("========================================")

highest_volume_row = payment_mode_kpi.loc[
    payment_mode_kpi["transaction_count"].idxmax()
]

highest_value_row = payment_mode_kpi.loc[
    payment_mode_kpi["total_transaction_amount"].idxmax()
]

highest_average_row = payment_mode_kpi.loc[
    payment_mode_kpi["average_transaction_amount"].idxmax()
]

highest_success_row = payment_mode_kpi.loc[
    payment_mode_kpi["success_rate"].idxmax()
]

highest_failure_row = payment_mode_kpi.loc[
    payment_mode_kpi["failure_rate"].idxmax()
]

print(
    f"\n1. Highest transaction volume: "
    f"{highest_volume_row['payment_mode']} "
    f"({highest_volume_row['transaction_count']:.0f} transactions)"
)

print(
    f"2. Highest transaction value: "
    f"{highest_value_row['payment_mode']} "
    f"({highest_value_row['total_transaction_amount']:.2f})"
)

print(
    f"3. Highest average transaction amount: "
    f"{highest_average_row['payment_mode']} "
    f"({highest_average_row['average_transaction_amount']:.2f})"
)

print(
    f"4. Highest success rate: "
    f"{highest_success_row['payment_mode']} "
    f"({highest_success_row['success_rate']:.2f}%)"
)

print(
    f"5. Highest failure rate: "
    f"{highest_failure_row['payment_mode']} "
    f"({highest_failure_row['failure_rate']:.2f}%)"
)


print("\n========================================")
print("FINAL PAYMENT MODE BUSINESS SUMMARY")
print("========================================")

print(
    f"""
1. {highest_volume_row['payment_mode']} has the highest
   transaction volume.

2. {highest_value_row['payment_mode']} has the highest
   total transaction value.

3. {highest_average_row['payment_mode']} has the highest
   average transaction amount.

4. {highest_success_row['payment_mode']} has the highest
   transaction success rate.

5. {highest_failure_row['payment_mode']} has the highest
   transaction failure rate.

6. Payment modes should be evaluated using both transaction
   frequency and transaction value.

7. Payment modes with relatively higher failure rates should
   be investigated using additional operational data.

8. Payment mode KPIs can be incorporated into the Power BI
   dashboard for interactive analysis.
"""
)

# ==========================================
# TRANSACTION CATEGORY ANALYSIS
# ==========================================

transactions_df = pd.read_csv(
    "cleaned_data/transactions_prepared.csv"
)

transactions_df["transaction_date"] = pd.to_datetime(
    transactions_df["transaction_date"]
)

print("\nTransaction Data:")
print(transactions_df.head())


category_count = transactions_df["category"].value_counts()

print("\nTransaction Categories:")
print(category_count)

# Transaction Volume by Category
category_transaction_count = (
    transactions_df
    .groupby("category")["transaction_id"]
    .nunique()
    .reset_index(name="transaction_count")
    .sort_values("transaction_count", ascending=False)
)

print("\nTransaction Count by Category:")
print(category_transaction_count)

# Total Transaction Amount by Category
category_transaction_amount = (
    transactions_df
    .groupby("category")["amount"]
    .agg(
        total_transaction_amount="sum",
        average_transaction_amount="mean",
        median_transaction_amount="median"
    )
    .round(2)
    .reset_index()
    .sort_values(
        "total_transaction_amount",
        ascending=False
    )
)

print("\nTransaction Amount by Category:")
print(category_transaction_amount)

# Create Final Category Performance Table
category_performance = (
    category_transaction_count
    .merge(
        category_transaction_amount,
        on="category",
        how="left"
    )
)

print("\n========================================")
print("CATEGORY PERFORMANCE")
print("========================================")

print(category_performance)

# Transaction Type by Category
category_transaction_type = (
    transactions_df
    .groupby(
        ["category", "transaction_type"]
    )
    .size()
    .reset_index(name="transaction_count")
)

print("\nTransaction Type by Category:")
print(category_transaction_type)

# Category Success Rate
category_success_rate = (
    transactions_df
    .assign(
        is_success=(
            transactions_df["transaction_status"] == "Success"
        ).astype(int)
    )
    .groupby("category")["is_success"]
    .mean()
    .mul(100)
    .round(2)
    .reset_index(name="success_rate")
    .sort_values("success_rate", ascending=False)
)

print("\nSuccess Rate by Category:")
print(category_success_rate)

# Create Final Category KPI Table
category_kpi = (
    category_performance
    .merge(
        category_success_rate,
        on="category",
        how="left"
    )
)

print("\n========================================")
print("FINAL CATEGORY KPI")
print("========================================")

print(category_kpi)



plt.figure(figsize=(10, 6))

sns.barplot(
    data=category_transaction_count,
    x="category",
    y="transaction_count"
)

plt.title("Transaction Volume by Category")
plt.xlabel("Transaction Category")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))

sns.barplot(
    data=category_transaction_amount,
    x="category",
    y="total_transaction_amount"
)

plt.title("Total Transaction Amount by Category")
plt.xlabel("Transaction Category")
plt.ylabel("Total Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 6))

sns.barplot(
    data=category_transaction_amount,
    x="category",
    y="average_transaction_amount"
)

plt.title("Average Transaction Amount by Category")
plt.xlabel("Transaction Category")
plt.ylabel("Average Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))

sns.barplot(
    data=category_success_rate,
    x="category",
    y="success_rate"
)

plt.title("Transaction Success Rate by Category")
plt.xlabel("Transaction Category")
plt.ylabel("Success Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Identify Category KPIs
highest_volume_category = category_kpi.loc[
    category_kpi["transaction_count"].idxmax(),
    "category"
]

highest_value_category = category_kpi.loc[
    category_kpi["total_transaction_amount"].idxmax(),
    "category"
]

highest_average_category = category_kpi.loc[
    category_kpi["average_transaction_amount"].idxmax(),
    "category"
]

highest_success_category = category_kpi.loc[
    category_kpi["success_rate"].idxmax(),
    "category"
]

print("\n========================================")
print("CATEGORY KPIs")
print("========================================")

print(
    f"Highest transaction volume category: "
    f"{highest_volume_category}"
)

print(
    f"Highest transaction value category: "
    f"{highest_value_category}"
)

print(
    f"Highest average transaction category: "
    f"{highest_average_category}"
)

print(
    f"Highest success rate category: "
    f"{highest_success_category}"
)


category_kpi.to_csv(
    "cleaned_data/category_performance.csv",
    index=False
)

print(
    "\nCategory performance saved successfully."
)


# ==========================================
# CATEGORY BUSINESS INSIGHTS
# ==========================================

print("\n========================================")
print("TRANSACTION CATEGORY BUSINESS INSIGHTS")
print("========================================")

highest_volume_row = category_kpi.loc[
    category_kpi["transaction_count"].idxmax()
]

highest_value_row = category_kpi.loc[
    category_kpi["total_transaction_amount"].idxmax()
]

highest_average_row = category_kpi.loc[
    category_kpi["average_transaction_amount"].idxmax()
]

highest_success_row = category_kpi.loc[
    category_kpi["success_rate"].idxmax()
]

print(
    f"\n1. Highest transaction volume category: "
    f"{highest_volume_row['category']} "
    f"({highest_volume_row['transaction_count']:.0f} transactions)"
)

print(
    f"2. Highest transaction value category: "
    f"{highest_value_row['category']} "
    f"({highest_value_row['total_transaction_amount']:.2f})"
)

print(
    f"3. Highest average transaction category: "
    f"{highest_average_row['category']} "
    f"({highest_average_row['average_transaction_amount']:.2f})"
)

print(
    f"4. Highest success rate category: "
    f"{highest_success_row['category']} "
    f"({highest_success_row['success_rate']:.2f}%)"
)


print("\n========================================")
print("FINAL CATEGORY BUSINESS SUMMARY")
print("========================================")

print(
    f"""
1. {highest_volume_row['category']} has the highest
   transaction volume.

2. {highest_value_row['category']} has the highest
   total transaction value.

3. {highest_average_row['category']} has the highest
   average transaction amount.

4. {highest_success_row['category']} has the highest
   transaction success rate.

5. Transaction frequency and transaction value should
   be analyzed together to understand category performance.

6. Categories with relatively lower success rates should
   be investigated using additional operational data.

7. Category-level KPIs can be incorporated into the
   Power BI dashboard for interactive analysis.
"""
)