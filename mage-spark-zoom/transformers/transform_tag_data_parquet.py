from pyspark.sql.functions import col, lower

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer

def transform(df_spark, *args, **kwargs):
    
    spark = kwargs.get('spark')
    df_spark = df_spark.withColumnRenamed("userId", "user_id")\
            .withColumnRenamed("movieId", "movie_id")\
            .withColumn("tag", lower(col("tag")))

    df = df_spark.toPandas()
    
    return df
