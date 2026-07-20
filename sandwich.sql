CREATE DATABASE IF NOT EXISTS sandwich_maker;
USE sandwich_maker;

-- Recreate the tables so the script can be run more than once.
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS sandwiches;
DROP TABLE IF EXISTS resources;

CREATE TABLE resources (
    item VARCHAR(50),
    amount INT
);

CREATE TABLE sandwiches (
    sandwich_size VARCHAR(50),
    price DECIMAL(5, 2)
);

CREATE TABLE recipes (
    sandwich_size VARCHAR(50),
    item VARCHAR(50),
    amount INT
);

INSERT INTO resources (item, amount) VALUES
    ('bread', 12),
    ('ham', 18),
    ('cheese', 24);

INSERT INTO sandwiches (sandwich_size, price) VALUES
    ('small', 1.75),
    ('medium', 3.25),
    ('large', 5.50);

INSERT INTO recipes (sandwich_size, item, amount) VALUES
    ('small', 'bread', 2),
    ('small', 'ham', 4),
    ('small', 'cheese', 4),
    ('medium', 'bread', 4),
    ('medium', 'ham', 6),
    ('medium', 'cheese', 8),
    ('large', 'bread', 6),
    ('large', 'ham', 8),
    ('large', 'cheese', 12);

-- Run each SELECT separately in MySQL Workbench and capture its result grid.
SELECT * FROM resources;
SELECT * FROM sandwiches;
SELECT * FROM recipes;