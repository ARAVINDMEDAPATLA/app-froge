from pydantic import BaseModel, Field as PydanticField
from typing import List

from .entity import Entity
from .page import Page
from .role import Role
from .api_route import ApiRoute
from .business_rule import BusinessRule


class CompilerIR(BaseModel):

    app_name: str

    entities: List[Entity] = PydanticField(default_factory=list)

    pages: List[Page] = PydanticField(default_factory=list)

    roles: List[Role] = PydanticField(default_factory=list)

    api_routes: List[ApiRoute] = PydanticField(default_factory=list)

    business_rules: List[BusinessRule] = PydanticField(default_factory=list)