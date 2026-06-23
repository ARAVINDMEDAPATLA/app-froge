import os
from pydantic_ai import Agent

from app.ai_engine.schemas.system_design import SystemDesignSchema
from app.ai_engine.schemas.db_schema import DBSchema
from app.ai_engine.schemas.api_schema import APISchema
from app.ai_engine.schemas.ui_schema import UISchema
from app.ai_engine.schemas.auth_schema import AuthSchema

MODEL = 'groq:llama-3.3-70b-versatile'

# 1. DB Schema Agent
db_agent = Agent(
    MODEL,
    output_type=DBSchema,
    system_prompt=(
        "You are an expert Database Architect. "
        "Based on the provided System Design, generate a strict relational Database Schema. "
        "Define all tables, columns, primary keys, and foreign keys."
    )
)

# 2. API Schema Agent
api_agent = Agent(
    MODEL,
    output_type=APISchema,
    system_prompt=(
        "You are an expert Backend API Architect. "
        "Based on the provided System Design, generate the required REST API endpoints. "
        "Ensure there are routes for CRUD operations on the core entities."
    )
)

# 3. UI Schema Agent
ui_agent = Agent(
    MODEL,
    output_type=UISchema,
    system_prompt=(
        "You are an expert Frontend Architect. "
        "Based on the provided System Design, generate the UI Schema. "
        "Define pages, routes, and the components needed on each page."
    )
)

# 4. Auth Schema Agent
auth_agent = Agent(
    MODEL,
    output_type=AuthSchema,
    system_prompt=(
        "You are an expert Security Architect. "
        "Based on the provided System Design, generate the Authorization Schema. "
        "Define exact roles and the granular permissions required for access control."
    )
)

def generate_schemas(design: SystemDesignSchema):
    """
    Synchronously generates the 4 core schemas from the System Design.
    """
    design_json = design.model_dump_json()
    prompt = f"System Design:\n{design_json}"
    
    print("Generating DB Schema...")
    db_result = db_agent.run_sync(prompt)
    
    print("Generating API Schema...")
    api_result = api_agent.run_sync(prompt)
    
    print("Generating UI Schema...")
    ui_result = ui_agent.run_sync(prompt)
    
    print("Generating Auth Schema...")
    auth_result = auth_agent.run_sync(prompt)
    
    return {
        "db": db_result.output,
        "api": api_result.output,
        "ui": ui_result.output,
        "auth": auth_result.output
    }
