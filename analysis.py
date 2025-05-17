import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory
os.makedirs("output", exist_ok=True)

# Load dataset
df = pd.read_csv("dataset.csv")

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Add date and hour columns
df['date'] = df['timestamp'].dt.date
df['hour'] = df['timestamp'].dt.hour

# Basic info
print("Data Info:")
print(df.info())

# CTR Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['ctr'].dropna(), bins=50, kde=True, color='skyblue')
plt.title("CTR Distribution")
plt.xlabel("Click-Through Rate (CTR)")
plt.ylabel("Frequency")
plt.savefig("output/ctr_distribution.png")
plt.close()

# Average CTR by Device Type
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='device_type', y='ctr', estimator='mean', ci=None, palette='Set2')
plt.title("Average CTR by Device Type")
plt.ylabel("Average CTR")
plt.savefig("output/avg_ctr_device_type.png")
plt.close()

# Average CTR by Ad Category
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='ad_category', y='ctr', estimator='mean', ci=None, palette='Set3')
plt.title("Average CTR by Ad Category")
plt.ylabel("Average CTR")
plt.savefig("output/avg_ctr_ad_category.png")
plt.close()

# Average CTR by Region
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='region', y='ctr', estimator='mean', ci=None, palette='viridis')
plt.title("Average CTR by Region")
plt.ylabel("Average CTR")
plt.xticks(rotation=45)
plt.savefig("output/avg_ctr_region.png")
plt.close()

# Clicks vs Impressions Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='impressions', y='clicks', alpha=0.3)
plt.title("Clicks vs Impressions")
plt.xlabel("Impressions")
plt.ylabel("Clicks")
plt.savefig("output/clicks_vs_impressions.png")
plt.close()

# Hourly CTR Trend
hourly_ctr = df.groupby("hour")["ctr"].mean()
plt.figure(figsize=(10, 6))
sns.lineplot(x=hourly_ctr.index, y=hourly_ctr.values, marker='o')
plt.title("Hourly CTR Trend")
plt.xlabel("Hour of Day")
plt.ylabel("Average CTR")
plt.grid(True)
plt.savefig("output/hourly_ctr_trend.png")
plt.close()

# Daily CTR Trend
df.set_index("timestamp", inplace=True)
daily_ctr = df['ctr'].resample('D').mean()
plt.figure(figsize=(14, 6))
daily_ctr.plot()
plt.title("Daily CTR Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Average CTR")
plt.grid(True)
plt.savefig("output/daily_ctr_trend.png")
plt.close()