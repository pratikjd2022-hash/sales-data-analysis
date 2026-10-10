import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv("cleaned_sales.csv")

# plt.figure(figsize=(10,6))
# product_revenue = data.groupby("product", as_index=False)["revenue"].sum()
# sns.barplot(
#     data=product_revenue,
#     x = "product",
#     y = "revenue",
#     errorbar= None
# )

# plt.title ("Product-wise Total Revenue")
# plt.xlabel("product")
# plt.ylabel("revenue")
# plt.xticks(rotation=45)
# plt.grid()

# plt.show()


# plt.figure(figsize=(10,6))
# region_revenue = data.groupby("region", as_index=False)["revenue"].sum()
# sns.barplot(
#     data=region_revenue,
#     x = "region",
#     y = "revenue",
#     errorbar= None
# )


# plt.figure(figsize=(10,6))

# product_units = data.groupby("product" , as_index=False)["units_sold"].sum()
# sns.barplot(
#     data=product_units,
#     x="product",
#     y="units_sold",
#     errorbar=None
# )


# plt.figure(figsize=(10,6))

# product_rating = data.groupby("product" , as_index=False)["customer_rating"].mean()

# sns.barplot(
#     data=product_rating,
#     x="product",
#     y="customer_rating",
#     errorbar=None
# )


# plt.figure(figsize=(10,6))

# monthly_revenue = data.groupby("month" , as_index=False)["revenue"].sum()

# sns.lineplot(
#     data=monthly_revenue,
#     x="month",
#     y="revenue",
#     marker="*"
# )



# plt.figure(figsize=(10,6))

# region_rating = data.groupby("region",as_index=False)["customer_rating"].mean()

# sns.barplot(
#     data=region_rating,
#     x="region",
#     y="customer_rating",
#     errorbar=None
# )

# plt.title("region-wise customer rating")
# plt.xlabel("region")
# plt.ylabel("customer_rating")
# plt.xticks(rotation=45)

# plt.grid()
# plt.show()



# plt.figure(figsize=(10,6))

# sns.histplot(
#     data=data,
#     x="revenue",
#     bins=20
# )

# plt.title("Revenue Distribution")
# plt.xlabel("Revenue")
# plt.ylabel("Frequency")
# plt.grid()
# plt.show()

# plt.figure(figsize=(10,6))

# sns.scatterplot(
#     data=data,
#     x="units_sold",
#     y="revenue"
# )

# plt.title("Units Sold vs Revenue")
# plt.xlabel("Units Sold")
# plt.ylabel("Revenue")
# plt.grid()
# plt.show()



plt.figure(figsize=(10, 6))

correlation = data.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()