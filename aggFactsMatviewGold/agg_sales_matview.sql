create or refresh materialized view dwh_retail.gold.agg_sales_gold
cluster by (Business_day,Store_id)
as
select 
sales.transaction_id Transaction_id,
cal.ty_date Business_day,
store.store_id Store_id,
store.store_name  Store_name ,
store.org_name  Org_name ,
cal.year  Year ,
cal.month  Month ,
cal.weekday  Weekday ,
year(cal.ty_date)||lpad(weekofyear(cal.ty_date),2,0)  Year_week ,
prod.product_id  Product_id ,
prod.product_name  Product_name ,
prod.dept_id  Department_id ,
prod.dept_name  Department_name ,
prod.class_id  Class_id ,
prod.class_name Class_name ,
prod.subclass_id  Subclass_id ,
prod.subclass_name  Subclass_name ,
sales.quantity  Quantity ,
sales.discount  Discount ,
sales.price  Product_price ,
sales.sales_amount  Sales_amount ,
sales.integration_id  Integration_id ,
current_timestamp() Refreshed_at,
cal.lw_date  LW_date ,
cal.year_start_date  Year_start_date ,
cal.year_end_date  Year_end_date
from
dwh_retail.silver.sales_silver sales
inner join
dwh_retail.gold.calendar_master_gold cal
on
sales.date_id=cal.date_id
inner join
dwh_retail.gold.load_token token
on cal.year between token.LLLY and token.TY
and token.description = 'History_3_years'
inner join
dwh_retail.gold.store_master_gold store
on
sales.store_id=store.store_id
and store.active_ind='Y'
inner join
dwh_retail.gold.product_master_gold prod
on
sales.product_id=prod.product_id
and prod.active_ind='Y';