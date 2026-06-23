from pydantic_ai import Agent
from app.ai_engine.schemas.db_schema import DBSchema
from app.ai_engine.schemas.api_schema import APISchema
from app.ai_engine.schemas.ui_schema import UISchema
from app.ai_engine.schemas.auth_schema import AuthSchema

MODEL = 'groq:llama-3.3-70b-versatile'

# A generic repair agent that can be used for any schema type
repair_agent = Agent(
    MODEL,
    system_prompt=(
        "You are an expert AI Repair Engine. "
        "Your task is to fix schema validation errors without completely regenerating the schema from scratch. "
        "You will be given the Current Schema and the Validation Error. "
        "Output the corrected Schema that strictly resolves the error."
    )
)

def repair_schema(layer: str, current_schema_json: str, error_message: str, context_schemas_json: str = ""):
    """
    Repairs a specific schema layer using the LLM.
    """
    prompt = (
        f"Layer: {layer}\n"
        f"Validation Error: {error_message}\n"
        f"Current Failing Schema:\n{current_schema_json}\n"
        f"Context (Other Schemas to align with):\n{context_schemas_json}\n\n"
        "Please provide the corrected schema that aligns with the context and fixes the error."
    )
    
    # We dynamically set the output type based on the failing layer
    if layer == "API":
        return repair_agent.run_sync(prompt, output_type=APISchema).output
    elif layer == "DB":
        return repair_agent.run_sync(prompt, output_type=DBSchema).output
    elif layer == "UI":
        return repair_agent.run_sync(prompt, output_type=UISchema).output
    elif layer == "Auth":
        return repair_agent.run_sync(prompt, output_type=AuthSchema).output
    else:
        raise ValueError(f"Unknown layer to repair: {layer}")
