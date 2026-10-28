import pandas as pd

df = pd.read_csv("matplotlib_sales_practice.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())