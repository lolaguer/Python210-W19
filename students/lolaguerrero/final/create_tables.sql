-- Desc: Python 210 Final - Create tables and insert some values
-- ChangeLog: (When,Who,What)
-- 03/07/19, Lola Guerrero,Created Script

-- Create tables --

CREATE TABLE Inventories (
InventoryID INT NOT NULL CONSTRAINT pkInventories PRIMARY KEY,
InventoryDate DATETIME NOT NULL);   -- DATETIME or TEXT??


CREATE TABLE Products (
ProductID INT NOT NULL CONSTRAINT pkProducts PRIMARY KEY,
ProductName NVARCHAR (100) NOT NULL); 


CREATE TABLE InventoryCounts (
InventoryID INT NOT NULL,
ProductID INT NOT NULL,
Count INT NOT NULL,
PRIMARY KEY (InventoryID, ProductID));


-- Insert values in the tables --

INSERT INTO Inventories (InventoryID, InventoryDate) VALUES (1,'2019-01-01');
INSERT INTO Inventories (InventoryID, InventoryDate) VALUES (2,'2019-02-01');

INSERT INTO Products (ProductID, ProductName) VALUES (100,'ProdA');
INSERT INTO Products (ProductID, ProductName) VALUES (200,'ProdB');

INSERT INTO InventoryCounts (InventoryID, ProductID, Count) VALUES (1,100,15);
INSERT INTO InventoryCounts (InventoryID, ProductID, Count) VALUES (1,200,33);
INSERT INTO InventoryCounts (InventoryID, ProductID, Count) VALUES (2,100,12);
INSERT INTO InventoryCounts (InventoryID, ProductID, Count) VALUES (2,200,45);
