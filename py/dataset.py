import pandas as pd
import numpy as np

# Create sample data
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
regions = ['North', 'South', 'East', 'West']
products = ['Laptop', 'Phone', 'Tablet']
data = {
    'Date': np.random.choice(dates, 1000),
    'Region': np.random.choice(regions, 1000),
    'Product': np.random.choice(products, 1000),
    'Units Sold': np.random.randint(1, 100, 1000),
    'Price Per Unit': np.random.uniform(100, 1000, 1000)
}
df = pd.DataFrame(data)
df['Total Revenue'] = df['Units Sold'] * df['Price Per Unit']
# Introduce some missing and negative values
df.loc[np.random.choice(df.index, 50), 'Units Sold'] = np.nan
df.loc[np.random.choice(df.index, 20), 'Price Per Unit'] = -df['Price Per Unit']
df.to_csv('sales_data.csv', index=False)