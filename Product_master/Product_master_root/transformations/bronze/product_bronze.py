from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.table(
    name="dwh_retail.bronze.product_bronze",
    comment="SRCI product data from source layer"
)
def product_bronze():
    product_bronze=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .option("cloudFiles.inferColumnTypes", "true")\
        .option("cloudFiles.schemaEvolutionMode","addNewColumns")\
        .load("/Volumes/dwh_retail/bronze/source_files/DIM_DATA/Products/")
    
    product_bronze=product_bronze.withColumn("updated_dttm",lit(current_date()))
    product_bronze=product_bronze.withColumn("source_file",col("_metadata.file_name"))

    return product_bronze