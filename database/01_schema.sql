SELECT TOP 5
    o.order_id,
    w.region,
    s.delivery_time,
    s.cost
FROM Orders o
JOIN Warehouse w ON o.warehouse_id = w.warehouse_id
JOIN Shipment s ON o.order_id = s.order_id;
