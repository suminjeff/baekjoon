-- 코드를 입력하세요

select o.product_id, p.product_name, sum(o.amount)*p.price as total_sales
from food_product p, food_order o
where o.produce_date like '2022-05%' and o.product_id = p.product_id
group by o.product_id
order by total_sales desc, o.product_id asc
