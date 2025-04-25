from typing import Optional
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from controller.telegram.telegram_utils import send_telegram_notification

router = APIRouter()

class TelegramMessage(BaseModel):
    message: str
    markdown: Optional[bool] = False
    
class MessageResponse(BaseModel):
    success: bool
    message: str
    response: Optional[dict] = None

@router.post("/bot/send", response_model=MessageResponse)
async def send_telegram_message(data: TelegramMessage):
    """
    Send a text message to Telegram.
    
    Send a text message to the default Telegram chat configured in environment variables.
    """
    try:
        response = send_telegram_notification(data.message, markdown=data.markdown)
        return {"success": True, "message": "Message sent successfully", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 