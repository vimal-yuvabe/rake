# pylint: disable=ungrouped-imports
# pylint: disable=missing-module-docstring

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.datastructures import CommaSeparatedStrings
from settings import settings
from route import router as RakeRouter
from model import RootModel

app = FastAPI(title="Extract Key Phrases", description="This REST API will extract the key phrases\
                    or keywords from the input text", version="1.0",
                    openapi_url="/api/v1/openapi.json")

app.include_router(RakeRouter)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CommaSeparatedStrings(settings.allowed_hosts),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["Root"], response_model=RootModel)
async def read_root():
    ''' Main Root API End point to return the description of the api'''
    msg = "This REST API will extract the key phrases or keywords from the input text"
    return RootModel(message=msg)
