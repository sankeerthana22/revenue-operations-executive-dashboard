-- Revenue Operations KPI checks

-- Total revenue
SELECT ROUND(SUM(net_revenue), 2) AS total_revenue
FROM orders;

-- Monthly revenue trend
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
