# Write your MySQL query statement below
WITH RevenuePerProduct AS (
    SELECT 
        p.product_id,
        COALESCE(SUM(u.units), 0) AS total_units,
        COALESCE(SUM(p.price * u.units), 0) AS total_revenue
    FROM 
        Prices p
    LEFT JOIN 
        UnitsSold u 
    ON 
        p.product_id = u.product_id
    AND 
        u.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY 
        p.product_id
)
SELECT 
    product_id,
    ROUND(
        CASE 
            WHEN total_units = 0 THEN 0 
            ELSE total_revenue / total_units 
        END, 2) AS average_price
FROM 
    RevenuePerProduct;


