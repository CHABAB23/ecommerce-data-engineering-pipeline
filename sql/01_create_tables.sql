CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    country VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(100),
    price NUMERIC(10,2),
    stock_quantity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount NUMERIC(10,2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);