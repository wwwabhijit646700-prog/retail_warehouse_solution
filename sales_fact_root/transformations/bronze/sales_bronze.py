from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.table(
    name="dwh_retail.bronze.sales_bronze",
    comment="This is bronze SRCI sales table"
)

def sales_bronze():
    sales_bronze=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
        .option("cloufFiles.schemaEvolutionMode","addNewColumns")\
        .option("cloudFiles.inferColumnTypes","True")\
        .load("/Volumes/dwh_retail/bronze/source_files/FACT_DATA/Sales_fact/")
    sales_bronze=sales_bronze.withColumn("updated_at",lit(current_timestamp()))
    sales_bronze=sales_bronze.withColumn("source_file",col("_metadata.file_name"))
    return sales_bronze
