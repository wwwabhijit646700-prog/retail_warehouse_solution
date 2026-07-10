from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.materialized_view(
    name="dwh_retail.gold.calendar_master_gold",
    comment="Calendar master table for gold layer"
)

def calendar_master_gold():
    calendar_master_gold=spark.sql(
        '''
        select 
        c.date_id,
        c.ty_date,
        c.year,
        c.quarter,
        c.month,
        c.day,
        c.weekday,
        lag(c.ty_date,7,'1900-01-01') over(partition by c.year order by c.ty_date) lw_date,
        min(c.ty_date) over(partition by c.year) year_start_date,
        max(c.ty_date) over(partition by c.year) year_end_date
        from dwh_retail.silver.calendar_silver c
        '''
    )
    return calendar_master_gold