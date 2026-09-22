USE banking_analytics;


-- 1. Rank transactions by amount

SELECT
    transaction_id,
    account_id,
    category,
    amount,
    ROW_NUMBER() OVER (
        ORDER BY amount DESC
    ) AS transaction_rank
FROM transactions;


-- 2. Top 10 transactions using ROW_NUMBER

WITH ranked_transactions AS (
    SELECT
        transaction_id,
        account_id,
        category,
        amount,
        ROW_NUMBER() OVER (
            ORDER BY amount DESC
        ) AS transaction_rank
    FROM transactions
)
SELECT
    transaction_id,
    account_id,
    category,
    amount,
    transaction_rank
FROM ranked_transactions
WHERE transaction_rank <= 10;


-- 3. RANK function

SELECT
    transaction_id,
    category,
    amount,
    RANK() OVER (
        ORDER BY amount DESC
    ) AS amount_rank
FROM transactions;


-- 4. DENSE_RANK function

SELECT
    transaction_id,
    category,
    amount,
    DENSE_RANK() OVER (
        ORDER BY amount DESC
    ) AS amount_rank
FROM transactions;


-- 5. Customer-wise transaction ranking

SELECT
    a.customer_id,
    t.transaction_id,
    t.category,
    t.amount,
    RANK() OVER (
        PARTITION BY a.customer_id
        ORDER BY t.amount DESC
    ) AS customer_transaction_rank
FROM accounts a
INNER JOIN transactions t
    ON a.account_id = t.account_id;


-- 6. Highest transaction for each customer

WITH ranked_transactions AS (
    SELECT
        a.customer_id,
        t.transaction_id,
        t.category,
        t.amount,
        RANK() OVER (
            PARTITION BY a.customer_id
            ORDER BY t.amount DESC
        ) AS transaction_rank
    FROM accounts a
    INNER JOIN transactions t
        ON a.account_id = t.account_id
)
SELECT
    customer_id,
    transaction_id,
    category,
    amount
FROM ranked_transactions
WHERE transaction_rank = 1;


-- 7. Transaction count per customer

SELECT
    a.customer_id,
    t.transaction_id,
    t.amount,
    COUNT(t.transaction_id) OVER (
        PARTITION BY a.customer_id
    ) AS customer_transaction_count
FROM accounts a
INNER JOIN transactions t
    ON a.account_id = t.account_id;


-- 8. Customer total transaction amount

SELECT
    a.customer_id,
    t.transaction_id,
    t.amount,
    SUM(t.amount) OVER (
        PARTITION BY a.customer_id
    ) AS customer_total_amount
FROM accounts a
INNER JOIN transactions t
    ON a.account_id = t.account_id;


-- 9. Running total

SELECT
    transaction_date,
    transaction_id,
    amount,
    SUM(amount) OVER (
        ORDER BY transaction_date, transaction_id
    ) AS running_total
FROM transactions
ORDER BY transaction_date, transaction_id;


-- 10. Customer running total

SELECT
    a.customer_id,
    t.transaction_date,
    t.transaction_id,
    t.amount,
    SUM(t.amount) OVER (
        PARTITION BY a.customer_id
        ORDER BY t.transaction_date, t.transaction_id
    ) AS customer_running_total
FROM accounts a
INNER JOIN transactions t
    ON a.account_id = t.account_id
ORDER BY
    a.customer_id,
    t.transaction_date;


-- 11. Previous transaction using LAG

SELECT
    a.customer_id,
    t.transaction_date,
    t.transaction_id,
    t.amount,
    LAG(t.amount) OVER (
        PARTITION BY a.customer_id
        ORDER BY t.transaction_date, t.transaction_id
    ) AS previous_transaction_amount
FROM accounts a
INNER JOIN transactions t
    ON a.account_id = t.account_id;


-- 12. Transaction amount difference

WITH transaction_comparison AS (
    SELECT
        a.customer_id,
        t.transaction_date,
        t.transaction_id,
        t.amount,
        LAG(t.amount) OVER (
            PARTITION BY a.customer_id
            ORDER BY t.transaction_date, t.transaction_id
        ) AS previous_amount
    FROM accounts a
    INNER JOIN transactions t
        ON a.account_id = t.account_id
)
SELECT
    customer_id,
    transaction_date,
    transaction_id,
    amount,
    previous_amount,
    ROUND(amount - previous_amount, 2) AS amount_difference
FROM transaction_comparison;


-- 13. Top 3 transactions per customer

WITH ranked_transactions AS (
    SELECT
        a.customer_id,
        t.transaction_id,
        t.category,
        t.amount,
        ROW_NUMBER() OVER (
            PARTITION BY a.customer_id
            ORDER BY t.amount DESC
        ) AS transaction_rank
    FROM accounts a
    INNER JOIN transactions t
        ON a.account_id = t.account_id
)
SELECT
    customer_id,
    transaction_id,
    category,
    amount,
    transaction_rank
FROM ranked_transactions
WHERE transaction_rank <= 3
ORDER BY customer_id, transaction_rank;


-- 14. Customer ranking by total transaction amount

WITH customer_totals AS (
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
    ROUND(total_transaction_amount, 2) AS total_transaction_amount,
    DENSE_RANK() OVER (
        ORDER BY total_transaction_amount DESC
    ) AS customer_rank
FROM customer_totals
ORDER BY customer_rank;


-- 15. Branch ranking by transaction amount

WITH branch_totals AS (
    SELECT
        a.branch_id,
        SUM(t.amount) AS total_transaction_amount
    FROM accounts a
    INNER JOIN transactions t
        ON a.account_id = t.account_id
    GROUP BY a.branch_id
)
SELECT
    b.branch_id,
    b.branch_name,
    b.branch_type,
    ROUND(bt.total_transaction_amount, 2) AS total_transaction_amount,
    DENSE_RANK() OVER (
        ORDER BY bt.total_transaction_amount DESC
    ) AS branch_rank
FROM branch_totals bt
INNER JOIN branches b
    ON bt.branch_id = b.branch_id
ORDER BY branch_rank;