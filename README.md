# Ads CTR Analysis and Forecasting

This Python project analyzes and visualizes a dataset of ad impressions, clicks, and user behavior to study and forecast Click-Through Rates (CTR).

## Dataset

**File:** `ads_ctr_dataset.csv`  
**Size:** 100,000 rows  
**Fields:**
1) `timestamp`: Event timestamp
2) `ad_id`, `user_id`: Identifiers
3) `device_type`: mobile, desktop, tablet
4) `ad_category`: tech, fashion, food, travel, finance
5) `region`: Geographical region
6) `impressions`, `clicks`, `ctr`: Engagement metrics

## Features

1) CTR distribution histogram
2) Average CTR by:
    Device type
    Ad category
    Region
3) Clicks vs Impressions scatter plot
4) Hourly CTR trends
5) Daily CTR time series plot

## Setup

```bash
pip install pandas matplotlib seaborn
```