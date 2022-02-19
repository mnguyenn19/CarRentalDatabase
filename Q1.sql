ALTER TABLE RENTAL
ADD COLUMN Returned INTEGER;

UPDATE RENTAL
SET Returned = 0
WHERE PaymentDate IS NULL;

UPDATE RENTAL
SET Returned = 1
WHERE PaymentDate IS NOT NULL;


CREATE VIEW vRentalInfo
AS
SELECT OrderDate AS orderDate, StartDate AS startDate, ReturnDate AS returnDate, RentalType * Qty AS TotalDays,
R.VehicleID AS VIN, V.VehicleDescription AS Vehicle,

CASE
    WHEN V.VehicleType = 1 THEN 'Compact'    --type
    WHEN V.VehicleType = 2 THEN 'Medium'    --type
    WHEN V.VehicleType = 3 THEN 'Large'    --type
    WHEN V.VehicleType = 4 THEN 'SUV'    --type
    WHEN V.VehicleType = 5 THEN 'Truck'    --type
    WHEN V.VehicleType = 6 THEN 'Van'    --type
    --WHEN V.Category = 0 THEN 'Basic'    --category
    --WHEN V.Category = 1 THEN 'Luxury'    --category
END AS 'Type',
CASE
    WHEN V.Category = 0 THEN 'Basic'    --category
    WHEN V.Category = 1 THEN 'Luxury'    --category
END AS Category,

R.custID AS CustomerID, C.CustomerName AS CustomerName, TotalAmount AS OrderAmount,

CASE
    WHEN PaymentDate IS NULL THEN TotalAmount
    WHEN PaymentDate IS NOT NULL THEN 0
END AS RentalBalance

FROM VEHICLE AS V NATURAL JOIN RENTAL AS R
NATURAL JOIN CUSTOMERS AS C
ORDER BY R.StartDate ASC;
