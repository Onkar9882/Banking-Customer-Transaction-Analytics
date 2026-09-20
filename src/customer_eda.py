import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned customer dataset
customer_df = pd.read_csv("cleaned_data/customers_cleaned.csv")
print("Cleaned customer data loaded successfully")

print("\nDataset shape:")
print(customer_df.shape)

print("\nFirst 5 records:")
print(customer_df.head())

print("\ncolumn names:")
print(customer_df.columns.tolist())

print("\nData Types:")
print(customer_df.dtypes)

# Customer data overview
print("\n ===== Customer Data Overview =====")

print("\nDataset information:")
print(customer_df.info())

print("\nDataset Descriptive Statistics:")
print(customer_df.describe())

print("\nNumerical Columns:")
print(customer_df.select_dtypes(include=np.number).columns.tolist())

print("\nCategorical columns:")
print(customer_df.select_dtypes(include="object").columns.tolist())


# Customer age analysis
print("\n ===== CUSTOMER AGE ANALYSIS =====")

print("\nAge statistics:")
print("Minimum age:",customer_df["age"].min())
print("Maximum age:",customer_df["age"].max())
print("Average age:",round(customer_df["age"].mean(),2))
print("Median age:",customer_df["age"].median())

print("\nAge group distribution:")
customer_df["age group"] = pd.cut(customer_df["age"],bins=[20,30,40,50,60,70],labels=["21-30","31-40","41-50","51-60","61-70"],include_lowest=True)

print(customer_df["age group"].value_counts().sort_index())

