from pydantic import BaseModel
from typing import Optional


class UpdateExampleItem(BaseModel):
    title: Optional[str] = None
    code: Optional[str] = None
    value: Optional[int] = None
    description: Optional[str] = None

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
