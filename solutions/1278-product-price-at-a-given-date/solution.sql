# Write your MySQL query statement below
WITH LastPriceChange AS (
    SELECT
        product_id,
        new_price,
        change_date,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM
        Products
    WHERE
        change_date <= '2019-08-16'
)
SELECT
    p.product_id,
    COALESCE(lpc.new_price, 10) AS price
FROM
    (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN
    LastPriceChange lpc
ON
    p.product_id = lpc.product_id AND lpc.rn = 1;

