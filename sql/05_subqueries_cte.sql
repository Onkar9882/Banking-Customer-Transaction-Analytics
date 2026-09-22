USE banking_analytics;


-- SUBQUERIES


-- 1. Customers with income above average

SELECT
    customer_id,
    name,
    occupation,
    income
FROM customers
WHERE income > (
    SELECT AVG(income)
    FROM customers
)
ORDER BY income DESC;


-- 2. Accounts with balance above average

SELECT
    account_id,
    customer_id,
    account_type,
    balance
FROM accounts
WHERE balance > (
    SELECT AVG(balance)
    FROM accounts
)
ORDER BY balance DESC;


-- 3. Customers with transaction amount above average

SELECT
    c.customer_id,
    c.name,
    ROUND(SUM(t.amount), 2) AS total_transaction_amount
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY c.customer_id, c.name
HAVING SUM(t.amount) > (
    SELECT AVG(customer_total)
    FROM (
        SELECT
            a2.customer_id,
            SUM(t2.amount) AS customer_total
        FROM accounts a2
        INNER JOIN transactions t2
            ON a2.account_id = t2.account_id
        GROUP BY a2.customer_id
    ) AS customer_totals
)
ORDER BY total_transaction_amount DESC;


-- CTE


-- 4. Customer transaction totals

WITH customer_transaction_totals AS (
    SELECT
        a.customer_id,
        SUM(t.amount) AS total_transaction_amount
    FROM accounts a
    INNER JOIN transactions t
        ON a.account_id = t.account_id
    GROUP BY a.customer_id
)
SELECT
    customer_id,
    ROUND(total_transaction_amount, 2) AS total_transaction_amount
FROM customer_transaction_totals
ORDER BY total_transaction_amount DESC;


-- 5. Customer transaction summary

WITH customer_transaction_totals AS (
    SELECT
        a.customer_id,
        COUNT(t.transaction_id) AS transaction_count,
        SUM(t.amount) AS total_transaction_amount,
        AVG(t.amount) AS average_transaction_amount
    FROM accounts a
    INNER JOIN transactions t
        ON a.account_id = t.account_id
    GROUP BY a.customer_id
)
SELECT
    c.customer_id,
    c.name,
    c.occupation,
    c.income,
    ctt.transaction_count,
    ROUND(ctt.total_transaction_amount, 2) AS total_transaction_amount,
    ROUND(ctt.average_transaction_amount, 2) AS average_transaction_amount
FROM customers c
INNER JOIN customer_transaction_totals ctt
    ON c.customer_id = ctt.customer_id
ORDER BY ctt.total_transaction_amount DESC;


-- 6. High-value customers

WITH customer_transaction_totals AS (
    SELECT
        a.customer_id,
        SUM(t.amount) AS total_transaction_amount
    FROM accounts a
    INNER JOIN transactions t
        ON a.account_id = t.account_id
    GROUP BY a.customer_id
)
SELECT
    c.customer_id,
    c.name,
    ROUND(ctt.total_transaction_amount, 2) AS total_transaction_amount
FROM customers c
INNER JOIN customer_transaction_totals ctt
    ON c.customer_id = ctt.customer_id
WHERE ctt.total_transaction_amount > 100000
ORDER BY total_transaction_amount DESC;


-- 7. Branch transaction summary

WITH branch_transaction_summary AS (
    SELECT
        a.branch_id,
        COUNT(t.transaction_id) AS transaction_count,
        SUM(t.amount) AS total_transaction_amount,
        AVG(t.amount) AS average_transaction_amount
    FROM accounts a
    INNER JOIN transactions t
        ON a.account_id = t.account_id
    GROUP BY a.branch_id
)
SELECT
    b.branch_id,
    b.branch_name,
    b.branch_type,
    b.city,
    ROUND(bts.total_transaction_amount, 2) AS total_transaction_amount,
    bts.transaction_count,
    ROUND(bts.average_transaction_amount, 2) AS average_transaction_amount
FROM branches b
INNER JOIN branch_transaction_summary bts
    ON b.branch_id = bts.branch_id
ORDER BY bts.total_transaction_amount DESC;


-- 8. Customer activity segmentation

WITH customer_activity AS (
    SELECT
        a.customer_id,
        COUNT(t.transaction_id) AS transaction_count
    FROM accounts a
    INNER JOIN transactions t
        ON a.account_id = t.account_id
    GROUP BY a.customer_id
)
SELECT
    customer_id,
    transaction_count,
    CASE
        WHEN transaction_count < 10 THEN 'Low Activity'
        WHEN transaction_count < 20 THEN 'Medium Activity'
        ELSE 'High Activity'
    END AS activity_segment
FROM customer_activity
ORDER BY transaction_count DESC;


-- 9. Final customer transaction analysis

WITH customer_transaction_summary AS (
    SELECT
        c.customer_id,
        c.name,
        c.state,
        c.occupation,
        COUNT(t.transaction_id) AS transaction_count,
        SUM(t.amount) AS total_transaction_amount,
        AVG(t.amount) AS average_transaction_amount
    FROM customers c
    INNER JOIN accounts a
        ON c.customer_id = a.customer_id
    INNER JOIN transactions t
        ON a.account_id = t.account_id
    GROUP BY
        c.customer_id,
        c.name,
        c.state,
        c.occupation
)
SELECT
    customer_id,
    name,
    state,
    occupation,
    transaction_count,
    ROUND(total_transaction_amount, 2) AS total_transaction_amount,
    ROUND(average_transaction_amount, 2) AS average_transaction_amount,
    CASE
        WHEN transaction_count < 10 THEN 'Low Activity'
        WHEN transaction_count < 20 THEN 'Medium Activity'
        ELSE 'High Activity'
    END AS activity_segment
FROM customer_transaction_summary
ORDER BY total_transaction_amount DESC;