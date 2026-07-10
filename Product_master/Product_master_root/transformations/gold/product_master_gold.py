from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.materialized_view(
    name="dwh_retail.gold.product_master_gold",
    comment="This is semantic product master table"
)

def product_master_gold():
    product_master_gold=spark.sql(
        '''
        select p.product_id ,p.product_name,m.dept_id,m.dept_name,m.class_id,m.class_name,m.subclass_id,m.subclass_name,p.price, 'Y' active_ind
        from dwh_retail.silver.product_silver p
        inner join
        dwh_retail.silver.merch_hier_silver m
        on
        p.subclass_id=m.subclass_id
        and p.__end_at is NULL and m.__end_at is NULL
        '''
    )
    return product_master_gold