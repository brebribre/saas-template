import os
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger, swag_from
from dotenv import load_dotenv

from routes.telegram import telegram_bp
from routes.langchain_routes import langchain_bp

# Load environment variables
load_dotenv()

# Environment configuration
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:3000')

# Configure allowed origins based on environment
ALLOWED_ORIGINS = [FRONTEND_URL]
if FLASK_ENV == 'production':
    ALLOWED_ORIGINS.append('https://www.google.com') # TODO: Change to the production URL

app = Flask(__name__)

# Configure Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api/v1/docs",
    "swagger_ui_bundle_js": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
    "swagger_ui_standalone_preset_js": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-standalone-preset.js",
    "swagger_ui_css": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    "swagger_ui_config": {
        "deepLinking": True,
        "displayOperationId": False,
        "defaultModelsExpandDepth": 1,
        "defaultModelExpandDepth": 1,
        "defaultModelRendering": "example",
        "displayRequestDuration": True,
        "docExpansion": "list",
        "filter": True,
        "operationsSorter": "alpha",
        "showExtensions": True,
        "showCommonExtensions": True,
        "tagsSorter": "alpha",
        "supportedSubmitMethods": ["get", "post", "put", "delete", "patch"],
        "tryItOutEnabled": True,  # Enable "Try it out" feature
        "persistAuthorization": True  # Keep authorization data between page reloads
    }
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Stratigo API",
        "description": "API for Stratigo application with LangChain integration",
        "version": "1.0.0",
        "contact": {
            "email": "support@stratigo.com"
        }
    },
    "basePath": "/api/v1",
    "schemes": ["http", "https"],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
    "security": [
        {
            "Bearer": []
        }
    ],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ]
}

# Only enable Swagger in development for security
if FLASK_ENV == 'development':
    swagger = Swagger(app, config=swagger_config, template=swagger_template)

CORS(app, resources={r"/*": {"origins": ALLOWED_ORIGINS}})

# Health check endpoint - Digital Ocean checks the root path by default
@app.route('/')
def health_check():
    """Health check endpoint for Digital Ocean."""
    return '', 200  # Return empty response with 200 status code

# Register blueprints
app.register_blueprint(telegram_bp, url_prefix='/api/v1')
app.register_blueprint(langchain_bp, url_prefix='/api/v1')

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Digital Ocean often uses port 8000
    app.run(
        host="0.0.0.0",
        port=port,
        debug=FLASK_ENV == 'development'
    )
