use orders_db;

-- select * from orders;
-- select category,count(*) AS order_count from orders group by category having count(*)>2;


-- select city,SUM(quantity * price) as total_revenue from orders group by city having SUM(quantity * price) > 1000;

-- select category,sum(quantity*price) as revenue from orders where status='Completed' group by category;

-- select category,avg(price) as avg_price from orders group by category having avg(price) > 400;

-- select category,sum(quantity*price) as total_revenue from orders group by category order by sum(quantity*price) desc limit 1;


-- select city,category,count(*) as total_orders from orders group by city,category;

-- select count(distinct customer) as unique_customers from orders;

-- select round(avg(quantity * price),2) as avg_order_value from orders where status='Completed';

-- select category,sum(quantity) as total_item from orders group by category having sum(quantity)>5

select 
	category,
    count(*) as order_count,
    sum(quantity) as total_items,
    round(avg(price),2) as avg_price,
    sum(quantity*price) as total_revenue
from orders
group by category
having sum(quantity*price) > 1000;
