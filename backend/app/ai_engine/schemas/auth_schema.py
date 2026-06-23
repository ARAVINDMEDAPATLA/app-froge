from pydantic import BaseModel, Field
from typing import List

class Permission(BaseModel):
    role: str
    access: str  # e.g., '*', 'read', 'write'
    resource: str  # e.g., 'Payment', 'Dashboard'

class AuthSchema(BaseModel):
    """
    Structured representation of the Authentication and Authorization layer.
    """
    roles: List[str] = Field(default_factory=list)
    permissions: List[Permission] = Field(default_factory=list)
