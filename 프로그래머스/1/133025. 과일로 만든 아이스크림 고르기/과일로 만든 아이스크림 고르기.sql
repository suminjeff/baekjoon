-- 코드를 입력하세요
select sales.flavor
from first_half as sales, icecream_info as info
where sales.flavor = info.flavor and sales.total_order > 3000 and info.ingredient_type = 'fruit_based'