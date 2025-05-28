# Superset on Render

# 📊 US Maritime Import Dashboard — Superset + Supabase

A lightweight data visualization project for U.S. import shipment data using:

- **Supabase** → Cloud PostgreSQL backend (free tier)
- **Apache Superset** → Web-based BI dashboards (hosted on Render)
- **Render** → Hosts Superset, directly connected to this GitHub repo (free tier)

Superset reads from Supabase via SQLAlchemy URI

Dashboards created and shared via Superset UI

## 🧱 Architecture

🚀 Render Deployment (No Docker)
Superset is deployed on Render.com as a Python Web Service

This GitHub repo is connected directly to Render

On push, Render automatically:

Installs from requirements.txt

Runs your build.sh and start.sh scripts

🛠️ Environment

Python ≥ 3.8 on Render

PostgreSQL connection via SQLAlchemy URI from Supabase

GitHub repo used as single source of truth
