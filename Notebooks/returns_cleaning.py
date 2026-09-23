import pandas as pd

#loading csv
df = pd.read_csv(r"C:\Users\ADMIN\OneDrive\Documents\DA 2\rawdata\online_retail.csv")

#GLOBAL CLEANING

#standardize cols
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
)

#remove duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)

print(f"Removed {before - after} duplicate rows")

#remove unnamed cols
df = df.loc[:, ~df.columns.str.contains('unnamed')]

#missing customer id
df = df.dropna(subset=['customerid'])

#fixing datatypes
df['customerid'] = df['customerid'].astype(int)
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unitprice'] = pd.to_numeric(df['unitprice'], errors='coerce')
df['invoicedate'] = pd.to_datetime(df['invoicedate'])


#preview
#print(df.head())

df.to_csv(r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\online_retail_step2_clean.csv", index=False)

#TABLE CLEANING

#selecting req cols
df = df[[
    'invoiceno',
    'stockcode',
    'quantity',
    'invoicedate',
    'unitprice',
    'customerid',
    'country'
]]

#rename cols
df = df.rename(columns={
    'invoiceno': 'invoice_no',
    'stockcode': 'stock_code',
    'invoicedate': 'invoice_date',
    'unitprice': 'unit_price',
    'customerid': 'customer_id'
})


df.info()
df.head()

df.to_csv(r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\online_retail_final.csv",index=False)
