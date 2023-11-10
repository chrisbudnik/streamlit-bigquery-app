from typing import Iterator, List, Any
import pandas as pd
from google.cloud import bigquery
from google.cloud.bigquery import QueryJobConfig
import json
import google.cloud.storage as gcs


bigquery_client = bigquery.Client()
cloudstorage_client = gcs.Client()


def save_to_bigquery(report_data: list, table_id: str) -> None:
    """
    Send formatted data to BigQuery.

    Parameters:
        report_data (list): The data to be inserted into BigQuery.
        table_id (str): The ID of the BigQuery table to insert data into.
    """

    table = bigquery_client.get_table(table_id)
    rows_to_insert = [report_data]
    bigquery_client.insert_rows_json(table, rows_to_insert)


def save_to_gcs(data: dict, bucket_name: str, blob_name: str) -> None:
    """
    Save data to Google Cloud Storage.

    Parameters:
        data (dict): The data to be saved.
        bucket_name (str): The name of the GCS bucket.
        blob_name (str): The name of the blob within the GCS bucket.
    """

    bucket = cloudstorage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(json.dumps(data))