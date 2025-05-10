import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Data Loading and Preprocessing
# Load dataset
df = pd.read_csv('sales_data.csv')

# Handle missing values
df['Units Sold'].fillna(df['Units Sold'].median(), inplace=True)  # Fill missing Units Sold with median
df['Price Per Unit'] = df['Price Per Unit'].abs()  # Convert negative prices to positive
df.dropna(subset=['Total Revenue'], inplace=True)  # Drop rows with missing Total Revenue
df['Total Revenue'] = df['Units Sold'] * df['Price Per Unit']  # Recalculate Total Revenue if needed

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 2. Exploratory Data Analysis (EDA)
# Basic statistics using NumPy
units_sold_stats = {
    'Mean': np.mean(df['Units Sold']),
    'Median': np.median(df['Units Sold']),
    'Std Dev': np.std(df['Units Sold'])
}
revenue_stats = {
    'Mean': np.mean(df['Total Revenue']),
    'Median': np.median(df['Total Revenue']),
    'Std Dev': np.std(df['Total Revenue'])
}
print("Units Sold Stats:", units_sold_stats)
print("Total Revenue Stats:", revenue_stats)

# Group by Region and Product
region_revenue = df.groupby('Region')['Total Revenue'].agg(['sum', 'mean']).reset_index()
product_revenue = df.groupby('Product')['Total Revenue'].agg(['sum', 'mean']).reset_index()
print("\nRegion Revenue:\n", region_revenue)
print("\nProduct Revenue:\n", product_revenue)

# Top 3 products by total revenue
top_products = product_revenue.sort_values('sum', ascending=False).head(3)
print("\nTop 3 Products by Total Revenue:\n", top_products)

# 3. Data Visualization
# Bar chart: Total revenue per region
plt.figure(figsize=(8, 5))
plt.bar(region_revenue['Region'], region_revenue['sum'], color='skyblue')
plt.title('Total Revenue per Region')
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.savefig('revenue_per_region.png')
plt.close()

# Line chart: Monthly revenue trends
df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Total Revenue'].sum().reset_index()
monthly_revenue['Month'] = monthly_revenue['Month'].astype(str)
plt.figure(figsize=(10, 6))
plt.plot(monthly_revenue['Month'], monthly_revenue['Total Revenue'], marker='o')
plt.title('Monthly Revenue Trends')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_revenue_trends.png')
plt.close()

# Pie chart: Revenue proportion of top 3 products
plt.figure(figsize=(7, 7))
plt.pie(top_products['sum'], labels=top_products['Product'], autopct='%1.1f%%', startangle=140)
plt.title('Revenue Proportion of Top 3 Products')
plt.savefig('top_products_pie.png')
plt.close()

# Subplots: Revenue trends by region
regions = df['Region'].unique()
fig, axes = plt.subplots(len(regions), 1, figsize=(10, 4*len(regions)), sharex=True)
for i, region in enumerate(regions):
    region_data = df[df['Region'] == region].groupby('Month')['Total Revenue'].sum().reset_index()
    region_data['Month'] = region_data['Month'].astype(str)
    axes[i].plot(region_data['Month'], region_data['Total Revenue'], marker='o')
    axes[i].set_title(f'Revenue Trend - {region}')
    axes[i].set_ylabel('Total Revenue')
axes[-1].set_xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('region_revenue_trends.png')
plt.close()

# 4. Advanced Analysis
# Seasonal trends by month
df['Month_num'] = df['Date'].dt.month
seasonal_trends = df.groupby('Month_num')['Total Revenue'].mean().reset_index()
print("\nAverage Revenue by Month:\n", seasonal_trends)

# Simulate future sales (simple extrapolation based on mean and std)
historical_mean = df['Total Revenue'].mean()
historical_std = df['Total Revenue'].std()
np.random.seed(42)
future_months = 3
simulated_sales = np.random.normal(historical_mean, historical_std, future_months)
print("\nSimulated Future Sales (3 months):\n", simulated_sales)

# Predict region with highest revenue next quarter
region_growth = df.groupby('Region')['Total Revenue'].mean().pct_change().fillna(0)
next_quarter_pred = region_revenue.set_index('Region')['mean'] * (1 + region_growth)
print("\nPredicted Revenue Next Quarter by Region:\n", next_quarter_pred.sort_values(ascending=False))

# 5. Report and Insights
report = """
### Sales Data Analysis Report

**Key Insights:**
1. **Revenue Distribution**: The {} region generates the highest total revenue ({:.2f}), indicating strong market performance.
2. **Top Products**: The top 3 products ({}) contribute significantly to revenue, with {} leading at {:.2f}.
3. **Seasonal Trends**: Highest average revenue occurs in month {}, suggesting a seasonal peak.
4. **Future Outlook**: Based on growth rates, {} is predicted to lead revenue next quarter.

**Recommendations:**
1. **Focus on High-Performing Regions**: Allocate more resources to {} to capitalize on its strong performance.
2. **Promote Top Products**: Increase marketing for {} to boost sales further.
3. **Seasonal Campaigns**: Launch promotions in month {} to maximize revenue during peak periods.
4. **Monitor Growth**: Track {} closely, as it shows potential for future revenue leadership.
""".format(
    region_revenue.loc[region_revenue['sum'].idxmax(), 'Region'],
    region_revenue['sum'].max(),
    ', '.join(top_products['Product']),
    top_products.iloc[0]['Product'],
    top_products.iloc[0]['sum'],
    seasonal_trends.loc[seasonal_trends['Total Revenue'].idxmax(), 'Month_num'],
    next_quarter_pred.idxmax(),
    region_revenue.loc[region_revenue['sum'].idxmax(), 'Region'],
    top_products.iloc[0]['Product'],
    seasonal_trends.loc[seasonal_trends['Total Revenue'].idxmax(), 'Month_num'],
    next_quarter_pred.idxmax()
)

with open('sales_analysis_report.txt', 'w') as f:
    f.write(report)
print("\nReport saved to 'sales_analysis_report.txt'")