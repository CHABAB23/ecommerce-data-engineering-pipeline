-- Total orders
SELECT
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_sales
FROM orders;


-- Sales by product
SELECT
    p.product_name,
    SUM(o.quantity) AS units_sold,
    SUM(o.total_amount) AS revenue
FROM orders o
JOIN products p
    ON p.product_id = o.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY
    revenue DESC;


-- Sales by customer
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS orders_count,
    SUM(o.total_amount) AS total_spent
FROM customers c
LEFT JOIN orders o
    ON o.customer_id = c.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY
    total_spent DESC NULLS LAST;


-- Sales by country
SELECT
    c.country,
    COUNT(o.order_id) AS orders_count,
    SUM(o.total_amount) AS revenue
FROM customers c
JOIN orders o
    ON o.customer_id = c.customer_id
GROUP BY
    c.country
ORDER BY
    revenue DESC;