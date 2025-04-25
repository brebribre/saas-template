from typing import Optional, List, Dict, Any
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field
import traceback

from controller.openai.openai_utils import OpenAIUtils

router = APIRouter()
openai_utils = OpenAIUtils()

class ResponseRequest(BaseModel):
    input: str
    model: Optional[str] = "gpt-4o"
    tools: Optional[List[Dict[str, Any]]] = []
    temperature: Optional[float] = 0.7

@router.post("/response")
async def create_response(request: ResponseRequest):
    """
    Create a response using the OpenAI Responses API.
    
    Sends a request to OpenAI's Responses API with the specified parameters and returns the response.
    """
    try:
        response = openai_utils.create_response(
            input_text=request.input,
            model=request.model,
            tools=request.tools,
            temperature=request.temperature,
        )
        
        # Convert the API response to a dictionary
        response_data = response.model_dump()
        
        return response_data
    
    except Exception as e:
        print(f"Error in create_response endpoint: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
