from pyspark import pipelines as ldp

@ldp.table(
    name="dwh_retail.bronze.calendar_bronze",
    comment="SRCI load for calendar data from source"
)

def calendar_bronze():
    calendar_bronze=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
        .option("cloudFiles.schemaEvolutionMode", "addNewColumns")\
        .option("cloudFiles.inferColumnTypes", "true")\
        .load("/Volumes/dwh_retail/bronze/source_files/DIM_DATA/calendar/")
    
    return calendar_bronze