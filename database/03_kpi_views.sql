-- KPI 1
CREATE VIEW vw_avg_delivery_by_region AS
SELECT w.region, ROUND(AVG(s.delivery_time),2) AS avg_delivery_days
FROM Shipment s
JOIN Orders o ON s.order_id = o.order_id
JOIN Warehouse w ON o.warehouse_id = w.warehouse_id
GROUP BY w.region;

-- KPI 2
CREATE VIEW vw_order_status_distribution AS
SELECT status, COUNT(*) AS total_orders
FROM Orders
GROUP BY status;

-- KPI 3 (Improved logic)
CREATE VIEW vw_on_time_delivery_rate AS
SELECT ROUND(
    SUM(CASE WHEN delivery_date <= DATEADD(day,3,order_date) THEN 1 ELSE 0 END) * 100.0
    / COUNT(*),2) AS on_time_delivery_percentage
FROM Orders;

-- KPI 4
CREATE VIEW vw_avg_cost_per_order AS
SELECT ROUND(AVG(cost),2) AS avg_cost_per_order
FROM Shipment;

-- KPI 5
CREATE VIEW vw_daily_cost_trend AS
SELECT date, SUM(total_cost) AS daily_total_cost
FROM CostMetrics
GROUP BY date;

-- KPI 6
CREATE VIEW vw_warehouse_cost_efficiency AS
SELECT warehouse_id, ROUND(AVG(total_cost),2) AS avg_cost
FROM CostMetrics
GROUP BY warehouse_id;

-- KPI 7
CREATE VIEW vw_delay_reason_analysis AS
SELECT delay_reason, COUNT(*) AS delay_count
FROM Shipment
WHERE delay_reason <> 'None'
GROUP BY delay_reason;

-- KPI 8
CREATE VIEW vw_orders_by_region AS
SELECT w.region, COUNT(*) AS total_orders
FROM Orders o
JOIN Warehouse w ON o.warehouse_id = w.warehouse_id
GROUP BY w.region;
