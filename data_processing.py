import pandas as pd
import os

# Paths
data_dir = 'data'
raw_filename = 'zomato.csv'
raw_path = os.path.join(data_dir, raw_filename)

# Load raw data with fallback encoding
try:
    df = pd.read_csv(raw_path)
except UnicodeDecodeError:
    df = pd.read_csv(raw_path, encoding='latin-1')

# Drop duplicates
df.drop_duplicates(inplace=True)

# Select relevant columns
cols = ['Restaurant ID', 'Restaurant Name', 'City', 'Cuisines',
        'Average Cost for two', 'Price range', 'Aggregate rating', 'Votes', 'Latitude', 'Longitude']
df = df[cols].copy()

# Cleaning function
def clean_data(df):
    # Lowercase and extract primary cuisine
    df['Cuisines'] = df['Cuisines'].str.lower().str.split(',').str[0]
    # Cost buckets
    max_cost = df['Average Cost for two'].max()
    df['CostBucket'] = pd.cut(
        df['Average Cost for two'],
        bins=[0, 300, 700, max_cost + 1],
        labels=['low', 'medium', 'high'],
        include_lowest=True
    )
    # Rename rating field
    df['Rating'] = df['Aggregate rating']
    # Drop rows with any missing values in key columns
    return df.dropna(subset=['Cuisines', 'CostBucket', 'Rating', 'Latitude', 'Longitude'])

# Clean and save
enabled = True
cleaned = clean_data(df)
os.makedirs(data_dir, exist_ok=True)
cleaned.to_csv(os.path.join(data_dir, 'zomato_clean.csv'), index=False)
print(f"Data cleaned ({len(cleaned)} rows) and saved to {os.path.join(data_dir, 'zomato_clean.csv')}")