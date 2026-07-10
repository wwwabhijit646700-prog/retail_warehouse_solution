from pyspark import pipelines as ldp

ldp.create_streaming_table(
    name="dwh_retail.silver.merch_hier_silver",
    comment="CDC merch hierarchial data from bronze with SCD2"
)

ldp.create_auto_cdc_flow(
    source="dwh_retail.bronze.merch_hier_bronze",
    target="dwh_retail.silver.merch_hier_silver",
    keys=["subclass_id"],
    sequence_by="updated_dttm",
    stored_as_scd_type=2
)