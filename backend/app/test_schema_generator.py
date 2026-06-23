import sys
import os

# Add backend directory to sys.path so 'app' can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ai_engine.schemas.system_design import SystemDesignSchema
from app.ai_engine.compiler.schema_generator.generator import generate_schemas

def main():
    if not os.environ.get("GROQ_API_KEY"):
        print("Warning: GROQ_API_KEY is not set.")
    
    # Mock SystemDesignSchema output from the previous sprint
    mock_design = SystemDesignSchema(
        entities=["User", "Contact", "Payment"],
        pages=["Login", "Dashboard", "Contacts"],
        roles=["Admin", "User"],
        workflows=["Payment Processing", "Admin Analytics Access"]
    )
    
    print("--- Mock System Design Input ---")
    print(mock_design.model_dump_json(indent=2))
    print("\nStarting Schema Generation Pipeline (DB, API, UI, Auth)...\n")
    
    try:
        schemas = generate_schemas(mock_design)
        
        print("\n=== GENERATED SCHEMAS ===\n")
        print("--- DB Schema ---")
        print(schemas["db"].model_dump_json(indent=2))
        
        print("\n--- API Schema ---")
        print(schemas["api"].model_dump_json(indent=2))
        
        print("\n--- UI Schema ---")
        print(schemas["ui"].model_dump_json(indent=2))
        
        print("\n--- Auth Schema ---")
        print(schemas["auth"].model_dump_json(indent=2))
        
    except Exception as e:
        print(f"\nError during schema generation: {e}")

if __name__ == "__main__":
    main()
