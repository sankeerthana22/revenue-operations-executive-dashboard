-- Dashboard export queries for Tableau

-- Executive KPIs
SELECT
    ROUND(SUM(net_revenue), 2) AS total_revenue,
    COUNT(order_id) AS total_orders,
    ROUND(AVG(net_revenue), 2) AS avg_order_value
FROM orders;

-- Conversion KPIs
SELECT
    (SELECT COUNT(*) FROM leads) AS total_leads,
    (SELECT COUNT(*) FROM customers) AS total_customers,
    ROUND(
        100.0 * (SELECT COUNT(*) FROM customers) / (SELECT COUNT(*) FROM leads),
        2
    ) AS lead_to_customer_conversion_pct;

-- Monthly revenue
SELECT
    DATE(order_date, 'start of month') AS revenue_month,
    ROUND(SUM(net_revenue), 2) AS monthly_revenue,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY DATE(order_date, 'start of month')
ORDER BY revenue_month;

-- Revenue by region
SELECT
    c.region,
    ROUND(SUM(o.net_revenue), 2) AS total_revenue,
    COUNT(o.order_id) AS total_orders,
    ROUND(AVG(o.net_revenue), 2) AS avg_order_value
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY c.region
ORDER BY total_revenue DESC;
