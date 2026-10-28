
# Sales Project — Organized Visualization Code

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
data = pd.read_csv("cleaned_sales.csv")
data["month"] = pd.to_datetime(data["month"])

# Create CHARTS folder automatically
os.makedirs("CHARTS", exist_ok=True)


# Helper function: Save chart and close figure
def save_chart(filename):
    plt.tight_layout()
    plt.savefig(
        os.path.join("CHARTS", filename),
        dpi=300,
        bbox_inches="tight"
    )
    print(f"Saved: CHARTS/{filename}")
    plt.close()


# Q1: Product-wise Total Revenue
def product_revenue_chart():
    product_revenue = data.groupby("product", as_index=False)["revenue"].sum()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=product_revenue, x="product", y="revenue", errorbar=None)
    plt.title("Product-wise Total Revenue")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    save_chart("product_revenue.png")


# Q2: Region-wise Total Revenue
def region_revenue_chart():
    region_revenue = data.groupby("region", as_index=False)["revenue"].sum()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=region_revenue, x="region", y="revenue", errorbar=None)
    plt.title("Region-wise Total Revenue")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.grid(axis="y")
    save_chart("region_revenue.png")


# Q3: Product-wise Units Sold
def product_units_chart():
    product_units = data.groupby("product", as_index=False)["units_sold"].sum()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=product_units, x="product", y="units_sold", errorbar=None)
    plt.title("Product-wise Units Sold")
    plt.xlabel("Product")
    plt.ylabel("Units Sold")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    save_chart("product_units.png")


# Q4: Product-wise Average Customer Rating
def product_rating_chart():
    product_rating = data.groupby("product", as_index=False)["customer_rating"].mean()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=product_rating, x="product", y="customer_rating", errorbar=None)
    plt.title("Product-wise Average Customer Rating")
    plt.xlabel("Product")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    save_chart("product_rating.png")


# Q5: Region-wise Average Customer Rating
def region_rating_chart():
    region_rating = data.groupby("region", as_index=False)["customer_rating"].mean()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=region_rating, x="region", y="customer_rating", errorbar=None)
    plt.title("Region-wise Average Customer Rating")
    plt.xlabel("Region")
    plt.ylabel("Average Rating")
    plt.grid(axis="y")
    save_chart("region_rating.png")


# Q6: Monthly Revenue Trend
def monthly_revenue_chart():
    monthly_revenue = data.groupby("month", as_index=False)["revenue"].sum()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=monthly_revenue, x="month", y="revenue", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.grid()
    save_chart("monthly_revenue.png")


# Q7: Revenue Distribution
def revenue_histogram():
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x="revenue", bins=20)
    plt.title("Revenue Distribution")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.grid(axis="y")
    save_chart("revenue_distribution.png")


# Q8: Units Sold vs Revenue
def units_revenue_scatter():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x="units_sold", y="revenue")
    plt.title("Units Sold vs Revenue")
    plt.xlabel("Units Sold")
    plt.ylabel("Revenue")
    plt.grid()
    save_chart("units_revenue_scatter.png")


# Q9: Product Rating Distribution
def product_rating_boxplot():
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x="product", y="customer_rating")
    plt.title("Product Rating Distribution")
    plt.xlabel("Product")
    plt.ylabel("Customer Rating")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    save_chart("product_rating_boxplot.png")


# Q10: Numerical Correlation Heatmap
def correlation_heatmap():
    correlation = data.corr(numeric_only=True)

    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    save_chart("correlation_heatmap.png")


# Run all 10 charts
if __name__ == "__main__":
    product_revenue_chart()
    region_revenue_chart()
    product_units_chart()
    product_rating_chart()
    region_rating_chart()
    monthly_revenue_chart()
    revenue_histogram()
    units_revenue_scatter()
    product_rating_boxplot()
    correlation_heatmap()

    print("\nAll 10 charts saved successfully!")
