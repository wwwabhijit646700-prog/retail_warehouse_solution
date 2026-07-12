from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.materialized_view(
    name="dwh_retail.gold.store_master_gold",
    comment="This is semantic product master table"
)
def store_master_gold():
    store_master_gold=spark.sql(
        '''
        select s.store_id,s.store_name,r.org_name,'Y' active_ind from
        dwh_retail.silver.stores_silver s
        inner join dwh_retail.silver.region_silver r
        on s.org_id=r.org_id
        and s.__end_at is null and r.__end_at is null
        '''
    )
    return store_master_gold