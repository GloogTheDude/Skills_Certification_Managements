#!/usr/bin/env bash
set -e

DB_NAME="module_certificator"
DB_OWNER="glg"

echo "Drop database..."
sudo -u postgres dropdb --if-exists "$DB_NAME"

echo "Create database..."
sudo -u postgres createdb -O "$DB_OWNER" "$DB_NAME"

echo "Run Alembic migrations..."
alembic upgrade head

echo "Load seed data..."
psql -d "$DB_NAME" -f db/sql/seed.sql

echo "Database reset complete."
