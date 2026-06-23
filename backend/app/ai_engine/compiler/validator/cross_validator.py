from typing import Dict, List, Any
from app.ai_engine.schemas.db_schema import DBSchema
from app.ai_engine.schemas.api_schema import APISchema
from app.ai_engine.schemas.ui_schema import UISchema
from app.ai_engine.schemas.auth_schema import AuthSchema

class ValidationError(Exception):
    def __init__(self, layer: str, message: str, context: Any = None):
        self.layer = layer
        self.message = message
        self.context = context
        super().__init__(f"[{layer}] {message}")

def validate_schemas(db: DBSchema, api: APISchema, ui: UISchema, auth: AuthSchema) -> List[ValidationError]:
    """
    Cross-validates schemas to ensure consistency.
    Returns a list of validation errors. If empty, validation passed.
    """
    errors = []
    
    # 1. API -> DB Validation
    # Check if API routes that clearly reference entities exist in the DB schema
    db_table_names = {table.name.lower() for table in db.tables}
    for route in api.routes:
        # Simplistic heuristic: if route path starts with /entity_name, entity should exist
        base_path = route.path.split('/')[1] if len(route.path) > 1 else ""
        # Handle plurals simplistically (e.g., users -> user)
        if base_path.endswith('s'):
            singular = base_path[:-1].lower()
            if singular not in db_table_names and base_path not in db_table_names:
                errors.append(ValidationError("API", f"Route '{route.path}' references unknown entity '{base_path}' not found in DB Schema."))

    # 2. Auth -> DB/UI Validation
    # Ensure Auth roles and resources map to known elements
    valid_resources = db_table_names.union({page.name.lower() for page in ui.pages})
    valid_resources.update({workflow.lower() for workflow in ["Payment Processing", "Admin Analytics Access"]}) # Ideally passed from SystemDesign
    
    for perm in auth.permissions:
        if perm.resource.lower() not in valid_resources:
            errors.append(ValidationError("Auth", f"Permission references unknown resource '{perm.resource}'."))

    return errors
