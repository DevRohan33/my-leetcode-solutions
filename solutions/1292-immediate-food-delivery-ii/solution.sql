# Write your MySQL query statement below
WITH FirstOrders AS (
    SELECT 
        customer_id, 
        MIN(order_date) AS first_order_date
    FROM 
        Delivery
    GROUP BY 
        customer_id
),
FirstOrdersDetails AS (
    SELECT 
        f.customer_id,
        f.first_order_date,
        d.customer_pref_delivery_date,
        CASE 
            WHEN f.first_order_date = d.customer_pref_delivery_date THEN 'immediate'
            ELSE 'scheduled'
        END AS order_type
    FROM 
        FirstOrders f
    JOIN 
        Delivery d
    ON 
        f.customer_id = d.customer_id 
        AND f.first_order_date = d.order_date
)
SELECT 
    ROUND(
        SUM(CASE WHEN order_type = 'immediate' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 
        2
    ) AS immediate_percentage
FROM 
    FirstOrdersDetails;


