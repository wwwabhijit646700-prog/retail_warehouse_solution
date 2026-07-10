from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.table(
    name="dwh_retail.bronze.region_bronze",
    comment="SRCI region bronze table to replicate source"
)

def region_bronze():
    region_bronze=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
        .option("cloudFiles.inferColumnTypes","true")\
        .option("cloudFiles.schemaEvolutionMode","addNewColumns")\
        .load("/Volumes/dwh_retail/bronze/source_files/DIM_DATA/region/")
    
    region_bronze=region_bronze.withColumn("updated_dttm",lit(current_timestamp()))
    region_bronze=region_bronze.withColumn("source_file",col("_metadata.file_name"))
    return region_bronze