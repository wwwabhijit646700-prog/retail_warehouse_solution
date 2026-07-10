from pyspark import pipelines as ldp
from pyspark.sql.functions import *

@ldp.table(
    name="dwh_retail.silver.calendar_silver",
    comment="Calendar silver table with small transformation"
)

def calendar_silver():
    calendar_silver=spark.sql(
        '''
        select c.date_id,
        c.date ty_date,
        c.year,
        c.quarter,
        case c.month
        when 1 then 'January'
        when 2 then 'February'
        when 3 then 'March'
        when 4 then 'April'
        when 5 then 'May'
        when 6 then 'June'
        when 7 then 'July'
        when 8 then 'August'
        when 9 then 'September'
        when 10 then 'October'
        when 11 then 'November'
        when 12 then 'December'
        end month,
        c.day,
        case c.weekday
        when 1 then 'Monday'
        when 2 then 'Tuesday'
        when 3 then 'Wednesday'
        when 4 then 'Thursday'
        when 5 then 'Friday'
        when 6 then 'Saturday'
        when 7 then 'Sunday'
        end weekday
        from stream(dwh_retail.bronze.calendar_bronze) c
        '''
    )
    return calendar_silver