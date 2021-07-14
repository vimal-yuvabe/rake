#!/bin/bash

# mkdir -p app/temp/input

uvicorn --reload main:app --host=0.0.0.0 --port="${1:-8000}"