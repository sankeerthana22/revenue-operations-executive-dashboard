# Revenue Operations Executive Dashboard

An end-to-end analytics workflow using **Python, SQL, and Tableau** to analyze revenue KPIs, validate metrics, and present insights through an executive business dashboard.

## Analytics Pipeline

Python Data Generation
        ↓
SQLite Data Loading
        ↓
SQL KPI Analysis
        ↓
CSV Metrics
        ↓
Tableau Executive Dashboard

## Overview
This project presents a revenue operations analytics pipeline that combines Python, SQL, and Tableau to analyze business KPIs, validate revenue metrics, and deliver an executive-level dashboard for performance monitoring and decision-making.

## Business Questions Answered
- How much total revenue was generated?
- How many total orders were placed?
- What is the average order value?
- What is the lead-to-customer conversion rate?
- How has revenue changed over time?
- Which regions generate the most revenue?

## Key KPIs
- **Total Revenue:** $10.35M
- **Total Orders:** 2,200
- **Average Order Value:** $4,704
- **Lead-to-Customer Conversion Rate:** 28.93%

## Tools Used
- Python for data generation and pipeline support
- SQL for KPI analysis, validation, and dashboard exports
- Tableau for executive dashboard design and reporting
- Structured CSV datasets for analysis inputs
- Business KPI analysis for performance monitoring

## Data Pipeline
This project follows a simple analytics workflow:

1. `generate_data.py` creates structured revenue datasets
2. `load_to_sqlite.py` loads data into SQLite for query-based analysis
3. SQL queries validate KPIs and prepare dashboard-ready outputs
4. Tableau visualizes revenue performance in an executive dashboard

## Visualizations
- Monthly Revenue Trend
- Revenue by Region
- Executive KPI summary cards

## Key Insights
- Revenue reached **$10.35M** across **2,200 orders**.
- The business maintained a strong average order value of **$4,704**.
- Lead-to-customer conversion stood at **28.93%**.
- **North** was the top-performing region, followed by **South**.
- Monthly revenue showed variability across the year, with a major spike in the final period.

## Project Files
- `dashboard/revenue_operations_executive_dashboard.twbx` — Tableau dashboard workbook
- `images/dashboard_preview.png` — exported dashboard image
- `data/monthly_revenue_metrics.csv` — monthly revenue data
- `data/revenue_by_region_metrics.csv` — regional revenue data
- `data/executive_kpi_metrics.csv` — top-level KPI values
- `data/conversion_rate_metrics.csv` — conversion KPI values
- `sql/revenue_kpi_analysis.sql` — KPI validation and analysis queries
- `sql/dashboard_exports.sql` — export queries for dashboard-ready outputs
- `generate_data.py` — synthetic revenue dataset generator
- `load_to_sqlite.py` — SQLite loading script

## Purpose
This project demonstrates the ability to build a small end-to-end analytics workflow using Python, SQL, and Tableau to support executive revenue reporting and business insight generation.

## Executive Dashboard
The Tableau dashboard provides a concise executive view of revenue performance, order volume, conversion efficiency, and regional contribution.

![Dashboard Preview](images/dashboard_preview.png)

## Business Recommendations
- Review the final-period revenue spike to identify repeatable growth drivers.
- Compare top-performing regional strategies and apply them to lower-performing regions.
- Improve funnel efficiency to increase the lead-to-customer conversion rate.
- Use monthly revenue trends to support forecasting and performance planning.

## How to Open the Dashboard
Open the file `dashboard/revenue_operations_executive_dashboard.twbx` in Tableau Desktop.

## Project Workflow
Python Data Generation → SQLite Loading → SQL KPI Validation → Tableau Dashboard Design → Executive Reporting
