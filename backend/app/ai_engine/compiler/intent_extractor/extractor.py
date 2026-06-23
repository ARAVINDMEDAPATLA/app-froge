import os
from pydantic_ai import Agent
from app.ai_engine.schemas.intent import IntentSchema

# We define a PydanticAI Agent that is strictly typed to return an IntentSchema
# We can use the default model or specify a specific one like 'google:gemini-2.0-flash'
intent_extractor_agent = Agent(
    'google:gemini-2.0-flash',
    output_type=IntentSchema,
    system_prompt=(
        "You are an expert AI system architect. "
        "Your task is to analyze user prompts for software applications and extract the core intent. "
        "You must identify the application type, the core features requested, and any user roles mentioned. "
        "Be concise and extract only what is explicitly requested or highly implied by standard architecture."
    )
)

def extract_intent(user_prompt: str) -> IntentSchema:
    """
    Synchronously extracts the intent from a user prompt using PydanticAI.
    """
    # Run the agent and return the structured data
    result = intent_extractor_agent.run_sync(user_prompt)
    return result.data
