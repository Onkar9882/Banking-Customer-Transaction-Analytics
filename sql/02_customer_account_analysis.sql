USE banking_analytics;


-- 1. Customer distribution by gender

SELECT
    gender,
    COUNT(*) AS customer_count
FROM customers
GROUP BY gender
ORDER BY customer_count DESC;


-- 2. Customer distribution by occupation

SELECT
    occupation,
    COUNT(*) AS customer_count
FROM customers
GROUP BY occupation
ORDER BY customer_count DESC;


-- 3. Customer distribution by state

SELECT
    state,
    COUNT(*) AS customer_count
FROM customers
GROUP BY state
ORDER BY customer_count DESC;


-- 4. Account type analysis

SELECT
    account_type,
    COUNT(*) AS account_count
FROM accounts
GROUP BY account_type
ORDER BY account_count DESC;


-- 5. Unique customers by account type

SELECT
    account_type,
    COUNT(DISTINCT customer_id) AS customer_count
FROM accounts
GROUP BY account_type
ORDER BY customer_count DESC;


-- 6. Average balance by account type

SELECT
    account_type,
    ROUND(AVG(balance), 2) AS average_balance
FROM accounts
GROUP BY account_type
ORDER BY average_balance DESC;


-- 7. Total balance by account type

SELECT
    account_type,
    ROUND(SUM(balance), 2) AS total_balance
FROM accounts
GROUP BY account_type
ORDER BY total_balance DESC;


-- 8. Active and inactive accounts

SELECT
    account_status,
    COUNT(*) AS account_count
FROM accounts
GROUP BY account_status
ORDER BY account_count DESC;


-- 9. Account type and status analysis

SELECT
    account_type,
    account_status,
    COUNT(*) AS account_count
FROM accounts
GROUP BY account_type, account_status
ORDER BY account_type, account_count DESC;


-- 10. Customer and account details

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


-- 11. State-wise customer and balance analysis

SELECT
    c.state,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    ROUND(SUM(a.balance), 2) AS total_balance
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
GROUP BY c.state
ORDER BY total_balance DESC;


-- 12. Final account type summary

SELECT
    a.account_type,
    COUNT(DISTINCT a.customer_id) AS customer_count,
    COUNT(a.account_id) AS account_count,
    ROUND(SUM(a.balance), 2) AS total_balance,
    ROUND(AVG(a.balance), 2) AS average_balance
FROM accounts a
GROUP BY a.account_type
ORDER BY total_balance DESC;