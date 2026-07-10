from pyspark import pipelines as ldp

ldp.create_streaming_table(
    name="dwh_retail.silver.product_silver",
    comment="CDC product data from bronze with SCD2"
)

ldp.create_auto_cdc_flow(
    source="dwh_retail.bronze.product_bronze",
    target="dwh_retail.silver.product_silver",
    keys=["product_id"],
    sequence_by="updated_dttm",
    stored_as_scd_type=2
)