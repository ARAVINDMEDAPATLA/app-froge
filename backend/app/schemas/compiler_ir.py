
from pydantic import BaseModel
from typing import List, Optional


class Field(BaseModel):
    name: str
    type: str
    required: bool = True

class Entity(BaseModel):
    name: str
    fields: List[Field] = []


contact = Entity(
    name="Contact",
    fields=[
        Field(name="id", type="integer"),
        Field(name="email", type="string")
    ]
)

print(contact)
print(contact.model_dump())