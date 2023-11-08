from typing import Any, Optional, Literal
from dataclasses import dataclass

@dataclass
class QueryParam:
    name: str
    type: Literal["STRING", "INT64", "FLOAT64", "DATE", "BOOL"] = "STRING" 
    value: Optional[Any] = None