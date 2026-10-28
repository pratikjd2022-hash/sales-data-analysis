
import pandas as pd
import numpy as np
from pathlib import Path

# 1. Load data
script_folder = Path(__file__).resolve().parent
file_path = script_folder / "cleaned_sales.csv"

data = pd.read_csv(file_path)
data["month"] = pd.to_datetime(data["month"])

print("===== SALES DATA ANALYSIS =====")
print("Dataset Shape:", data.shape)

print("\nFirst 5 Rows:")
print(data.head())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:", data.duplicated().sum())

print("\nNumerical Summary:")
print(data.describe())

# 2. Revenue summary
print("\n===== REVENUE SUMMARY =====")
print("Mean Revenue:", np.mean(data["revenue"]))
print("Median Revenue:", data["revenue"].median())
print("Maximum Revenue:", np.max(data["revenue"]))
print("Minimum Revenue:", np.min(data["revenue"]))

# 3. Product-wise revenue
product_revenue = data.groupby("product")["revenue"].sum()
product_revenue = product_revenue.sort_values(ascending=False)

print("\n===== PRODUCT-WISE REVENUE =====")
print(product_revenue)

# 4. Region-wise revenue
region_revenue = data.groupby("region")["revenue"].sum()
region_revenue = region_revenue.sort_values(ascending=False)

print("\n===== REGION-WISE REVENUE =====")
print(region_revenue)

# 5. Product-wise units sold
product_units = data.groupby("product")["units_sold"].sum()
product_units = product_units.sort_values(ascending=False)

print("\n===== PRODUCT-WISE UNITS SOLD =====")
print(product_units)

# 6. Average ratings
product_rating = data.groupby("product")["customer_rating"].mean()
region_rating = data.groupby("region")["customer_rating"].mean()

print("\n===== AVERAGE RATING BY PRODUCT =====")
print(product_rating.round(2).sort_values(ascending=False))

print("\n===== AVERAGE RATING BY REGION =====")
print(region_rating.round(2).sort_values(ascending=False))

# 7. Monthly revenue
monthly_revenue = data.groupby(
    data["month"].dt.to_period("M")
)["revenue"].sum()

print("\n===== MONTHLY REVENUE =====")
print(monthly_revenue.sort_values(ascending=False))

# 8. Business insights
print("\n===== BUSINESS INSIGHTS =====")
print("Highest Revenue Product:", product_revenue.idxmax())
print("Highest Revenue Region:", region_revenue.idxmax())
print("Most Units Sold Product:", product_units.idxmax())
print("Highest Rated Product:", product_rating.idxmax())
print("Highest Revenue Month:", monthly_revenue.idxmax())

print("\nSales Data Analysis Completed!")
