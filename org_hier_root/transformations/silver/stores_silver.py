from pyspark import pipelines as ldp

ldp.create_streaming_table(
    name="dwh_retail.silver.stores_silver",
    comment="CDC silver stores layer using SCD2"
)

ldp.create_auto_cdc_flow(
    source="dwh_retail.bronze.stores_bronze",
    target="dwh_retail.silver.stores_silver",
    keys=["store_id"],
    sequence_by="updated_dttm",
    stored_as_scd_type=2
)
