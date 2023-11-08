from typing import Iterator, List, Any
from google.cloud import bigquery
from google.cloud.bigquery import QueryJobConfig


def run_parameterized_query(sql: str, job_config: QueryJobConfig) -> Iterator[List[Any]]:
    """
    Run a parameterized query on BigQuery.
    """
    bigquery_client = bigquery.Client()
    return bigquery_client.query(sql, job_config=job_config)