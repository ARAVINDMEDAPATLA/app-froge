import os
from pydantic_ai import Agent
from app.ai_engine.schemas.intent import IntentSchema
from app.ai_engine.schemas.system_design import SystemDesignSchema

# Initialize the System Designer Agent
system_designer_agent = Agent(
    'google:gemini-2.0-flash',  # We use the same model, ideally swap in production
    output_type=SystemDesignSchema,
    system_prompt=(
        "You are an expert Software Architect and Product Manager. "
        "Your task is to take the user's raw intent and design a high-level system architecture. "
        "Analyze the provided Intent (app type, features, roles) and map it into: "
        "1. Core database entities needed. "
        "2. Core frontend pages needed. "
        "3. User roles for access control. "
        "4. High-level workflows and business logic rules. "
        "Return this as a structured SystemDesignSchema."
    )
)

def design_system(intent: IntentSchema) -> SystemDesignSchema:
    """
    Synchronously translates an IntentSchema into a SystemDesignSchema using PydanticAI.
    """
    # We pass the intent as a JSON string to the agent
    intent_json = intent.model_dump_json()
    result = system_designer_agent.run_sync(f"Design a system for this intent:\n{intent_json}")
    return result.data
