import pyarrow as pa
import pyarrow.parquet as pq
import os
from dotenv import load_dotenv


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# Give path to json payload in Mage project folder
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/gcp_auth.json"

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
bucket_name = os.getenv("GCS_BUCKET_NAME")


@data_exporter
def export_data(data, *args, **kwargs):

    table_name = "genome_scores_data_parquet"
    root_path = f'{bucket_name}/{table_name}'
    

    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        filesystem=gcs
    )
    
   