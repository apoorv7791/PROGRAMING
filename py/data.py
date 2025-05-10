import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.dates as mdates

# Set the style for our plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

# 1. Data Loading and Preprocessing
print("1. Data Loading and Preprocessing")
print("---------------------------------")

# Create sample data since we don't have the actual CSV file
np.random.seed(42)  # For reproducibility

# Generate dates for the past year
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Define regions and products
regions = ['North', 'South', 'East', 'West', 'Central']
products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch', 'TV', 'Camera']

# Create a DataFrame with random data
n_samples = 1000
data = {
    'Date': np.random.choice(dates, n_samples),
    'Region': np.random.choice(regions, n_samples),
    'Product': np.random.choice(products, n_samples),
    'Units Sold': np.random.randint(1, 50, n_samples),
    'Price Per Unit': np.random.uniform(50, 1000, n_samples).round(2),
}

# Introduce some missing values and errors
data['Units Sold'][np.random.choice(range(n_samples), 20)] = np.nan
data['Price Per Unit'][np.random.choice(range(n_samples), 10)] = -1

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Total Revenue
df['Total Revenue'] = df['Units Sold'] * df['Price Per Unit']

print(f"Original dataset shape: {df.shape}")
print("\nFirst few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Handle missing or erroneous data
print("\nHandling missing and erroneous data...")

# Replace negative prices with the median price for that product
for product in products:
    median_price = df[(df['Product'] == product) & (df['Price Per Unit'] > 0)]['Price Per Unit'].median()
    df.loc[(df['Product'] == product) & (df['Price Per Unit'] <= 0), 'Price Per Unit'] = median_price

# Fill missing Units Sold with the median for that product
for product in products:
    median_units = df[(df['Product'] == product) & (df['Units Sold'].notna())]['Units Sold'].median()
    df.loc[(df['Product'] == product) & (df['Units Sold'].isna()), 'Units Sold'] = median_units

# Recalculate Total Revenue
df['Total Revenue'] = df['Units Sold'] * df['Price Per Unit']

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Add Month and Year columns for easier analysis
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Month_Year'] = df['Date'].dt.strftime('%Y-%m')

print("\nAfter cleaning, missing values in each column:")
print(df.isnull().sum())

print("\nDataset summary statistics:")
print(df.describe())

# 2. Exploratory Data Analysis (EDA)
print("\n\n2. Exploratory Data Analysis")
print("-----------------------------")

# Calculate basic statistics using NumPy
units_sold_mean = np.mean(df['Units Sold'])
units_sold_median = np.median(df['Units Sold'])
units_sold_std = np.std(df['Units Sold'])

revenue_mean = np.mean(df['Total Revenue'])
revenue_median = np.median(df['Total Revenue'])
revenue_std = np.std(df['Total Revenue'])

print(f"Units Sold - Mean: {units_sold_mean:.2f}, Median: {units_sold_median:.2f}, Std Dev: {units_sold_std:.2f}")
print(f"Total Revenue - Mean: ${revenue_mean:.2f}, Median: ${revenue_median:.2f}, Std Dev: ${revenue_std:.2f}")

# Group by Region and Product
region_product_revenue = df.groupby(['Region', 'Product']).agg({
    'Total Revenue': ['sum', 'mean'],
    'Units Sold': ['sum', 'mean']
}).reset_index()

print("\nRevenue by Region and Product (Top 10):")
print(region_product_revenue.sort_values(('Total Revenue', 'sum'), ascending=False).head(10))

# Identify top 3 products by total revenue
top_products = df.groupby('Product')['Total Revenue'].sum().sort_values(ascending=False).head(3)
print("\nTop 3 Products by Total Revenue:")
print(top_products)

# 3. Data Visualization
print("\n\n3. Data Visualization")
print("---------------------")

# Create a figure with 2x2 subplots
fig = plt.figure(figsize=(20, 16))

# 1. Bar chart showing total revenue per region
ax1 = fig.add_subplot(2, 2, 1)
region_revenue = df.groupby('Region')['Total Revenue'].sum().sort_values(ascending=False)
region_revenue.plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_title('Total Revenue by Region', fontsize=16)
ax1.set_ylabel('Total Revenue ($)', fontsize=12)
ax1.set_xlabel('Region', fontsize=12)
ax1.tick_params(axis='x', rotation=0)
for i, v in enumerate(region_revenue):
    ax1.text(i, v + 0.1, f"${v:.2f}", ha='center', fontsize=10)

# 2. Line chart showing monthly revenue trends
ax2 = fig.add_subplot(2, 2, 2)
monthly_revenue = df.groupby('Month_Year')['Total Revenue'].sum()
monthly_revenue.plot(kind='line', marker='o', color='green', ax=ax2)
ax2.set_title('Monthly Revenue Trends', fontsize=16)
ax2.set_ylabel('Total Revenue ($)', fontsize=12)
ax2.set_xlabel('Month', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)

# 3. Pie chart for top 3 products
ax3 = fig.add_subplot(2, 2, 3)
top_products.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax3, 
                 colors=sns.color_palette("viridis", 3))
