from pydantic import BaseModel, Field
from typing import List

class Route(BaseModel):
    path: str
    method: str  # GET, POST, PUT, DELETE
    description: str
    requires_auth: bool = True

class APISchema(BaseModel):
    """
    Structured representation of the API routing layer.
    """
    routes: List[Route] = Field(default_factory=list)
