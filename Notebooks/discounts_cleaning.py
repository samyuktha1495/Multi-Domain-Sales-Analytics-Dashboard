import pandas as pd

df = pd.read_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\rawdata\amazon_sale_report.csv",
    low_memory=False
)

#GLOBAL CLEANING

# standardize cols
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('-', '_')
)

# remove duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Removed {before - after} duplicate rows")

# remove unnamed columns
df = df.loc[:, ~df.columns.str.contains('unnamed')]

# fixing datatypes
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# droP unnecesary cols
df = df.dropna(subset=['sku', 'date', 'amount'])


df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\amazon_sale_step2_clean.csv",
    index=False
)

#TABLE CLEANING

#select req cols
df = df[[
    'date',
    'sku',
    'qty',
    'amount',
    'promotion_ids'
]]

#discount flag
df['discount_flag'] = df['promotion_ids'].notna().astype(int)

#renaming cols
df = df.rename(columns={
    'date': 'order_date',
    'sku': 'product_id',
    'qty': 'quantity',
    'amount': 'sales_amount'
})

df.info()
df.head()

df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\amazon_sale_pricing_final.csv",
    index=False
)
