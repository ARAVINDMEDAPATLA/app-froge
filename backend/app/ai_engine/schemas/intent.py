from pydantic import BaseModel, Field
from typing import List, Optional

class IntentSchema(BaseModel):
    """
    The structured intermediate representation of a user's natural language request.
    This schema captures the high-level intent before system design occurs.
    """
    app_type: str = Field(
        ..., 
        description="The general category or type of application being built (e.g., 'CRM', 'E-commerce', 'Dashboard')"
    )
    features: List[str] = Field(
        default_factory=list, 
        description="A list of core features requested by the user (e.g., 'login', 'contacts', 'payments')"
    )
    roles: List[str] = Field(
        default_factory=list, 
        description="A list of user roles identified in the request (e.g., 'admin', 'user', 'guest')"
    )
    additional_notes: Optional[str] = Field(
        None, 
        description="Any other constraints or ambiguous requirements that need to be captured."
    )
