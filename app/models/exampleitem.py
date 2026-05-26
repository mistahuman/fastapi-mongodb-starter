from typing import Optional
from beanie import Document
from pydantic import Field


class ExampleItem(Document):
    title: str = Field(..., description="Title of exampleitem")
    value: int = Field(..., description="Value of exampleitem")
    code: str = Field(..., description="Code of exampleitem")
    description: Optional[str] = Field(None, description="Description of exampleitem")

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Lorem ipsum",
                "value": 100,
                "code": "LIPS01",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            }
        }
    }

    class Settings:
        name = "exampleitems"
