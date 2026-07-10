from pyspark import pipelines as ldp

ldp.create_streaming_table(
    name="dwh_retail.bronze.region_silver",
    comment="CDC silver region layer using SCD2"
)

ldp.create_auto_cdc_flow(
    source="dwh_retail.bronze.region_bronze",
    target="dwh_retail.bronze.region_silver",
    keys=["org_id"],
    sequence_by="updated_dttm",
    stored_as_scd_type=2
)
