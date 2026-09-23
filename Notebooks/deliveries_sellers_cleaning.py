import pandas as pd

#load
df = pd.read_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\rawdata\olist_sellers.csv"
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

#drop dupes and remove unnamed cols
df = df.drop_duplicates()
df = df.loc[:, ~df.columns.str.contains('unnamed')]

#drop rows without sellerid
df = df.dropna(subset=['seller_id'])

print("After Step 2 shape:", df.shape)


df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_sellers_step2_clean.csv",
    index=False
)

#TABLE CLEANING

#select req cols
df = df[[
    'seller_id',
    'seller_city',
    'seller_state'
]]

df.info()
print(df.head())

df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_sellers_final.csv",
    index=False
)
