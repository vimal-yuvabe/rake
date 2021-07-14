# pylint: disable=missing-module-docstring
import uuid
from fastapi import APIRouter, Body, HTTPException
from model import InputModel, ExtractRakeOutputModel
from rake_service import RakeService

# Declaration of Router and Initialization of Rake service
router = APIRouter()
rake_service = RakeService()


@router.post("/extract-phrases", response_description="Keyphrases Extracted Successfully",
             response_model=ExtractRakeOutputModel)
async def extract_key_phrases(input: InputModel = Body(...)) -> ExtractRakeOutputModel:
    """ Post Route Method to extract the key phrases """
    request_id = None
    response_id = uuid.uuid4().hex
    if hasattr(input, "request_id"):
        request_id = input.request_id

    try:

        rake_output = []
        for text_str in input.input_text:
            rake_output.append(rake_service.get_phrases(text_str))
        output = ExtractRakeOutputModel(key_phrases=rake_output,
                             request_id=request_id, response_id=response_id)
        return output

    except Exception as error_response:
        raise HTTPException(
            status_code=500, detail="Error extracting keywords from text."+str(error_response))
