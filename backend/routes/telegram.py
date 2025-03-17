from controller.telegram.telegram_utils import (
    send_telegram_notification,
)
from flask import Blueprint, request, jsonify
from flasgger import swag_from

telegram_bp = Blueprint("telegram", __name__)

@telegram_bp.route("/bot/send/text", methods=["POST"])
@swag_from({
    "tags": ["Telegram"],
    "summary": "Send a text message to Telegram",
    "description": "Send a text message to the default Telegram chat configured in environment variables",
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["message"],
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message to send",
                        "example": "Hello, this is a test message"
                    },
                    "markdown": {
                        "type": "boolean",
                        "description": "Whether to parse the message as Markdown",
                        "example": False
                    }
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Message sent successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "success": {
                        "type": "boolean",
                        "example": True
                    },
                    "message": {
                        "type": "string",
                        "example": "Message sent successfully"
                    }
                }
            }
        },
        "400": {
            "description": "Bad request, missing required parameters",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "example": "Message is required"
                    }
                }
            }
        },
        "500": {
            "description": "Server error",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "example": "Failed to send message"
                    }
                }
            }
        }
    }
})
def send_telegram_text_message():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    message = data["message"]
    markdown = data.get("markdown", False)

    try:
        response = send_telegram_notification(message, markdown=markdown)
        return jsonify({"success": True, "message": "Message sent successfully", "response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
