# SaaS Quickstart: Frontend

The Vue 3 frontend for the SaaS Quickstart template.

## Overview

This is the frontend portion of the SaaS Quickstart template, providing a complete Vue 3 application with Supabase authentication, dashboard layout, and landing page.

## Features

- **Vue 3**: Modern Vue framework with Composition API and `<script setup>` syntax
- **TypeScript**: Type-safe development experience
- **Vite**: Fast development server and optimized builds
- **Supabase Authentication**: Secure user authentication system
- **Pinia**: State management for Vue applications
- **Vue Router**: Client-side routing with navigation guards
- **Tailwind CSS**: Utility-first CSS framework for styling
- **vue-shad-cn**: Uses the vue-shad-cn component library
- **Responsive Design**: Mobile-friendly layouts for all pages

## Authentication

The application uses Supabase for authentication:

- **Email/Password Authentication**: Users can register and login with email and password
- **User Profiles**: User metadata is stored in Supabase user profiles
- **Protected Routes**: Routes with `requiresAuth` meta property are protected
- **Guest-Only Routes**: Routes with `guestOnly` meta property are only accessible to non-authenticated users
- **Session Persistence**: Authentication state is maintained across page refreshes

## Key Components

- **HomeView**: Landing page with hero section and features
- **HomeNavbar**: Navigation bar for the landing page with auth buttons
- **AppView**: Main application layout with sidebar
- **AppSidebar**: Navigation sidebar for authenticated users
- **DashboardView**: Main dashboard page for authenticated users
- **ProfileView**: User profile management page
- **LoginView**: User login page
- **RegisterView**: User registration page

## Project Structure

```
frontend/
├── src/                # Source code
│   ├── components/     # Reusable components
│   │   ├── ui/         # UI components
│   │   └── ...         # Feature-specific components
│   ├── views/          # Page components
│   ├── stores/         # Pinia stores
│   │   └── auth.ts     # Authentication store
│   ├── router/         # Vue Router configuration
│   ├── lib/            # Utilities and libraries
│   │   └── supabase.ts # Supabase client
│   └── ...
├── public/             # Static assets
└── ...
```

## Development

### Prerequisites

- Node.js (v16 or higher)
- npm (v7 or higher)
- Supabase account and project

### Environment Setup

Create a `.env` file in the frontend directory with your Supabase credentials:
```
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### Installation

```bash
npm install
```

### Development Server

```bash
npm run dev
```

### Build for Production

```bash
npm run build
```

## Customization

### Styling

- Update theme colors in `tailwind.config.ts`
- Modify global styles in `src/index.css`

### Content

- Update landing page content in `src/views/HomeView.vue`
- Modify navigation items in `src/components/AppSidebar.vue`
- Customize dashboard in `src/views/DashboardView.vue`

### Routes

- Add or modify routes in `src/router/index.ts`

## Learn More

- [Vue 3 Documentation](https://v3.vuejs.org/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Vite Documentation](https://vitejs.dev/guide/)
- [Supabase Documentation](https://supabase.io/docs)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [Vue Router Documentation](https://router.vuejs.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
