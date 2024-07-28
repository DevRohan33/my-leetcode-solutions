# Write your MySQL query statement below
WITH SameTIV2015 AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
),
UniqueLocation AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
),
FilteredInsurance AS (
    SELECT *
    FROM Insurance
    WHERE tiv_2015 IN (SELECT tiv_2015 FROM SameTIV2015)
      AND (lat, lon) IN (SELECT lat, lon FROM UniqueLocation)
)
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM FilteredInsurance;

