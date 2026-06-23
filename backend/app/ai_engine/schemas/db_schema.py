from pydantic import BaseModel, Field
from typing import List

class Column(BaseModel):
    name: str
    type: str  # e.g., 'string', 'integer', 'boolean'
    is_primary_key: bool = False
    is_foreign_key: bool = False
    references: str | None = None  # Table name if it's a foreign key

class Table(BaseModel):
    name: str
    columns: List[Column] = Field(default_factory=list)

class DBSchema(BaseModel):
    """
    Structured representation of the database layer.
    """
    tables: List[Table] = Field(default_factory=list)
