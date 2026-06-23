from pydantic import BaseModel, Field
from typing import List

class SystemDesignSchema(BaseModel):
    """
    Translates the Intent into a high-level system architecture.
    This acts as the 'Product Manager' layer, deciding what exactly needs to be built.
    """
    entities: List[str] = Field(
        default_factory=list,
        description="Core database entities needed (e.g., 'User', 'Contact', 'Payment')"
    )
    pages: List[str] = Field(
        default_factory=list,
        description="Core frontend pages/views needed (e.g., 'Login', 'Dashboard', 'Contacts')"
    )
    roles: List[str] = Field(
        default_factory=list,
        description="User roles for access control (e.g., 'Admin', 'User')"
    )
    workflows: List[str] = Field(
        default_factory=list,
        description="High-level business logic workflows (e.g., 'Payment Processing', 'Admin Analytics Access')"
    )
