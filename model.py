# pylint: disable=missing-module-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Optional, List
from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """ Input Model """
    input_text: List[str] = Field(...)
    request_id: Optional[str]

    class Config:
        """ Sample Config"""
        schema_extra = {
            "example": {
                "input_text": ["Welcome to Rake processing service"]
            }

        }


class ExtractRakeOutputModel(BaseModel):
    """ Output Model"""
    key_phrases: List[List[str]]
    request_id: Optional[str]
    response_id: str
    message: str = "Keywords Extracted Successfully"

    class Config:
        """ Sample Config """
        schema_extra = {
            "example": {
                "key_phrases": [["rake processing service", "welcome"]],
                "request_id": "a4fc770680d52b11ebbb",
                "response_id": "abfa8d10da2b11ebbb43a4fc770680d5",
                "message": "Keywords Extracted Successfully"
            }
        }


class RootModel(BaseModel):
    """ Root Model """
    message: str

    class Config:
        """ Sample Config """
        schema_extra = {
            "example": {
                "message": "This REST API will extract the key phrases or keywords \
                           from the input text"
            }
        }
