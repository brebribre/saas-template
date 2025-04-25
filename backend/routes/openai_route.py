from typing import Optional, List, Dict, Any, Union
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field
import traceback

from controller.openai.openai_utils import OpenAIUtils
from controller.tools import Tools

router = APIRouter()
openai_utils = OpenAIUtils()

class Message(BaseModel):
    role: str
    content: str

class ResponseRequest(BaseModel):
    input: Union[str, List[Message]]
    model: Optional[str] = "gpt-4o"
    tools: Optional[List[str]] = []
    temperature: Optional[float] = 0.7
    stream: Optional[bool] = False

@router.post("/response")
async def create_response(request: ResponseRequest):
    """
    Create a response using the OpenAI API.
    """
    try:
        # Get tool definitions based on the requested tool names
        processed_tools = Tools.get_tools_by_names(request.tools) if request.tools else []
        
        print(f"Processed tools: {processed_tools}")
        # Format input properly
        formatted_input = request.input
        if isinstance(formatted_input, list):
            # Convert Pydantic model objects to dictionaries
            formatted_input = [message.dict() for message in formatted_input]
        
        response = openai_utils.create_response(
            input_text=formatted_input,
            model=request.model,
            tools=processed_tools,
            temperature=request.temperature,
            stream=request.stream
        )
        
        response_data = response.model_dump()
        
        return response_data["output"]
    
    except ValueError as e:
        # Handle errors for unknown tools
        raise HTTPException(status_code=400, detail=str(e))
    
    except HTTPException as e:
        # Re-raise HTTP exceptions
        raise
    
    except Exception as e:
        print(f"Error in create_response endpoint: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/available-tools")
async def get_available_tools():
    """
    Get the list of available predefined tools.
    
    Returns the IDs of available tools that can be referenced in the /response endpoint.
    """
    return {"available_tools": list(Tools.get_all_tools_definitions())}
