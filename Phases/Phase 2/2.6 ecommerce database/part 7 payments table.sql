USE ecommerce_db;

CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL UNIQUE,
    payment_method VARCHAR(30) NOT NULL,
    payment_status VARCHAR(30) NOT NULL DEFAULT 'Pending',
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CHECK (payment_method IN (
        'Cash',
        'Card',
        'Bank Transfer',
        'Online'
    )),

    CHECK (payment_status IN (
        'Pending',
        'Paid',
        'Failed',
        'Refunded'
    ))
);