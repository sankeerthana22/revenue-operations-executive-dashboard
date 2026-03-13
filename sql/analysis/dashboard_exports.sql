-- 1) Monthly revenue trend
SELECT 
    DATE(order_date, 'start of month') AS revenue_month,
    ROUND(SUM(net_revenue), 2) AS monthly_revenue,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY DATE(order_date, 'start of month')
ORDER BY revenue_month;

-- 2) Lead funnel by stage
SELECT
    lead_stage,
    COUNT(*) AS total_leads,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM leads), 2) AS pct_of_total_leads
FROM leads
GROUP BY lead_stage
ORDER BY total_leads DESC;

-- 3) Revenue by region
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

-- 4) Monthly target vs actual by region
SELECT
    DATE(o.order_date, 'start of month') AS revenue_month,
    c.region,
    ROUND(SUM(o.net_revenue), 2) AS actual_revenue,
    t.revenue_target,
    ROUND(SUM(o.net_revenue) - t.revenue_target, 2) AS variance_to_target
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN targets t
    ON t.target_month = DATE(o.order_date, 'start of month')
   AND t.region = c.region
GROUP BY DATE(o.order_date, 'start of month'), c.region, t.revenue_target
ORDER BY revenue_month, c.region;
