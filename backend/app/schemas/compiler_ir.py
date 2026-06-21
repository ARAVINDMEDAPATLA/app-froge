from pydantic import BaseModel, Field as PydanticField
from typing import List, Optional


# =========================
# FIELD
# =========================

class Field(BaseModel):
    name: str
    type: str
    required: bool = True


# =========================
# ENTITY
# =========================

class Entity(BaseModel):
    name: str
    fields: List[Field] = PydanticField(default_factory=list)


# =========================
# PAGE
# =========================

class Page(BaseModel):
    name: str
    route: str


# =========================
# ROLE
# =========================

class Role(BaseModel):
    name: str
    description: Optional[str] = None


# =========================
# API ROUTE
# =========================

class ApiRoute(BaseModel):
    path: str
    method: str
    description: Optional[str] = None


# =========================
# BUSINESS RULE
# =========================

class BusinessRule(BaseModel):
    name: str
    description: str


# =========================
# COMPILER IR
# =========================

class CompilerIR(BaseModel):
    app_name: str

    entities: List[Entity] = PydanticField(default_factory=list)

    pages: List[Page] = PydanticField(default_factory=list)

    roles: List[Role] = PydanticField(default_factory=list)

    api_routes: List[ApiRoute] = PydanticField(default_factory=list)

    business_rules: List[BusinessRule] = PydanticField(default_factory=list)


# =========================
# TEST
# =========================

if __name__ == "__main__":

    crm_ir = CompilerIR(
        app_name="CRM",

        entities=[
            Entity(
                name="Contact",
                fields=[
                    Field(
                        name="id",
                        type="integer"
                    ),
                    Field(
                        name="email",
                        type="string"
                    )
                ]
            )
        ],

        pages=[
            Page(
                name="Dashboard",
                route="/dashboard"
            ),
            Page(
                name="Contacts",
                route="/contacts"
            )
        ],

        roles=[
            Role(
                name="Admin",
                description="Full access"
            ),
            Role(
                name="User",
                description="Standard user"
            )
        ],

        api_routes=[
            ApiRoute(
                path="/contacts",
                method="GET"
            ),
            ApiRoute(
                path="/contacts",
                method="POST"
            )
        ],

        business_rules=[
            BusinessRule(
                name="AdminAnalytics",
                description="Only admin can view analytics"
            )
        ]
    )

    print("\n=== COMPILER IR ===\n")

    print(crm_ir)

    print("\n=== JSON OUTPUT ===\n")

    print(crm_ir.model_dump())