# Age distribution visualization
plt.figure(figsize=(8,5))
sns.histplot(data=customer_df,x="age",bins=15,kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of customers")
plt.tight_layout()
plt.show()

# Gender distribution analysis
print("\n ===== GENDER DISTRIBUTION =====")

# Gender distribution analysis

print("\n========== GENDER DISTRIBUTION ==========")

gender_counts = customer_df["gender"].value_counts()

print("\nNumber of customers by gender:")
print(gender_counts)

print("\nPercentage of customers by gender:")
gender_percentage = (
    customer_df["gender"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print(gender_percentage)

# Gender distribution visualization
plt.figure(figsize=(7,5))
sns.countplot(data=customer_df,x="gender")
plt.title("Customer Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Gender")
plt.tight_layout()
plt.show()


# Occupation analysis
print("\n ===== OCCUPATION ANALYSIS =====")

occupation_count = customer_df["occupation"].value_counts()
print("\nNumber of customers by occupations:")
print(occupation_count)

print("\nTop 5 occupations:")
print(occupation_count.head(5))

# Occupation distribution visualization
plt.figure(figsize=(9,5))
sns.countplot(data=customer_df,y="occupation",order=occupation_count.index)
plt.title("Customer Occupation Distributions")
plt.ylabel("Occupation")
plt.xlabel("Number Of Occupations")
plt.tight_layout()
plt.show()


# Income analysis
print("\n ===== INCOME ANALYSIS =====")
print("\nIncome Statistics:")
print("Minimum Income:",customer_df["income"].min())
print("Maximum Income:",customer_df["income"].max())
print("Average Income:",round(customer_df["income"].mean(),2))
print("Median Income:",customer_df["income"].median())

print("\nIncome Quartiles:")
print(customer_df["income"].quantile([0.25, 0.50, 0.75]))


# Create income groups
customer_df["income_group"] = pd.cut(
    customer_df["income"],
    bins=[0, 50000, 100000, 150000, float("inf")],
    labels=[
        "Low Income",
        "Lower-Middle Income",
        "Upper-Middle Income",
        "High Income"
    ]
)

income_group_counts = customer_df["income_group"].value_counts()

print("\nIncome Group Distribution:")
print(income_group_counts)

# Income distribution visualization

plt.figure(figsize=(9, 5))

sns.histplot(
    data=customer_df,
    x="income",
    bins=30,
    kde=True
)

plt.title("Customer Income Distribution")
plt.xlabel("Income")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()


# City and state distribution analysis
print("\n ===== CITY AND STATE DISTRIBUTION =====")
print("\nTop 10 city by customer count:")
city_count = customer_df["city"].value_counts()
print(city_count.head(10))

print("\nTop 10 state by customer count:")
state_count = customer_df["state"].value_counts()
print(state_count.head(10))

# Top 10 cities visualization
top_10_cities = city_count.head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_10_cities.values, y=top_10_cities.index)
plt.title("Top 10 cities by customer count")
plt.xlabel("Number of customer")
plt.ylabel("city")
plt.tight_layout()
plt.show()


# Top 10 states visualization
top_10_states = state_count.head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_10_states.values, y=top_10_states.index)
plt.title("Top 10 states by customer count")
plt.xlabel("Number of customer")
plt.ylabel("state")
plt.tight_layout()
plt.show()


# Customer Joining Trend Analysis

# Convert join_date to datetime
customer_df["join_date"] = pd.to_datetime(customer_df["join_date"])

# Analyze customer joining by year
customer_df["join_year"] = customer_df["join_date"].dt.year
yearly_joins = customer_df["join_year"].value_counts().sort_index()
print("\nCustomer joining trend by year:")
print(yearly_joins)

plt.figure(figsize=(8,6))
sns.countplot(data=customer_df, x="join_year")
plt.title("Customer joining trend by year")
plt.xlabel("year")
plt.ylabel("Number of customer")
plt.tight_layout()
plt.show()


# Find the highest and lowest joining years
highest_join_year = yearly_joins.idxmax()
highest_join_count = yearly_joins.max()

lowest_join_year = yearly_joins.idxmin()
lowest_join_count = yearly_joins.min()

print("\nHighest customer joining year:")
print(highest_join_year,"-",highest_join_count,"customers")

print("\nLowest customer joining year:")
print(lowest_join_year,"-",lowest_join_count,"customers")


# Monthly Customer Joining Trend

# Create a monthly period
customer_df["join_month"] = customer_df["join_date"].dt.month 
monthly_joins = (customer_df["join_month"].value_counts().sort_index())
print("\nMonthly customer joining trend:")
print(monthly_joins)

monthly_joins_df = monthly_joins.reset_index()

monthly_joins_df.columns = ["join_month", "customer_count"]

print("\nMonthly Joining Data:")
print(monthly_joins_df.head())

# Create the monthly trend chart
plt.figure(figsize=(12,7))
plt.plot(monthly_joins_df["join_month"].astype(str),monthly_joins_df["customer_count"],marker="o")
plt.title("Monthly customer joining trend")
plt.xlabel("join month")
plt.ylabel("customer count")
plt.tight_layout()
plt.show()


#Find highest and lowest months
highest_join_month = monthly_joins.idxmax()
highest_month_count = monthly_joins.max()

lowest_join_month = monthly_joins.idxmin()
lowest_month_count = monthly_joins.min()

print("\nHighest customer joining month:")
print(highest_join_month,"-",highest_month_count,"customers")

print("\nLowest customer joining month:")
print(lowest_join_month,"-",lowest_month_count,"customers")

# Customer Income vs Age Analysis
correlation = customer_df["age"].corr(customer_df["income"])
print("\nCorrelation between the age and income:")
print(round(correlation,2))

plt.figure(figsize=(12,6))
sns.scatterplot(data=customer_df, x="age", y="income")
plt.title("Customer age and income analysis")
plt.xlabel("age")
plt.ylabel("income")
plt.tight_layout()
plt.show()

# Check the income groups
print("\nCustomer distribution by group:")
print(customer_df["income_group"].value_counts().sort_index())

income_occupation = pd.crosstab(
    customer_df["occupation"],
    customer_df["income_group"]
)

print("\nIncome Group vs Occupation:")
print(income_occupation)

plt.figure(figsize=(8,5))
sns.heatmap(income_occupation,annot=True,fmt="d",cmap="Blues")
plt.title("Customer Segmentation by Income Group and Occupation")
plt.xlabel("Income group")
plt.ylabel("occupation")
plt.tight_layout()
plt.show()

largest_segment = income_occupation.stack().idxmax()
largest_segment_count = income_occupation.stack().max()

print("\nLargest Customer Segment:")
print("Occupation:", largest_segment[0])
print("Income Group:", largest_segment[1])
print("Customers:", largest_segment_count)

# Calculate customer tenure
today = pd.Timestamp.today()
customer_df["tenure days"] = (today - customer_df["join_date"]).dt.days

customer_df["tenure_years"] = (customer_df["tenure days"]/365).round(1)

print("\nCustomer Tenure:")
print(customer_df[["customer_id", "join_date", "tenure_years"]].head())

# Create tenure groups
customer_df["tenure_group"] = pd.cut(
    customer_df["tenure_years"],
    bins=[0, 1, 2, 3, 4, 5, float("inf")],
    labels=[
        "Less than 1 Year",
        "1-2 Years",
        "2-3 Years",
        "3-4 Years",
        "4-5 Years",
        "5+ Years"
    ],
    include_lowest=True
)

tenure_counts = customer_df["tenure_group"].value_counts().sort_index()

print("\nCustomer Distribution by Tenure:")
print(tenure_counts)

plt.figure(figsize=(10, 5))

sns.countplot(
    data=customer_df,
    x="tenure_group",
    order=tenure_counts.index
)

plt.title("Customer Distribution by Tenure")
plt.xlabel("Customer Tenure")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()


print("\n========== CUSTOMER PROFILE SUMMARY ==========")

total_customers = customer_df["customer_id"].nunique()
average_age = customer_df["age"].mean()
average_income = customer_df["income"].mean()
median_income = customer_df["income"].median()
average_tenure = customer_df["tenure_years"].mean()

print("Total Customers:", total_customers)
print("Average Age:", round(average_age, 2))
print("Average Income:", round(average_income, 2))
print("Median Income:", round(median_income, 2))
print("Average Tenure:", round(average_tenure, 2), "years")


most_common_gender = customer_df["gender"].mode()[0]
most_common_occupation = customer_df["occupation"].mode()[0]
most_common_income_group = customer_df["income_group"].mode()[0]
most_common_tenure_group = customer_df["tenure_group"].mode()[0]

print("\nMost Common Gender:", most_common_gender)
print("Most Common Occupation:", most_common_occupation)
print("Most Common Income Group:", most_common_income_group)
print("Most Common Tenure Group:", most_common_tenure_group)


customer_profile = {
    "Total Customers": total_customers,
    "Average Age": round(average_age, 2),
    "Average Income": round(average_income, 2),
    "Median Income": round(median_income, 2),
    "Average Tenure": round(average_tenure, 2),
    "Most Common Gender": most_common_gender,
    "Most Common Occupation": most_common_occupation,
    "Most Common Income Group": most_common_income_group,
    "Most Common Tenure Group": most_common_tenure_group
}

print("\nCustomer Profile Summary:")
print(customer_profile)