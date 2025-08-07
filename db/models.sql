-- Database schema for Sparly
-- This file defines tables for stores, discounts, and users.

-- Enable PostGIS extension
CREATE EXTENSION IF NOT EXISTS postgis;

-- Table: stores
CREATE TABLE IF NOT EXISTS stores (
    id SERIAL PRIMARY KEY,
    chain VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    lat DOUBLE PRECISION NOT NULL,
    lon DOUBLE PRECISION NOT NULL,
    geom GEOMETRY(Point, 4326) NOT NULL,
    address TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Table: discounts
CREATE TABLE IF NOT EXISTS discounts (
    id SERIAL PRIMARY KEY,
    store_id INTEGER REFERENCES stores(id) ON DELETE CASCADE,
    product_name TEXT NOT NULL,
    price NUMERIC(8, 2) NOT NULL,
    price_old NUMERIC(8, 2),
    valid_until DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Table: users
CREATE TABLE IF NOT EXISTS users (
    id BIGINT PRIMARY KEY, -- Telegram user ID
    lang VARCHAR(2) DEFAULT 'uk',
    radius DOUBLE PRECISION DEFAULT 6.0,
    location GEOMETRY(Point, 4326),
    categories TEXT[],
    trial_start TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
