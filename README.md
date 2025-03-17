# SaaS Quickstart

A complete starter template for building SaaS applications with Vue 3 with shad-cn and Tailwind CSS, Flask, and Supabase authentication.

## Overview

This template provides everything you need to quickly launch a SaaS product:

- **Frontend**: Vue 3 with TypeScript, Vite, Tailwind CSS, and shad-cn
- **Backend**: Flask Python API with a structured project setup
- **Authentication**: Complete Supabase auth system with login, registration, and profile management
- **Infrastructure**: Development environment with concurrent frontend and backend servers

## Features

- **Authentication System**: Complete Supabase authentication with:
  - Email/password login and registration
  - User profile management
  - Protected routes and navigation guards
  - Session persistence across page refreshes

- **Dashboard Layout**: Professional SaaS dashboard with:
  - Responsive sidebar navigation
  - User profile section
  - Dark/light mode support
  - Mobile-friendly design

- **Landing Page**: Customizable landing page with:
  - Hero section with call-to-action buttons
  - Features showcase
  - Responsive navigation

- **Development Setup**: Streamlined development with:
  - Concurrent frontend and backend servers

- **Notification System**: Telegram integration for notifications:
  - Send messages to a configured Telegram chat
  - Support for Markdown formatting
  - Simple API endpoint for sending notifications

- **AI Integration**: LangChain integration with multiple AI models:
  - OpenAI: GPT-3.5 Turbo, GPT-4
  - Anthropic: Claude 3 Opus, Claude 3 Sonnet, Claude 3.5 Sonnet, Claude 3.7 Opus
  - Google: Gemini Pro

- **AI Agent System**: Extensible agent framework with tool integration:
  - Generic agent endpoint that can use any available tools
  - Automatic tool selection based on query content
  - Detailed information about tool usage in responses
  - Easily extensible with new tool categories

- **Math Tools**: LangChain-powered mathematical problem solving:
  - Basic arithmetic operations (add, subtract, multiply, divide)
  - Advanced functions (power, square root, logarithm, factorial)
  - Statistical operations (mean, median, standard deviation)
  - Equation solving (quadratic equations)
  - AI-assisted step-by-step solutions

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm (v7 or higher)
- Python 3.8 or higher
- pip (Python package installer)
- Supabase account and project (for authentication)
- Telegram bot (optional, for notifications)
- API keys for AI providers (optional, for AI features)

### Supabase Setup

1. Create a new project on [Supabase](https://supabase.com)
2. Enable Email Auth in Authentication settings
3. Copy your project URL and anon key from the API settings

### Telegram Bot Setup (Optional)

1. Create a new bot using [BotFather](https://t.me/botfather) on Telegram
2. Get your bot token from BotFather
3. Add your bot to a group chat or start a direct conversation with it
4. Get the chat ID (you can use the [getUpdates API method](https://core.telegram.org/bots/api#getupdates) or a bot like [@userinfobot](https://t.me/userinfobot))

### AI Setup (Optional)

1. Get API keys for the AI providers you want to use:
   - OpenAI API key from [OpenAI](https://platform.openai.com/api-keys)
   - Anthropic API key from [Anthropic](https://console.anthropic.com/settings/keys)
   - Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Environment Setup

1. Create a `.env` file in the frontend directory with your Supabase credentials:
```
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

2. Create a `.env` file in the backend directory with your configuration:
```
# Telegram Bot Configuration (optional)
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GROUP_CHAT_ID=your_telegram_group_chat_id

# AI API Keys (optional)
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/brebribre/vue-flask-saas-quickstart.git
cd vue-flask-saas-quickstart
```

2. Install all dependencies (frontend and backend):
```bash
npm run install-all
```

### Development

To run both frontend and backend in development mode:
```bash
npm run dev
```

This will start:
- Frontend on http://localhost:5173
- Backend on http://localhost:5000 (default Flask port)

To run only frontend:
```bash
npm run frontend
```

To run only backend:
```bash
npm run backend
```

### Manual Backend Setup (if needed)

If you prefer to set up the backend manually or if the automatic setup fails:

1. Create and activate virtual environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run Flask:
```bash
flask run
```

### Production

1. Build the frontend:
```bash
npm run build
```

2. Start the production server:
```bash
npm start
```

## API Endpoints

### Telegram Notifications

Send a notification to the configured Telegram chat:

```
POST /bot/send/text
```

Request body:
```json
{
  "message": "Your notification message",
  "markdown": false
}
```

### AI Question Answering

Ask a question to an AI model:

```
POST /api/v1/ask
```

Request body:
```json
{
  "question": "Your question here",
  "model": "claude-3.5-sonnet"
}
```

Available models:
- `gpt-3.5-turbo`
- `gpt-4`
- `claude-3-opus`
- `claude-3-sonnet`
- `claude-3.5-sonnet`
- `claude-3.7-opus`
- `gemini-pro`

### AI Agent

Send a query to an AI agent that can use various tools:

```
POST /api/v1/agent
```

Request body:
```json
{
  "query": "Calculate the square root of 16 and then add it to 10",
  "model": "claude-3.5-sonnet",
  "tool_categories": ["math"]
}
```

The `tool_categories` field is optional. If not provided, the agent will have access to all available tools and will decide which ones to use based on the query.

The response includes:
- The answer to the query
- Information about which tools were used
- A list of tool categories that were used
- The model that generated the answer

### Math Problem Solving

Solve a mathematical problem using AI and math tools:

```
POST /api/v1/math/solve
```

Request body:
```json
{
  "problem": "Calculate the square root of 16 and then add it to 10",
  "model": "claude-3.5-sonnet"
}
```

The response includes:
- The solution with step-by-step explanation
- Information about which math tools were used
- The model that generated the solution

## Extending with New Tools

To add new tool categories:

1. Create a new file in the `backend/langchain-tools` directory (e.g., `web_tool.py`)
2. Define your tools using the `@tool` decorator from LangChain
3. Import and add your tools to the `self.tools` dictionary in `LangChainController.__init__`

Example:
```python
# In backend/langchain-tools/web_tool.py
from langchain_core.tools import tool

@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    # Implementation here
    return results

# In backend/controller/langchain/langchain_controller.py
from web_tool import search_web

# In __init__ method
self.tools = {
    "math": [...],
    "web": [search_web]
}
```

## Available Scripts

- `npm run dev` - Run both frontend and backend in development mode
- `npm run frontend` - Run only frontend in development mode
- `npm run backend` - Run only backend in development mode (activates venv and runs Flask)
- `npm run install-all` - Install dependencies for both frontend and backend (including Python venv setup)
- `npm run build` - Build frontend for production
- `npm start` - Start the production server (Flask backend)

## License

MIT
