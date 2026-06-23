import sys
import os

# Add backend directory to sys.path so 'app' can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ai_engine.schemas.intent import IntentSchema
from app.ai_engine.compiler.system_designer.designer import design_system

def main():
    if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("OPENAI_API_KEY"):
        print("Warning: Neither GEMINI_API_KEY nor OPENAI_API_KEY is set. The extraction may fail.")
    
    # Mocking the IntentSchema output that we would have gotten from the Intent Extractor
    mock_intent = IntentSchema(
        app_type="CRM",
        features=["login", "contacts", "dashboard", "premium plan with payments", "analytics"],
        roles=["Admin", "User"],
        additional_notes="Admins can see analytics."
    )
    
    print("--- Mock Intent Input ---")
    print(mock_intent.model_dump_json(indent=2))
    print("\nDesigning System Architecture...")
    
    try:
        design = design_system(mock_intent)
        print("\n--- Extracted System Design ---")
        print(design.model_dump_json(indent=2))
    except Exception as e:
        print(f"\nError during system design: {e}")

if __name__ == "__main__":
    main()
