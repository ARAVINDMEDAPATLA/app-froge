import sys
import os

# Add backend directory to sys.path so 'app' can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ai_engine.compiler.intent_extractor.extractor import extract_intent

def main():
    if not os.environ.get("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY is not set. The extraction may fail if not configured with a default key.")
    
    sample_prompt = (
        "Build a CRM with login, contacts, dashboard, role-based access, and premium "
        "plan with payments. Admins can see analytics."
    )
    
    print(f"--- Input Prompt ---\n{sample_prompt}\n")
    print("Extracting intent...")
    
    try:
        intent = extract_intent(sample_prompt)
        print("\n--- Extracted Intent ---")
        print(intent.model_dump_json(indent=2))
    except Exception as e:
        print(f"\nError during extraction: {e}")

if __name__ == "__main__":
    main()
