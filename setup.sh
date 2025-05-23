#!/bin/bash
set -e

# Initialize the database
superset db upgrade

# Create admin user if not exists
superset fab create-admin \
  --username russdevv \
  --firstname Russ \
  --lastname Devv \
  --email russ.devv@outlook.com \
  --password Admin123 || true

# Setup roles and permissions
superset init
