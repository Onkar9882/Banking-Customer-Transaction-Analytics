USE banking_analytics;


-- 1. Total transactions

SELECT
    COUNT(*) AS total_transactions
FROM transactions;


-- 2. Total transaction amount

SELECT
    ROUND(SUM(amount), 2) AS total_transaction_amount
FROM transactions;


-- 3. Transaction KPIs

SELECT
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_transaction_amount,
    ROUND(AVG(amount), 2) AS average_transaction_amount,
    ROUND(MIN(amount), 2) AS minimum_transaction_amount,
    ROUND(MAX(amount), 2) AS maximum_transaction_amount
FROM transactions;


-- 4. Transaction type analysis

SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount,
    ROUND(AVG(amount), 2) AS average_amount
FROM transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;


-- 5. Category analysis

SELECT
    category,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount,
    ROUND(AVG(amount), 2) AS average_amount
FROM transactions
GROUP BY category
ORDER BY total_amount DESC;


-- 6. Payment mode analysis

SELECT
    payment_mode,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount,
    ROUND(AVG(amount), 2) AS average_amount
FROM transactions
GROUP BY payment_mode
ORDER BY transaction_count DESC;


-- 7. Transaction status

SELECT
    transaction_status,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY transaction_status
ORDER BY transaction_count DESC;


-- 8. Transaction status percentage

SELECT
    transaction_status,
    COUNT(*) AS transaction_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM transactions),
        2
    ) AS percentage
FROM transactions
GROUP BY transaction_status
ORDER BY transaction_count DESC;


-- 9. Overall success rate

SELECT
    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'Success' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS success_rate
FROM transactions;


-- 10. Payment mode success rate

SELECT
    payment_mode,
    COUNT(*) AS total_transactions,
    SUM(
        CASE
            WHEN transaction_status = 'Success' THEN 1
            ELSE 0
        END
    ) AS successful_transactions,
    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'Success' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS success_rate
FROM transactions
GROUP BY payment_mode
ORDER BY success_rate DESC;


-- 11. Category and transaction status

SELECT
    category,
    transaction_status,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY category, transaction_status
ORDER BY category, transaction_count DESC;


-- 12. High-value transactions

SELECT
    transaction_id,
    account_id,
    transaction_date,
    transaction_type,
    category,
    amount,
    payment_mode,
    transaction_status
FROM transactions
WHERE amount > 50000
ORDER BY amount DESC;


-- 13. Top 10 transactions

SELECT
    transaction_id,
    account_id,
    transaction_date,
    category,
    amount,
    payment_mode,
    transaction_status
FROM transactions
ORDER BY amount DESC
LIMIT 10;


-- 14. Transaction analysis by account type

SELECT
    a.account_type,
    COUNT(t.transaction_id) AS transaction_count,
    ROUND(SUM(t.amount), 2) AS total_transaction_amount,
    ROUND(AVG(t.amount), 2) AS average_transaction_amount
FROM accounts a
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY a.account_type
ORDER BY total_transaction_amount DESC;


-- 15. Final transaction KPI

SELECT
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_transaction_amount,
    ROUND(AVG(amount), 2) AS average_transaction_amount,
    ROUND(MIN(amount), 2) AS minimum_transaction_amount,
    ROUND(MAX(amount), 2) AS maximum_transaction_amount,
    SUM(
        CASE
            WHEN transaction_status = 'Success'
            THEN 1 ELSE 0
        END
    ) AS successful_transactions,
    SUM(
        CASE
            WHEN transaction_status = 'Failed'
            THEN 1 ELSE 0
        END
    ) AS failed_transactions,
    SUM(
        CASE
            WHEN transaction_status = 'Pending'
            THEN 1 ELSE 0
        END
    ) AS pending_transactions
FROM transactions;