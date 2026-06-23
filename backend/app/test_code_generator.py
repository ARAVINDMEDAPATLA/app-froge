import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ai_engine.schemas.db_schema import DBSchema, Table, Column
from app.ai_engine.schemas.api_schema import APISchema, Route
from app.ai_engine.schemas.ui_schema import UISchema, UIPage, UIComponent

from app.ai_engine.compiler.code_generator.db_gen import generate_db_code
from app.ai_engine.compiler.code_generator.api_gen import generate_api_code
from app.ai_engine.compiler.code_generator.ui_gen import generate_ui_code

def main():
    print("--- Simulating Validated Schemas ---\n")
    
    # 1. DB
    db = DBSchema(tables=[
        Table(name="User", columns=[
            Column(name="id", type="int", is_primary_key=True),
            Column(name="username", type="string"),
        ]),
        Table(name="Contact", columns=[
            Column(name="id", type="int", is_primary_key=True),
            Column(name="user_id", type="int", is_foreign_key=True, references="User.id"),
            Column(name="name", type="string")
        ])
    ])
    
    # 2. API
    api = APISchema(routes=[
        Route(path="/users", method="GET", description="Get all users", requires_auth=True),
        Route(path="/users/{id}", method="GET", description="Get user by ID", requires_auth=True),
        Route(path="/contacts", method="POST", description="Create a contact", requires_auth=True),
    ])
    
    # 3. UI
    ui = UISchema(pages=[
        UIPage(name="Dashboard", route="/dashboard", components=[
            UIComponent(name="Navbar", type="header", description="Top nav"),
            UIComponent(name="ContactList", type="list", description="List of contacts")
        ])
    ])
    
    print("=== Generating SQLAlchemy Models ===")
    print(generate_db_code(db))
    print("\n" + "="*40 + "\n")
    
    print("=== Generating FastAPI Routers ===")
    print(generate_api_code(api))
    print("\n" + "="*40 + "\n")
    
    print("=== Generating React/TSX ===")
    print(generate_ui_code(ui))

if __name__ == "__main__":
    main()
