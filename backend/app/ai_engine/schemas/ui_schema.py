from pydantic import BaseModel, Field
from typing import List

class UIComponent(BaseModel):
    name: str
    type: str  # e.g., 'Form', 'Table', 'Chart', 'Button'
    description: str

class UIPage(BaseModel):
    name: str
    route: str
    components: List[UIComponent] = Field(default_factory=list)

class UISchema(BaseModel):
    """
    Structured representation of the Frontend UI layer.
    """
    pages: List[UIPage] = Field(default_factory=list)
