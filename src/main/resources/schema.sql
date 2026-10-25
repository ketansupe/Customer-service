CREATE TABLE IF NOT EXISTS customers (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(50),
    address TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (first_name, last_name, email, phone, address, created_at, updated_at)
SELECT 'John', 'Doe', 'john.doe@example.com', '555-0101', '123 Main St', NOW(), NOW()
WHERE NOT EXISTS (SELECT 1 FROM customers WHERE email = 'john.doe@example.com');

INSERT INTO customers (first_name, last_name, email, phone, address, created_at, updated_at)
SELECT 'Jane', 'Smith', 'jane.smith@example.com', '555-0102', '456 Oak Ave', NOW(), NOW()
WHERE NOT EXISTS (SELECT 1 FROM customers WHERE email = 'jane.smith@example.com');

INSERT INTO customers (first_name, last_name, email, phone, address, created_at, updated_at)
SELECT 'Robert', 'Brown', 'robert.brown@example.com', '555-0103', '789 Pine Rd', NOW(), NOW()
WHERE NOT EXISTS (SELECT 1 FROM customers WHERE email = 'robert.brown@example.com');
