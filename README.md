# SaaS Quickstart

A complete starter template for building SaaS applications with Vue 3 with shad-cn and Tailwind CSS, Flask, and Supabase authentication.

## Overview

This template provides everything you need to quickly launch a SaaS product:

- **Frontend**: Vue 3 with TypeScript, Vite, Tailwind CSS, and shad-cn
- **Backend**: Flask Python API with a structured project setup
- **Authentication**: Complete Supabase auth system with login, registration, and profile management
- **Infrastructure**: Development environment with concurrent frontend and backend servers

## Features

- **Supabase Authentication System**: Complete Supabase authentication with:
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

- **AI Integration**: OpenAI Integration with Responses API & OpenAI Agents SDK
  - Integrated with example tools, both for Responses API and OpenAI SDK. Enabling easy plugin of tools.

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

### AI Setup (Optional)

1. Get API keys for the AI providers you want to use:
   - OpenAI API key from [OpenAI](https://platform.openai.com/api-keys)

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
- Backend on http://localhost:8000

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
## License

MIT
