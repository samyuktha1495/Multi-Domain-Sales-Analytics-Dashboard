import pandas as pd

#load data
df = pd.read_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\rawdata\amazon_reviews.csv",
    engine="python",
    on_bad_lines="skip"
)

print("Original shape:", df.shape)
print("Original columns:", df.columns)

#GLOBAL CLEANING 

#standardize cols
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('-', '_')
)

#drop duplicates
df = df.drop_duplicates()

#remove unnamed cols
df = df.loc[:, ~df.columns.str.contains('unnamed')]

#striping whitespace
df['reviewer_name'] = df['reviewer_name'].astype(str).str.strip()
df['rating'] = df['rating'].astype(str).str.strip()
df['review_count'] = df['review_count'].astype(str).str.strip()

#drop rows where reviewer name missing
df = df[df['reviewer_name'] != '']

print("After cleaning shape:", df.shape)

df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\amazon_reviews_step2_clean.csv",
    index=False
)

#TABLE CLEANING

#select req cols
df = df[[
    'reviewer_name',
    'country',
    'review_count',
    'rating'
]]

#rename cols
df = df.rename(columns={
    'reviewer_name': 'reviewer_id'
})


df.info()
print(df.head())


df.to_csv(
    r"C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\amazon_reviews_final.csv",
    index=False
)
