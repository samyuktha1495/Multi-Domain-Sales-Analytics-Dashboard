import pandas as pd

#load data
df = pd.read_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\rawdata\olist_customers.csv"
)

print("Original shape:", df.shape)

#GLOBAL CLEANING

#standardize
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('-', '_')
)

#drop dupes and rename cols
df = df.drop_duplicates()
df = df.loc[:, ~df.columns.str.contains('unnamed')]

#drop rows without customerid
df = df.dropna(subset=['customer_id'])

print("After Step 2 shape:", df.shape)


df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_customers_step2_clean.csv",
    index=False
)

#TABLE CLEANING

#select req cols
df = df[[
    'customer_id',
    'customer_city',
    'customer_state'
]]

df.info()
print(df.head())


df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_customers_final.csv",
    index=False
)
