from typing import Dict, Any, Tuple, List, Literal
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

    def get_requirements(self) -> Dict[str, Any]:
        """
        Get the query requirements based on the params.
        Used for marketing promo description.
        """
        return {
            param_name: param_value
            for param_name, param_value in self.params.items() 
            if param_value not in QueryConfig.DEFAULT_VALUES_TO_IGNORE
        }
    
    def _transform_params(self) -> Dict[str, QueryParam]:
        """
        Transform the input parameters to QueryParam objects, ignoring defaults.
        """
        return {
            param_name: QueryParam(
                name=param_name, 
                type=QueryConfig.DEFAULT_PARAMS_TYPES[param_name],
                value=param_value
            )
            for param_name, param_value in self.params.items()
            if param_value not in QueryConfig.DEFAULT_VALUES_TO_IGNORE
        }
    
    def _construct_where_clauses(self) -> List[str]:
        """
        Construct where clauses from the query parameters.
        """
        where_clauses = []
        for param in self.query_params.values():
            if isinstance(param.value, list):
                clause = f"{param.name} IN UNNEST(@{param.name})"
            else:
                operator = QueryConfig.DEFAULT_WHERE_OPERATORS[param.type]
                clause = f"{param.name} {operator} @{param.name}"

            where_clauses.append(clause)
        return where_clauses
    
    def _construct_query_params(self) -> List[ScalarQueryParameter]:
        """
        Construct query parameters for the BigQuery job.
        """
        query_params = []
        for param in self.query_params.values():
            if isinstance(param.value, list):
                query_param = ArrayQueryParameter(param.name, param.type, param.value)
            else:
                query_param = ScalarQueryParameter(param.name, param.type, param.value)
            query_params.append(query_param)
        return query_params
    
    def construct_query(self, 
                        result_type: Literal["group_counts", "export_list"] = "group_counts"
                    ) -> Tuple[str, QueryJobConfig]:
        """
        Construct the SQL query string dynamically based on set parameters
        and prepare the QueryJobConfig.
        """
        # Build the query parameters list and the where clause
        query_params = self._construct_query_params()
        where_clauses = self._construct_where_clauses()

        # Construct the full SQL query
        base_sql = QueryConfig.BASE_SQL 
        where_clause = "\n\tAND ".join(where_clauses)

        full_sql = f"{base_sql} {where_clause}" if where_clauses else base_sql + " 1=1"

        # Prepare the job config
        job_config = QueryJobConfig()
        job_config.query_parameters = query_params

        return full_sql, job_config

    
