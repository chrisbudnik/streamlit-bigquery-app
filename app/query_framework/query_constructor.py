from typing import Dict, Any, Tuple  
from .query_param import QueryParam
from .query_config import QueryConfig
from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter


class QueryConstructor:
    def __init__(self, requirements) -> None:
        """
        Initialize the QueryConstructor with a list of requirements.
        """
        self.requirements = requirements
        self.params = self._transform_params()

    def _transform_params(self) -> Dict[str, QueryParam]:
        """
        Get the query parameters based on the requirements.
        """
        params = {}
        for param_name, param_value in self.requirements.items():

            params[param_name] = QueryParam(name=param_name, 
                                            type=QueryConfig.DEFAULT_PARAMS_TYPES[param_name],
                                            value=param_value)

        return params

    
    def construct_query(self) -> Tuple[str, QueryJobConfig]:
        """
        Construct the SQL query string dynamically based on set parameters
        and prepare the QueryJobConfig.
        """
        # Build the query parameters list and the where clause
        query_params = []
        where_clauses = []
        for param in self.params.values():
            if param.value is not None:
                scalar_param = ScalarQueryParameter(param.name, param.type, param.value)
                query_params.append(scalar_param)
                where_clauses.append(f"{param.name} = @{param.name}")

        # Construct the full SQL query
        base_sql = QueryConfig.BASE_SQL 
        where_clause = "\n\tAND ".join(where_clauses)

        full_sql = f"{base_sql} {where_clause}" if where_clauses else base_sql

        # Prepare the job config
        job_config = QueryJobConfig()
        job_config.query_parameters = query_params

        return full_sql, job_config
    
