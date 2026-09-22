CREATE DATABASE banking_analytics;

USE banking_analytics;


-- Customers Table

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    city VARCHAR(100),
    state VARCHAR(100),
    occupation VARCHAR(100),
    income DECIMAL(12,2),
    join_date DATE
);


-- Accounts Table

CREATE TABLE accounts (
    account_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    branch_id VARCHAR(20),
    account_type VARCHAR(50),
    opening_date DATE,
    balance DECIMAL(15,2),
    account_status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


-- Branches Table

CREATE TABLE branches (
    branch_id VARCHAR(20) PRIMARY KEY,
    branch_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    branch_type VARCHAR(50)
);


-- Transactions Table

CREATE TABLE transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    account_id VARCHAR(20),
    transaction_date DATE,
    transaction_type VARCHAR(20),
    category VARCHAR(50),
    amount DECIMAL(15,2),
    payment_mode VARCHAR(50),
    merchant_category VARCHAR(100),
    transaction_status VARCHAR(20),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);