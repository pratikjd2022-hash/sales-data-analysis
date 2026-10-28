import pandas as pd 
import numpy as np 

data = pd.read_csv("cleaned_sales.csv")

print(data.head())
print(data.shape)

# product_revenue = data.groupby("product")["revenue"].sum()
# product_revenue = product_revenue.sort_values(ascending=False)

# print(product_revenue)


# region_revenue = data.groupby("region")["revenue"].sum()
# region_revenue = region_revenue.sort_values(ascending=False)

# print(region_revenue)

# data ["calculated_revenue"]  = data["units_sold"]*data["unit_price"]
# print((data["revenue"] != data["calculated_revenue"]).sum())




# product_units = data.groupby("product")["units_sold"].sum()
# product_units = product_units.sort_values (ascending=False)
# print(product_units)




# product_rating = data.groupby("product")["customer_rating"].mean()
# product_rating = product_rating.sort_values(ascending=False)
# print(product_rating)




# region_rating = data.groupby("region")["customer_rating"].mean()
# region_rating = region_rating.sort_values(ascending=False)
# print(region_rating)


# highest_revenue = data.groupby("product")["revenue"].mean()
# highest_revenue = highest_revenue.sort_values(ascending=False)
# print(highest_revenue)

# highest_revenue = data.groupby("month")["revenue"].sum()
# highest_revenue = highest_revenue.sort_values(ascending=False)
# print(highest_revenue)

product = data.groupby("product").agg(
    total_revenue = ("revenue","sum"),
    avg_rating = ("customer_rating","mean")
)
print(product)
