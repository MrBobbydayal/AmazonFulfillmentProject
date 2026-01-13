import pandas as pd
import numpy as np
from python.db_connection import get_connection

print("Starting data validation...\n")

conn = get_connection()


# 1. Row Count Validation

tables = ['Warehouse', 'Inventory', 'Orders', 'Shipment', 'CostMetrics']

for table in tables:
    df = pd.read_sql(f"SELECT COUNT(*) AS count FROM {table}", conn)
    print(f"{table} row count:", df.loc[0, 'count'])


# 2. NULL Value Validation

null_check_orders = pd.read_sql(
    """
    SELECT
        SUM(CASE WHEN status IS NULL THEN 1 ELSE 0 END) AS status_nulls,
        SUM(CASE WHEN order_date IS NULL THEN 1 ELSE 0 END) AS order_date_nulls
    FROM Orders
    """,
    conn
)

print("\nOrders NULL check:")
print(null_check_orders)

null_check_shipment = pd.read_sql(
    """
    SELECT
        SUM(CASE WHEN cost IS NULL THEN 1 ELSE 0 END) AS cost_nulls,
        SUM(CASE WHEN delivery_time IS NULL THEN 1 ELSE 0 END) AS delivery_time_nulls
    FROM Shipment
    """,
    conn
)

print("\nShipment NULL check:")
print(null_check_shipment)


# 3. Range & Logic Validation

df_delivery = pd.read_sql(
    "SELECT delivery_time FROM Shipment",
    conn
)

invalid_delivery = df_delivery[df_delivery['delivery_time'] <= 0]
print("\nInvalid delivery_time records:", len(invalid_delivery))


# 4. KPI Sanity Check

df_kpi = pd.read_sql(
    "SELECT on_time_delivery_percentage FROM vw_on_time_delivery_rate",
    conn
)

kpi_value = df_kpi.loc[0, 'on_time_delivery_percentage']

if kpi_value < 0 or kpi_value > 100:
    print("ERROR: On-time delivery KPI out of range!")
else:
    print("On-time delivery KPI is valid:", kpi_value, "%")


# 5. Cost Outlier Detection

df_cost = pd.read_sql(
    "SELECT total_cost FROM CostMetrics",
    conn
)

mean_cost = np.mean(df_cost['total_cost'])
std_cost = np.std(df_cost['total_cost'])

outliers = df_cost[
    (df_cost['total_cost'] > mean_cost + 3 * std_cost) |
    (df_cost['total_cost'] < mean_cost - 3 * std_cost)
]

print("\nCost outliers detected:", len(outliers))


# 6. Validation Summary

print("\nData validation completed successfully.")

conn.close()
