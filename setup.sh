#!/bin/bash

# Step 1: Install Python dependencies
pip install -r requirements.txt

# Step 2: Upgrade the Superset database
superset db upgrade

# Step 3: Create admin user (only if it doesn't exist)
superset fab create-admin \
  --username admin \
  --firstname Superset \
  --lastname Admin \
  --email admin@superset.com \
  --password admin

# Step 4: Initialize Superset
superset init
