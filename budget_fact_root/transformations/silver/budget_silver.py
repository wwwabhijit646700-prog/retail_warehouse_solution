from pyspark import pipelines as ldp
from pyspark.sql.functions import *

expect_dict={
    "valid_budget":"budget_amount>0",
    "valid_store":"store_id is not NULL",
    "valid_dept":"dept_id is not NULL",
    "valid_year":"year is not NULL"
}

@ldp.table(
    name="dwh_retail.silver.budget_silver",
    comment="This is a silver budget table with the expectations"
)

@ldp.expect_all_or_drop(
    expect_dict
)

def budget_silver():
    budget_silver=spark.sql(
        '''
        select 
        budget.budget_id,
        budget.store_id,
        budget.dept_id,
        budget.year,
        cast(budget.budget_amount as decimal(14,2)) budget_amount,
        budget.update_at
        from
        stream(dwh_retail.bronze.budget_bronze) budget
        '''
    )
    return budget_silver