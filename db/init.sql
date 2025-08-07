-- Initialization script for Sparly database
-- Creates necessary extensions and tables

-- Enable PostGIS extension
CREATE EXTENSION IF NOT EXISTS postgis;

-- Include schema definitions from models.sql
\i models.sql
