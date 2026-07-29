from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.table(
    name="dwh_retail.bronze.budget_bronze",
    comment="This is a SRCI bronze nze yearly budget table"
)

def budget_bronze():
    budget_bronze=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
        .option("cloudFiles.schemaEvolutionMode","addNewColumns")\
        .option("cloudFiles.inferColumnTypes","True")\
        .load("/Volumes/dwh_retail/bronze/source_files/FACT_DATA/budget_fact/")
    
    budget_bronze=budget_bronze.withColumn("update_at",lit(current_timestamp()))
    budget_bronze=budget_bronze.withColumn("source_file",col("_metadata.file_name"))
    return budget_bronze