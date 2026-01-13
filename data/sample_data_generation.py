import random
import datetime
from python.db_connection import get_connection

# Connect to SQL Server

conn = get_connection()
cur = conn.cursor()


# 1. Insert Warehouses

regions = ['North', 'South', 'East', 'West']
managers = ['Amit', 'Bobby', 'Sneha', 'Ravi']

for region, manager in zip(regions, managers):
    cur.execute(
        """
        INSERT INTO Warehouse (region, capacity, manager)
        VALUES (?, ?, ?)
        """,
        region,
        random.randint(500, 1000),
        manager
    )


# 2. Insert Inventory

items = ['Laptop', 'Shoes', 'Mobile', 'Book', 'Keyboard']

for item in items:
    cur.execute(
        """
        INSERT INTO Inventory (item_name, stock_level, warehouse_id)
        VALUES (?, ?, ?)
        """,
        item,
        random.randint(50, 200),
        random.randint(1, 4)
    )


# 3. Insert Orders & Shipments

for _ in range(20):
    order_date = datetime.date(2025, 10, random.randint(1, 20))
    delivery_gap = random.randint(1, 7)
    delivery_date = order_date + datetime.timedelta(days=delivery_gap)

    if delivery_gap <= 3:
        status = 'Delivered'
    elif delivery_gap <= 5:
        status = 'Processing'
    else:
        status = 'Delayed'

    # Insert Order
    cur.execute(
        """
        INSERT INTO Orders (customer_id, warehouse_id, order_date, delivery_date, status)
        OUTPUT INSERTED.order_id
        VALUES (?, ?, ?, ?, ?)
        """,
        random.randint(1000, 2000),
        random.randint(1, 4),
        order_date,
        delivery_date,
        status
    )

    order_id = cur.fetchone()[0]

    delay_reason = random.choice(['Traffic', 'Weather']) if status == 'Delayed' else 'None'

    # Insert Shipment
    cur.execute(
        """
        INSERT INTO Shipment (order_id, cost, delay_reason, delivery_time)
        VALUES (?, ?, ?, ?)
        """,
        order_id,
        round(random.uniform(50, 500), 2),
        delay_reason,
        delivery_gap
    )


# 4. Insert Cost Metrics

for warehouse_id in range(1, 5):
    for day in range(1, 6):
        labor = round(random.uniform(100, 200), 2)
        transport = round(random.uniform(200, 500), 2)
        total = labor + transport

        cur.execute(
            """
            INSERT INTO CostMetrics
            (warehouse_id, date, labor_hours, transport_cost, total_cost)
            VALUES (?, ?, ?, ?, ?)
            """,
            warehouse_id,
            datetime.date(2025, 10, day),
            labor,
            transport,
            total
        )

conn.commit()
cur.close()
conn.close()

print("Sample data inserted successfully.")
