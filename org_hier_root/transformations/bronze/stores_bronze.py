from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.table(
    name="dwh_retail.bronze.stores_bronze",
    comment="SRCI stores bronze table to replicate source"
)

def stores_bronze():
    stores_bronze=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
        .option("cloudFiles.inferColumnTypes","true")\
        .option("cloudFiles.schemaEvolutionMode","addNewColumns")\
        .load("/Volumes/dwh_retail/bronze/source_files/DIM_DATA/stores/")
    stores_bronze=stores_bronze.withColumn("updated_dttm",lit(current_timestamp()))
    stores_bronze=stores_bronze.withColumn("source_file",col("_metadata.file_name"))

    return stores_bronze