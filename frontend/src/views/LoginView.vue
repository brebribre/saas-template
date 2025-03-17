<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { Mail, Lock, LogIn } from 'lucide-vue-next'

const router = useRouter()
const authStore = useAuthStore()

const email = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  if (!email.value || !password.value) {
    errorMessage.value = 'Please enter both email and password'
    return
  }

  isLoading.value = true
  errorMessage.value = ''

  try {
    const { success, error } = await authStore.signIn(email.value, password.value)
    
    if (success) {
      router.push('/app')
    } else {
      errorMessage.value = error || 'Failed to sign in'
    }
  } catch (err: any) {
    errorMessage.value = err.message || 'An unexpected error occurred'
  } finally {
    isLoading.value = false
  }
}

const goToRegister = () => {
  router.push('/register')
}
</script>

<template>
  <div class="flex min-h-screen items-center justify-center p-4">
    <div class="w-full max-w-md space-y-8 rounded-lg border bg-card p-6 shadow-sm">
      <div class="text-center">
        <h1 class="text-2xl font-bold">Sign In</h1>
        <p class="mt-2 text-sm text-muted-foreground">
          Sign in to your account to continue
        </p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-4">
        <div class="space-y-2">
          <label for="email" class="text-sm font-medium">Email</label>
          <div class="relative">
            <Mail class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
            <input
              id="email"
              v-model="email"
              type="email"
              placeholder="name@example.com"
              class="w-full rounded-md border bg-background py-2 pl-10 pr-4 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
              required
            />
          </div>
        </div>

        <div class="space-y-2">
          <label for="password" class="text-sm font-medium">Password</label>
          <div class="relative">
            <Lock class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
            <input
              id="password"
              v-model="password"
              type="password"
              placeholder="••••••••"
              class="w-full rounded-md border bg-background py-2 pl-10 pr-4 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
              required
            />
          </div>
        </div>

        <div v-if="errorMessage" class="rounded-md bg-destructive/15 p-3 text-sm text-destructive">
          {{ errorMessage }}
        </div>

        <button
          type="submit"
          class="flex w-full items-center justify-center rounded-md bg-primary py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90 focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2 disabled:opacity-50"
          :disabled="isLoading"
        >
          <LogIn v-if="!isLoading" class="mr-2 h-4 w-4" />
          <span v-if="isLoading" class="mr-2 h-4 w-4 animate-spin">●</span>
          {{ isLoading ? 'Signing in...' : 'Sign In' }}
        </button>
      </form>

      <div class="mt-4 text-center text-sm">
        Don't have an account?
        <button @click="goToRegister" class="font-medium text-primary hover:underline">
          Sign up
        </button>
      </div>
    </div>
  </div>
</template> 