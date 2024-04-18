from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
import os
from os import path
from dotenv import load_dotenv

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_big_query(df: DataFrame, **kwargs) -> None:

    project_id = os.getenv("GCLOUD_PROJECT_ID")
    bq_name = os.getenv("GCS_BIGQUERY_NAME")
    table_name = "genome_scores"
    
    table_id = f'{project_id }.{bq_name}.{table_name}' 

    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        table_id,
        if_exists='replace',  # Specify resolution policy if table name already exists
    )
