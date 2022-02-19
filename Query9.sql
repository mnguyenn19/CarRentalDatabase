--9A.)
SELECT C.custID AS customerID, C.CustomerName AS CustomerName, V.VehicleDescription AS CarDescription, V.VehicleYear AS Year,
CASE
    WHEN V.VehicleType = 1 THEN 'Compact'    --type
    WHEN V.VehicleType = 2 THEN 'Medium'    --type
    WHEN V.VehicleType = 3 THEN 'Large'    --type
    WHEN V.VehicleType = 4 THEN 'SUV'    --type
    WHEN V.VehicleType = 5 THEN 'Truck'    --type
    WHEN V.VehicleType = 6 THEN 'Van'    --type
    --WHEN V.Category = 0 THEN 'Basic'    --category
    --WHEN V.Category = 1 THEN 'Luxury'    --category
END AS Vehicle_type,
CASE
    WHEN V.Category = 0 THEN 'Basic'    --category
    WHEN V.Category = 1 THEN 'Luxury'    --category
END AS Vehicle_category, 

R.TotalAmount/R.Qty AS Unit_Price, R.RentalType*R.Qty AS Duration_in_days, R.TotalAmount,

CASE
    WHEN R.PaymentDate IS NULL THEN 'No Payment'
    WHEN R.PaymentDate IS NOT NULL THEN R.PaymentDate
END AS payment_exist,

R.StartDate AS startDate, R.ReturnDate AS returnDate

FROM RENTAL AS R NATURAL JOIN VEHICLE AS V NATURAL JOIN CUSTOMERS AS C
WHERE C.CustomerName = 'J. Brown'
ORDER BY R.StartDate ASC;

--9B.)
SELECT C.custID AS customerID, C.CustomerName AS CustomerName, SUM(R.TotalAmount) AS current_balance
FROM CUSTOMERS AS C NATURAL JOIN RENTAL AS R 
WHERE C.CustomerName = 'J. Brown' AND R.PaymentDate IS NULL;


--5.)





--SELECT julianday(strftime('%m/%d/%Y', R.ReturnDate)) - julianday(strftime('%m/%d/%Y', R.StartDate))
--FROM RENTAL AS R;

--SELECT strftime('%m/%d/%Y', R.ReturnDate)
--FROM RENTAL AS R;
