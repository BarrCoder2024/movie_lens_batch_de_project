from pandas import DataFrame
import pyarrow as pa
import pyarrow.parquet as pq
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/gcp_auth.json"

bucket_name = 'movielens_parquet_zoom_data'
table_name = 'movie_data_parquet'
root_path = f'{bucket_name}/{table_name}'
 
gcs = pa.fs.GcsFileSystem() 

@data_loader

def load_data(*args, **kwargs)-> DataFrame:
    
    arrow_df = pq.ParquetDataset(root_path, filesystem=gcs)
    print(arrow_df.schema)
    
    df = arrow_df.read_pandas().to_pandas()
    df_spark = kwargs['spark'].createDataFrame(df)
    
    return df_spark