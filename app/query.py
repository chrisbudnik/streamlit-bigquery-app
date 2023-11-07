from dataclasses import dataclass, field
from typing import Any, List, Dict, Optional, Tuple, Literal
from google.cloud import bigquery
from google.cloud.bigquery import ScalarQueryParameter, QueryJobConfig


@dataclass
class QueryParam:
    name: str
    type: Literal["STRING", "INT64", "FLOAT64", "DATE", "BOOL"] = "STRING" 
    value: Optional[Any] = None
     

class QueryConstructor:
    def __init__(self):
        """
        Initialize the ParameterizedQuery with a list of default parameters.
        """
        # Convert the list of DefaultParam into a dictionary for easy access
        self.country = QueryParam(name="country", value="USA"),
        self.region = QueryParam(name="region", value="West"),
        self.segment = QueryParam(name="segment"),
        self.extended_group = QueryParam(name="extended_group", type="BOOL", value=False),

    
    
    def construct_query(self, base_sql: str) -> Tuple[str, QueryJobConfig]:
        """
        Construct the SQL query string dynamically based on set parameters
        and prepare the QueryJobConfig.
        """
        # Build the query parameters list and the where clause
        query_params = []
        where_clauses = []
        for param in self.params.values():
            if param.value is not None:  # Only include set parameters
                query_params.append(ScalarQueryParameter(param.name, param.type, param.value))
                where_clauses.append(f"{param.name} = @{param.name}")
        
        # Construct the full SQL query
        where_clause = " AND ".join(where_clauses)
        full_sql = f"{base_sql} WHERE {where_clause}" if where_clauses else base_sql
        
        # Prepare the job config
        job_config = QueryJobConfig()
        job_config.query_parameters = query_params
        
        return full_sql, job_config