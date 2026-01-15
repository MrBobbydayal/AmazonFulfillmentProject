CREATE DATABASE amazon_fulfillment;
GO 
USE amazon_fulfillment; 
GO 

-- Warehouse 
CREATE TABLE Warehouse ( warehouse_id INT IDENTITY PRIMARY KEY,
                         region VARCHAR(50) NOT NULL,
                          capacity INT NOT NULL, 
                          manager VARCHAR(50) NOT NULL );
                          
 -- Inventory 
 CREATE TABLE Inventory ( inventory_id INT IDENTITY PRIMARY KEY, 
                         item_name VARCHAR(50) NOT NULL,
                          stock_level INT NOT NULL,
                           warehouse_id INT NOT NULL,
                            FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id) );
                            
                            
 -- Orders 
 CREATE TABLE Orders ( order_id INT IDENTITY PRIMARY KEY, 
                       customer_id INT NOT NULL,
                        warehouse_id INT NOT NULL,
                         order_date DATE NOT NULL,
                          delivery_date DATE NOT NULL,
                           status VARCHAR(20) NOT NULL,
                            FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id) ); 
                            
                            
-- Shipment 
CREATE TABLE Shipment ( shipment_id INT IDENTITY PRIMARY KEY,
                        order_id INT NOT NULL,
                         cost FLOAT NOT NULL,
                          delay_reason VARCHAR(50) DEFAULT 'None',
                           delivery_time INT NOT NULL,
                            FOREIGN KEY (order_id) REFERENCES Orders(order_id) ); 
                            
-- Cost Metrics 
CREATE TABLE CostMetrics ( cost_id INT IDENTITY PRIMARY KEY,
                           warehouse_id INT NOT NULL,
                            date DATE NOT NULL,
                             labor_hours FLOAT NOT NULL, 
                             transport_cost FLOAT NOT NULL,
                              total_cost FLOAT NOT NULL,
                               FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id) );