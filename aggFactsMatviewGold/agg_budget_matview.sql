create or refresh materialized view dwh_retail.gold.agg_budget_gold
cluster by (Year,Store_id)
as
with department as(
    select distinct dept_id,dept_name from dwh_retail.silver.merch_hier_silver
)
select 
budget.year Year,
store.store_id Store_id,
store.store_name  Store_name,
department.dept_id Department_id,
department.dept_name Department_name,
budget.budget_amount Budget_amount,
current_timestamp Refreshed_at
from 
dwh_retail.silver.budget_silver budget
inner join 
dwh_retail.gold.store_master_gold store
on 
budget.store_id=store.store_id
and
store.active_ind='Y'
inner join
department
on
budget.dept_id=department.dept_id
