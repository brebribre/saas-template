import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def send_telegram_notification(message, markdown=None, chat_id=None, bot_token=None):
    print("sending telegram notification: ", message)

    bot_token = bot_token or os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = chat_id or os.getenv("GROUP_CHAT_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    if markdown:
        payload = {"chat_id": chat_id, "text": message, "parse_mode": "MarkdownV2"}
    else:
        payload = {"chat_id": chat_id, "text": message}

    response = requests.post(url, json=payload)
    return response.json()