ax3.set_title('Revenue Proportion of Top 3 Products', fontsize=16)
ax3.set_ylabel('')

# 4. Subplots to compare revenue trends across regions
ax4 = fig.add_subplot(2, 2, 4)
pivot_df = df.pivot_table(index='Month_Year', columns='Region', values='Total Revenue', aggfunc='sum')
pivot_df.plot(kind='line', marker='.', ax=ax4)
ax4.set_title('Monthly Revenue Trends by Region', fontsize=16)
ax4.set_ylabel('Total Revenue ($)', fontsize=12)
ax4.set_xlabel('Month', fontsize=12)
ax4.grid(True, linestyle='--', alpha=0.7)
ax4.legend(title='Region')

plt.tight_layout()
plt.show()

# 4. Advanced Analysis
print("\n\n4. Advanced Analysis")
print("-------------------")

# Seasonal trends by month
monthly_sales = df.groupby(['Month'])['Total Revenue'].sum().reset_index()
print("Monthly Sales Trends (Seasonal Analysis):")
print(monthly_sales)

# Calculate month-over-month growth rate
monthly_revenue_series = df.groupby('Month_Year')['Total Revenue'].sum()
monthly_growth = monthly_revenue_series.pct_change() * 100
print("\nMonth-over-Month Revenue Growth Rate:")
print(monthly_growth)

# Simulate future sales based on historical data
# Using a simple moving average model for prediction
def simulate_future_sales(historical_data, periods=3, window=3):
    """Simulate future sales using a moving average model"""
    # Calculate the moving average
    ma = historical_data.rolling(window=window).mean()
    
    # Use the last moving average value as the base
    last_ma = ma.iloc[-1]
    
    # Add some random noise to simulate variability
    future_values = []
    for _ in range(periods):
        # Add random noise (±10% of the last moving average)
        noise = np.random.uniform(-0.1, 0.1) * last_ma
        future_values.append(last_ma + noise)
    
    return future_values

# Simulate future monthly sales
future_months = ['2024-01', '2024-02', '2024-03']
future_sales = simulate_future_sales(monthly_revenue_series, periods=3)

print("\nSimulated Future Monthly Sales:")
for month, sales in zip(future_months, future_sales):
    print(f"{month}: ${sales:.2f}")

# Predict the region that might generate the most revenue next quarter
region_growth = df.pivot_table(
    index='Month_Year', 
    columns='Region', 
    values='Total Revenue', 
    aggfunc='sum'
).pct_change().mean() * 100

print("\nAverage Monthly Growth Rate by Region:")
print(region_growth)

# Predict next quarter revenue by region
current_region_revenue = df.groupby('Region')['Total Revenue'].sum()
predicted_region_revenue = current_region_revenue * (1 + region_growth/100) ** 3  # 3 months

print("\nPredicted Revenue by Region for Next Quarter:")
print(predicted_region_revenue.sort_values(ascending=False))

top_region_next_quarter = predicted_region_revenue.idxmax()
print(f"\nThe region predicted to generate the most revenue next quarter is: {top_region_next_quarter}")

# 5. Report and Insights
print("\n\n5. Report and Insights")
print("---------------------")

print("Key Insights:")
print("-------------")
print(f"1. The {region_revenue.index[0]} region generated the highest total revenue (${region_revenue.iloc[0]:.2f}).")
print(f"2. The top 3 products by revenue are {', '.join(top_products.index.tolist())}.")
print(f"3. {monthly_sales['Month'].iloc[monthly_sales['Total Revenue'].argmax()]} was the month with the highest sales.")
print(f"4. {top_region_next_quarter} is predicted to be the highest-revenue region in the next quarter.")

# Calculate product-region combinations with highest revenue
product_region_combo = df.groupby(['Product', 'Region'])['Total Revenue'].sum().sort_values(ascending=False)
best_combo = product_region_combo.index[0]
print(f"5. The {best_combo[0]} product sells best in the {best_combo[1]} region.")

print("\nActionable Recommendations:")
print("--------------------------")
print(f"1. Focus marketing efforts on {top_region_next_quarter} region, which is predicted to have the highest growth.")
print(f"2. Increase inventory for {top_products.index[0]} products, especially during {monthly_sales['Month'].iloc[monthly_sales['Total Revenue'].argmax()]}.")
print(f"3. Consider special promotions for {', '.join(top_products.index[1:].tolist())} to boost their sales further.")
print(f"4. Investigate why {region_revenue.index[-1]} region has the lowest sales and develop strategies to improve performance.")
print(f"5. Create targeted marketing campaigns for {best_combo[0]} in {best_combo[1]} region to capitalize on this successful combination.")