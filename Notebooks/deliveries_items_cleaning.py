import pandas as pd

# load raw data
df = pd.read_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\rawdata\olist_order_items.csv"
)

print("Original shape:", df.shape)
print(df.columns)


#GLOBAL CLEANING

# standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('-', '_')
)

# remove duplicates
df = df.drop_duplicates()

# remove unnamed columns
df = df.loc[:, ~df.columns.str.contains('unnamed')]

# drop rows without essential keys
df = df.dropna(subset=['order_id', 'seller_id'])

print("After Step 2 shape:", df.shape)

# save step 2 cleaned file
df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_order_items_step2_clean.csv",
    index=False
)


#TABLE CLEANING

# select only required columns
df = df[[
    'order_id',
    'seller_id'
]]

df.info()
print(df.head())

# save final cleaned table
df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_order_items_final.csv",
    index=False
)
