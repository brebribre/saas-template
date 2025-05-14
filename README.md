# SaaS Quickstart

A complete starter template for building SaaS applications with Vue 3 with shad-cn and Tailwind CSS, FastAPI, and Supabase authentication.

## Overview

This template provides everything you need to quickly launch a SaaS product:

- **Frontend**: Vue 3 with TypeScript, Vite, Tailwind CSS, and shad-cn
- **Backend**: FastAPI Python with a structured project setup
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
VITE_BACKEND_URL=http://127.0.0.1:8000
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
This repository uses Concurrently to create package.json scripts that concurrently run the client and server. To run the application, follow these:

1. Clone the repository:

2. Install all dependencies (frontend and backend):
```bash
npm run install-all
```

### Development

To run both frontend and backend in development mode, run this from root folder:
```bash
npm run dev
```
This will activate the package.json script using Concurrently, that calls the backend and frontend together.

This will start:
- Frontend on http://localhost:5173
- Backend on http://localhost:8000 with Endpoints accessible via swagger in http://127.0.0.1:8000/api/v1/docs

To run only frontend:
```bash
npm run frontend
```

To run only backend:
```bash
npm run backend
```


## License

MIT
