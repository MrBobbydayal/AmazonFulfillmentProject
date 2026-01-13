# Amazon Fulfillment Analytics Dashboard

## 📌 Project Overview
This project analyzes Amazon-style fulfillment operations using **SQL Server, Python, and Power BI**.  
The goal is to monitor **delivery performance, cost efficiency, and operational bottlenecks** through well-defined KPIs and an interactive dashboard.

The project follows an **end-to-end analytics workflow**:
- Database design & KPI views (SQL)
- Data generation & validation (Python)
- Business visualization & insights (Power BI)

---

## 🛠 Tech Stack
- **Database:** Microsoft SQL Server
- **Programming:** Python (pandas, numpy, pyodbc)
- **Visualization:** Power BI
- **Version Control:** Git & GitHub

---

## 📊 Key KPIs
- On-Time Delivery Percentage
- Orders by Region
- Order Status Distribution
- Daily Cost Trend
- Average Delivery Time by Region
- Delay Reason Analysis
- Average Cost per Warehouse
- Average Cost per Order

---

## 📁 Project Structure


Amazon_Fulfillment_Project/
│
├── data/
│ └── sample_data_generation.py
│
├── database/
│ ├── 01_schema.sql
│ ├── 02_sample_data_insert.sql
│ └── 03_kpi_views.sql
│
├── python/
│ ├── db_connection.py
│ ├── data_validation.py
│ └── kpi_analysis.py
│
├── powerbi/
│ └── Amazon_Fulfillment_Dashboard.pbix
│
├── docs/
│ ├── project_overview.md
│ ├── kpi_definitions.md
│ └── dashboard_explanation.md
│
└── README.md




---

## 🚀 How to Run
1. Execute SQL scripts in order:
   - `01_schema.sql`
   - `02_sample_data_insert.sql`
   - `03_kpi_views.sql`

2. Activate virtual environment and run:
   ```bash
   python -m data.sample_data_generation
   python -m python.data_validation


3. Open Power BI file and connect to SQL Server:
     Server: localhost\SQLEXPRESS(can be changed)
     Database: amazon_fulfillment(can be changed)
