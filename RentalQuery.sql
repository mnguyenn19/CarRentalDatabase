--Task 2 (before task 3 queries)
SELECT COUNT(*)
FROM CUSTOMERS;

SELECT COUNT(*)
FROM VEHICLE;

SELECT COUNT(*)
FROM RENTAL;

SELECT COUNT(*)
FROM RATE;


--QUETSION 1
--inserting myself as a new customer
--INSERT INTO CUSTOMERS (CustomerName,Phone)
--VALUES ('Kevin Phan','(817) 111-1111'); 

--QUESTION 2
--update your phone number to (817) 721-8965
--UPDATE CUSTOMERS
--SET Phone = '(837) 721-8965'
--WHERE CustomerName = 'Kevin Phan';



--QUESTION 5
--SELECT DISTINCT V.VehicleID AS VIN, V.VehicleDescription, V.VehicleYear
--FROM VEHICLE AS V NATURAL JOIN RENTAL AS R
--WHERE (R.OrderDate IS NOT(R.OrderDate BETWEEN '06/01/2019' AND '06/20/2019') AND R.StartDate IS NOT (R.StartDate BETWEEN '06/01/2019' AND '06/20/2019')) AND V.Category = 1 AND V.VehicleType = 1;


--SELECT
--FROM CUSTOMERS AS C 
--JOIN RENTAL AS R ON C.custID = R.custID
--JOIN VEHICLE AS V ON R.VehicleID = V.VehicleID



SELECT V.VehicleID AS VIN, V.VehicleDescription AS Description, V.VehicleYear AS Year, V.Category, R.Weekly AS Weekly, R.Daily AS Daily,
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
END AS Vehicle_category
FROM VEHICLE V NATURAL JOIN RATE R
WHERE V.Category = R.Category AND V.VehicleType = R.VehicleType

ORDER BY V.Category DESC, V.VehicleType;
