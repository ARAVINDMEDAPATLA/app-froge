import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ai_engine.schemas.db_schema import DBSchema, Table, Column
from app.ai_engine.schemas.api_schema import APISchema, Route
from app.ai_engine.schemas.ui_schema import UISchema
from app.ai_engine.schemas.auth_schema import AuthSchema

from app.ai_engine.compiler.validator.cross_validator import validate_schemas
from app.ai_engine.compiler.repair_engine.repair import repair_schema

def main():
    print("--- Simulating Inconsistent Schemas ---")
    
    # DB has only User
    db = DBSchema(tables=[
        Table(name="User", columns=[Column(name="id", type="int")])
    ])
    
    # API tries to access Contact which doesn't exist in DB
    api = APISchema(routes=[
        Route(path="/contacts", method="GET", description="Get contacts", requires_auth=True)
    ])
    
    ui = UISchema(pages=[])
    auth = AuthSchema(roles=[], permissions=[])
    
    print("\n[Validator Engine] Running cross-layer validation...")
    errors = validate_schemas(db, api, ui, auth)
    
    if not errors:
        print("All schemas are valid.")
    else:
        for err in errors:
            print(f"Validation Failed: {err}")
            
            if not os.environ.get("GROQ_API_KEY"):
                print("Skipping repair since GROQ_API_KEY is not set.")
                continue
            
            print("\n[Repair Engine] Triggering AI Repair for specific layer...")
            try:
                # We repair the API schema, giving it the DB schema as context so it knows what entities exist
                repaired_api = repair_schema("API", api.model_dump_json(), err.message, context_schemas_json=db.model_dump_json())
                print("\n--- Repaired API Schema ---")
                print(repaired_api.model_dump_json(indent=2))
            except Exception as e:
                print(f"Repair failed: {e}")

if __name__ == "__main__":
    main()
