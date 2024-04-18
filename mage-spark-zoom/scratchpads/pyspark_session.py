import os
from pyspark.sql import SparkSession


spark = SparkSession.builder.master(os.getenv('SPARK_MASTER_HOST', 'local')).config("spark.driver.memory", "6g").config("spark.executor.memory", "16g").config("spark.executor.instances", "1").config("spark.executor.cores", "6").config("spark.dynamicAllocation.enabled", "false").config("spark.executor.memoryOverhead", "2g").getOrCreate()