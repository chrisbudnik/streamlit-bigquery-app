from typing import Iterator, List, Any
import pandas as pd
from google.cloud import bigquery
from google.cloud.bigquery import QueryJobConfig
import json
import google.cloud.storage as gcs
import streamlit as st  

@st.cache()
def fetch_query_results(sql: str, job_config: QueryJobConfig) -> pd.DataFrame:
    """
    Run a parameterized query on BigQuery.
    """
    bigquery_client = bigquery.Client()
    return bigquery_client.query(sql, job_config=job_config).to_dataframe()

