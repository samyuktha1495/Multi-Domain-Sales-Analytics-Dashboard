import pandas as pd

#load data
df = pd.read_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\rawdata\olist_orders.csv"
)

print("Original shape:", df.shape)
print(df.columns)

#GLOBAL CLEANING

#standardize
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('-', '_')
)

#drp dupes and remove unnamed cols
df = df.drop_duplicates()
df = df.loc[:, ~df.columns.str.contains('unnamed')]

#convert date columns
date_cols = [
    'order_purchase_timestamp',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# drop rows without orderid
df = df.dropna(subset=['order_id'])

print("After Step 2 shape:", df.shape)


df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_orders_step2_clean.csv",
    index=False
)

#TABLE CLEANING

#select req cols
df = df[[
    'order_id',
    'customer_id',
    'order_purchase_timestamp',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]]

#rename cols
df = df.rename(columns={
    'order_purchase_timestamp': 'purchase_date',
    'order_delivered_customer_date': 'delivered_date',
    'order_estimated_delivery_date': 'estimated_delivery_date'
})


df.info()
print(df.head())

df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_orders_final.csv",
    index=False
)
