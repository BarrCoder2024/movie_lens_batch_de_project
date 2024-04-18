import pandas as pd
from pandas import DataFrame
import requests
import base64
import zipfile
import io

@data_loader
def data_from_kaggle(**kwargs):
    # Kaggle data URL
    base_url = "https://www.kaggle.com/api/v1"
    owner_slug = "grouplens"
    dataset_slug = "movielens-20m-dataset"
    dataset_version = "1"
        
    kaggle_username = kwargs.get('kaggle_username')
    kaggle_key = kwargs.get('kaggle_key')

    url = f"{base_url}/datasets/download/{owner_slug}/{dataset_slug}?datasetVersionNumber={dataset_version}"

    creds = base64.b64encode(bytes(f"{kaggle_username}:{kaggle_key}", "ISO-8859-1")).decode("ascii")
    headers = {
    "Authorization": f"Basic {creds}"
    }

    # Send GET request to the Kaggle URL with Kaggle credentials.
    response = requests.get(url, headers=headers)

    # Load response as file via io and open via zipfile.
    zf = zipfile.ZipFile(io.BytesIO(response.content))

    # Read CSV from zip file and convert to a dataframe.
    file_name = "rating.csv"

    rating_dtypes = {
        'userId':'int32',
        'movieId':'int32',
        'rating':'float32'
    }

    parse_dates = ['timestamp'] 

    df = pd.read_csv(zf.open(file_name), sep=",",dtype=rating_dtypes, parse_dates=parse_dates)
    return df
