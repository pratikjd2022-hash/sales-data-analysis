import pandas as pd 

data = pd.read_csv("matplotlib_sales_practice.csv")

# print(data.duplicated().sum())

# data["month"]=pd.to_datetime(data["month"])
# print(data.info())

# print(data["units_sold"].min())
# print(data["unit_price"].min())
# print(data["revenue"].min())
# print(data["customer_rating"].min())
# print(data["customer_rating"].max())


data["calculated_revenue"]=data["units_sold"]*data["unit_price"]
print((data["revenue"] != data["calculated_revenue"]).sum())

print(data[["units_sold", "unit_price", "revenue", "calculated_revenue"]].head())

data.drop(columns=["calculated_revenue"], inplace=True)
print(data.columns)

data.to_csv("DATA/cleaned_sales.csv", index=False)