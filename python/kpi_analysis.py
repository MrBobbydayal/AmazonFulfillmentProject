import pandas as pd, numpy as np
from python.db_connection import get_connection

conn = get_connection()

delivery = pd.read_sql("SELECT * FROM vw_avg_delivery_by_region", conn)
print("Delivery variance:", np.var(delivery.avg_delivery_days))

cost = pd.read_sql("SELECT * FROM vw_daily_cost_trend", conn)
print("Average daily cost:", np.mean(cost.daily_total_cost))

conn.close()
