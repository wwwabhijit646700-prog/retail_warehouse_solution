from pyspark import pipelines as ldp
from pyspark.sql.functions import *

expect_dict={
    "valid_discount": "discount >= 0 and discount < 1",
    "valid_price": "price > 0",
    "valid_sales_amount": "sales_amount>0",
    "valid_quantity": "quantity > 0",
    "valid_store_id": "store_id is not null",
    "valid_product_id": "product_id is not null"
}

@ldp.table(
    name="dwh_retail.silver.sales_silver",
    comment="This is silver sales table with quality data"
)
@ldp.expect_all_or_drop(
    expect_dict
)

def sales_silver():
    sales_silver=spark.sql(
        '''
        select sales.transaction_id,
        sales.date_id,
        sales.store_id,
        sales.product_id,
        sales.quantity,
        cast(sales.discount as decimal(3,2)) discount,
        sales.price,
        cast(sales.sales_amount as decimal(14,2)) sales_amount,
        sales.transaction_id||'~'||sales.date_id||'~'||sales.store_id||'~'||sales.product_id integration_id,
        sales.updated_at
        from stream(dwh_retail.bronze.sales_bronze) sales
        '''
    )
    return sales_silver