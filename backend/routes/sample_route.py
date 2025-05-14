from typing import Optional
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel

router = APIRouter()

class SampleRequest(BaseModel):
    name: str
    value: Optional[int] = None

class SampleResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None

@router.post("/test", response_model=SampleResponse)
async def test_endpoint(data: SampleRequest):
    """
    A simple test endpoint.
    
    Returns a greeting message with the provided name and value.
    """
    try:
        result = {
            "greeting": f"Hello, {data.name}!",
            "value": data.value
        }
        return {"success": True, "message": "Test endpoint successful", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
