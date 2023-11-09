from typing import Dict, Any, Tuple, Literal
from .query_param import QueryParam
from .query_config import QueryConfig
from google.cloud.bigquery import (
    QueryJobConfig, ScalarQueryParameter, ArrayQueryParameter
)


class QueryConstructor:
    def __init__(self, params: Dict) -> None:
        """
        Initialize the QueryConstructor with a list of params.
        """
        self.params = params
        self.query_params = self._transform_params()


    def _transform_params(self) -> Dict[str, QueryParam]:
        """
        Get the query parameters based on the params.
        """
        params = {}
        for param_name, param_value in self.params.items():
            if param_value in QueryConfig.DEFAULT_VALUES_TO_IGNORE:
                continue

            params[param_name] = QueryParam(name=param_name, 
                                            type=QueryConfig.DEFAULT_PARAMS_TYPES[param_name],
                                            value=param_value)
        return params
    
    def get_requirements(self) -> Dict[str, Any]:
        """
        Get the query requirements based on the params.
        """
        requirements = {k:v for k,v in self.params.items() if v not in QueryConfig.DEFAULT_VALUES_TO_IGNORE}
        return requirements

    def construct_query(self, result_type: Literal["group_counts", "export_list"]) -> Tuple[str, QueryJobConfig]:
        """
        Construct the SQL query string dynamically based on set parameters
        and prepare the QueryJobConfig.
        """
        # Build the query parameters list and the where clause
        query_params = []
        where_clauses = []

        for param in self.query_params.values():
            # Use ArrayQueryParameter for lists
            if isinstance(param.value, list):
                query_params.append(ArrayQueryParameter(param.name, param.type, param.value))
                where_clause = f"UNNEST(@{param.name})"
                where_clauses.append(f"{param.name} IN {where_clause}")

            # Use ScalarQueryParameter for scalar values
            else:
                query_params.append(ScalarQueryParameter(param.name, param.type, param.value))
                if param.type == 'BOOL':
                    where_clauses.append(f"{param.name}")
                elif param.type == 'DATE':
                    where_clauses.append(f"{param.name} <= @{param.name}")
                else:
                    where_clauses.append(f"{param.name} = @{param.name}")

        # Construct the full SQL query
        base_sql = QueryConfig.BASE_SQL 
        where_clause = "\n\tAND ".join(where_clauses)

        full_sql = f"{base_sql} {where_clause}" if where_clauses else base_sql

        # Prepare the job config
        job_config = QueryJobConfig()
        job_config.query_parameters = query_params

        return full_sql, job_config
    
