<script setup lang="ts">
// Inbox view component
import HomeNavbar from '@/components/HomeNavbar.vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const navigateToLogin = () => {
  router.push('/login')
}

const navigateToRegister = () => {
  router.push('/register')
}

const navigateToDashboard = () => {
  router.push('/app')
}
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <HomeNavbar />
    
    <main class="flex-1 flex flex-col">
      <!-- Hero Section -->
      <section class="py-20 px-6 flex flex-col items-center justify-center text-center">
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6">
          Welcome to Our Application
        </h1>
        <p class="text-lg md:text-xl text-muted-foreground max-w-3xl mb-10">
          A powerful platform for managing your tasks, communications, and more. 
          Sign up today to get started with our comprehensive suite of tools.
        </p>
        
        <div class="flex flex-col sm:flex-row gap-4">
          <button 
            v-if="authStore.isAuthenticated"
            @click="navigateToDashboard" 
            class="px-6 py-3 rounded-md bg-primary text-primary-foreground hover:bg-primary/90 text-lg font-medium"
          >
            Go to Dashboard
          </button>
          <template v-else>
            <button 
              @click="navigateToLogin" 
              class="px-6 py-3 rounded-md bg-primary text-primary-foreground hover:bg-primary/90 text-lg font-medium"
            >
              Login
            </button>
            <button 
              @click="navigateToRegister" 
              class="px-6 py-3 rounded-md bg-secondary text-secondary-foreground hover:bg-secondary/90 text-lg font-medium"
            >
              Register
            </button>
          </template>
        </div>
      </section>
      
      <!-- Features Section -->
      <section class="py-16 px-6 bg-muted/50">
        <div class="max-w-7xl mx-auto">
          <h2 class="text-3xl font-bold text-center mb-12">Key Features</h2>
          <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-card p-6 rounded-lg shadow-sm">
              <h3 class="text-xl font-semibold mb-3">Feature 1</h3>
              <p class="text-muted-foreground">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </p>
            </div>
            <div class="bg-card p-6 rounded-lg shadow-sm">
              <h3 class="text-xl font-semibold mb-3">Feature 2</h3>
              <p class="text-muted-foreground">
                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
                nisi ut aliquip ex ea commodo consequat.
              </p>
            </div>
            <div class="bg-card p-6 rounded-lg shadow-sm">
              <h3 class="text-xl font-semibold mb-3">Feature 3</h3>
              <p class="text-muted-foreground">
                Duis aute irure dolor in reprehenderit in voluptate velit esse 
                cillum dolore eu fugiat nulla pariatur.
              </p>
            </div>
          </div>
        </div>
      </section>
    </main>
    
    <footer class="py-8 px-6 bg-muted text-center">
      <p class="text-sm text-muted-foreground">
        © 2023 Your Company. All rights reserved.
      </p>
    </footer>
  </div>
</template>

<style scoped>
/* Add any component-specific styles here */
</style>
