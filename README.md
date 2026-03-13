# Revenue Operations KPI Dashboard

## Overview
This project simulates a revenue operations analytics workflow for a B2B company. It uses synthetic sales, lead, customer, campaign, and target data to build a multi-page KPI dashboard focused on business performance, funnel conversion, regional trends, and target-versus-actual analysis.

## Business Goal
Create an executive-ready dashboard to help leadership track:
- revenue trends
- lead funnel conversion
- regional performance
- target vs actual performance
- average order value
- pipeline distribution by stage

## Tools Used
- Python
- SQLite
- SQL
- Excel
- GitHub

## Dataset Tables
The project uses these datasets:
- leads
- customers
- orders
- campaigns
- sales reps
- targets

## Dashboard Pages
### 1. Executive Overview
Shows top-level KPIs including total revenue, total orders, average order value, and lead-to-customer conversion, along with monthly revenue trend and revenue by region.

### 2. Funnel & Conversion Analysis
Shows total leads, customers, conversion rate, won leads, lead funnel by stage, and stage share distribution.

### 3. Regional Performance
Compares revenue, orders, and average order value across regions to identify the strongest and weakest markets.

### 4. Target vs Actual Performance
Compares actual revenue to target revenue and highlights variance trends and regional consistency.

## Key Insights
- Total revenue reached $10.35M across 2,200 orders.
- Lead-to-customer conversion rate was 28.93%.
- North was the strongest revenue region, followed by South.
- West showed the highest average order value but lower order volume.
- North and South contributed most of total revenue.
- December 2025 was a major outlier month in target-vs-actual performance.

## Project Structure
```text
revenue_operations_kpi_dashboard/
├── dashboard/
│   ├── screenshots/
│   │   ├── executive_overview.png
│   │   ├── funnel_conversion.png
│   │   ├── regional_performance.png
│   │   └── target_vs_actual.png
│   └── Revenue_Operations_KPI_Dashboard.xlsx
├── data/
│   └── raw/
├── docs/
│   ├── insight_summary.md
│   └── kpi_definitions.md
├── sql/
│   └── analysis/
├── generate_data.py
├── load_to_sqlite.py
├── revenue_ops.db
└── README.md