# KPI Definitions

## 1. Total Revenue
Definition: Total net revenue generated from all customer orders.
Formula: SUM(net_revenue)
Business Use: Tracks overall business performance.

## 2. Lead-to-Customer Conversion Rate
Definition: Percentage of total leads that became customers.
Formula: total_customers / total_leads * 100
Business Use: Measures funnel efficiency.

## 3. Total Orders
Definition: Total number of orders placed.
Formula: COUNT(order_id)
Business Use: Tracks order volume.

## 4. Average Order Value
Definition: Average net revenue per order.
Formula: AVG(net_revenue)
Business Use: Measures revenue quality per transaction.

## 5. Revenue by Region
Definition: Total net revenue generated in each region.
Formula: SUM(net_revenue) grouped by region
Business Use: Identifies strongest and weakest markets.

## 6. Lead Funnel by Stage
Definition: Distribution of leads across funnel stages such as New, Qualified, Proposal, Won, and Lost.
Formula: COUNT(*) grouped by lead_stage
Business Use: Helps monitor pipeline health.

## 7. Monthly Revenue Trend
Definition: Total revenue generated each month.
Formula: SUM(net_revenue) grouped by month
Business Use: Tracks growth trends over time.

## 8. Revenue Target Variance
Definition: Difference between actual revenue and target revenue.
Formula: actual_revenue - revenue_target
Business Use: Measures performance against plan.
