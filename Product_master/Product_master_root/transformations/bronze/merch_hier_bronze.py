from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.table(
    name="dwh_retail.bronze.merch_hier_bronze",
    comment="SRCI merch hierarchy data from source layer"
)
def merch_hier_bronze():
    merch_hier_bronze=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .option("cloudFiles.inferColumnTypes", "true")\
        .option("cloudFiles.schemaEvolutionMode","addNewColumns")\
        .load("/Volumes/dwh_retail/bronze/source_files/DIM_DATA/merch_hier/")

    merch_hier_bronze=merch_hier_bronze.withColumn("updated_dttm",lit(current_date()))
    merch_hier_bronze=merch_hier_bronze.withColumn("source_file",col("_metadata.file_name"))

    return merch_hier_bronze