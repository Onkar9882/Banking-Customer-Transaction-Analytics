USE banking_analytics;


-- 1. Customer and account analysis

SELECT
    c.customer_id,
    c.name,
    c.city,
    c.state,
    a.account_id,
    a.account_type,
    a.balance,
    a.account_status
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id;


-- 2. Customer + account + transaction

SELECT
    c.customer_id,
    c.name,
    a.account_id,
    a.account_type,
    t.transaction_id,
    t.transaction_date,
    t.transaction_type,
    t.category,
    t.amount,
    t.payment_mode,
    t.transaction_status
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id;


-- 3. Customer-wise transaction summary

SELECT
    c.customer_id,
    c.name,
    COUNT(t.transaction_id) AS transaction_count,
    ROUND(SUM(t.amount), 2) AS total_transaction_amount,
    ROUND(AVG(t.amount), 2) AS average_transaction_amount
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY c.customer_id, c.name
ORDER BY total_transaction_amount DESC;


-- 4. Branch performance

SELECT
    b.branch_id,
    b.branch_name,
    b.city,
    b.state,
    b.branch_type,
    COUNT(t.transaction_id) AS transaction_count,
    ROUND(SUM(t.amount), 2) AS total_transaction_amount,
    ROUND(AVG(t.amount), 2) AS average_transaction_amount
FROM branches b
INNER JOIN accounts a
    ON b.branch_id = a.branch_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY
    b.branch_id,
    b.branch_name,
    b.city,
    b.state,
    b.branch_type
ORDER BY total_transaction_amount DESC;


-- 5. Branch type performance

SELECT
    b.branch_type,
    COUNT(DISTINCT b.branch_id) AS branch_count,
    COUNT(DISTINCT a.customer_id) AS customer_count,
    COUNT(t.transaction_id) AS transaction_count,
    ROUND(SUM(t.amount), 2) AS total_transaction_amount,
    ROUND(AVG(t.amount), 2) AS average_transaction_amount
FROM branches b
INNER JOIN accounts a
    ON b.branch_id = a.branch_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY b.branch_type
ORDER BY total_transaction_amount DESC;


-- 6. State-wise performance

SELECT
    c.state,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    COUNT(DISTINCT a.account_id) AS account_count,
    COUNT(t.transaction_id) AS transaction_count,
    ROUND(SUM(t.amount), 2) AS total_transaction_amount
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY c.state
ORDER BY total_transaction_amount DESC;


-- 7. Account type transaction analysis

SELECT
    a.account_type,
    COUNT(DISTINCT a.customer_id) AS customer_count,
    COUNT(DISTINCT a.account_id) AS account_count,
    COUNT(t.transaction_id) AS transaction_count,
    ROUND(SUM(t.amount), 2) AS total_transaction_amount,
    ROUND(AVG(t.amount), 2) AS average_transaction_amount
FROM accounts a
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY a.account_type
ORDER BY total_transaction_amount DESC;


-- 8. Payment mode and customer analysis

SELECT
    t.payment_mode,
    COUNT(DISTINCT a.customer_id) AS customer_count,
    COUNT(t.transaction_id) AS transaction_count,
    ROUND(SUM(t.amount), 2) AS total_transaction_amount,
    ROUND(AVG(t.amount), 2) AS average_transaction_amount
FROM accounts a
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY t.payment_mode
ORDER BY transaction_count DESC;


-- 9. Successful transaction value by branch

SELECT
    b.branch_id,
    b.branch_name,
    COUNT(t.transaction_id) AS successful_transactions,
    ROUND(SUM(t.amount), 2) AS successful_transaction_amount
FROM branches b
INNER JOIN accounts a
    ON b.branch_id = a.branch_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_status = 'Success'
GROUP BY b.branch_id, b.branch_name
ORDER BY successful_transaction_amount DESC;


-- 10. Customers with no transactions

SELECT
    c.customer_id,
    c.name,
    a.account_id,
    a.account_type
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
LEFT JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;