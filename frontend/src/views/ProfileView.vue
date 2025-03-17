<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { User, Mail, Save } from 'lucide-vue-next'

const authStore = useAuthStore()
const profile = ref<any>(null)
const isLoading = ref(true)
const isSaving = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

// Form fields
const fullName = ref('')
const website = ref('')
const bio = ref('')

// Load user profile
const loadProfile = async () => {
  isLoading.value = true
  errorMessage.value = ''
  
  try {
    profile.value = await authStore.getUserProfile()
    
    // Initialize form fields
    fullName.value = profile.value?.full_name || authStore.user?.user_metadata?.full_name || ''
    website.value = profile.value?.website || ''
    bio.value = profile.value?.bio || ''
  } catch (err: any) {
    console.error('Failed to load profile:', err)
    errorMessage.value = 'Failed to load profile'
  } finally {
    isLoading.value = false
  }
}

// Save profile changes
const saveProfile = async () => {
  isSaving.value = true
  errorMessage.value = ''
  successMessage.value = ''
  
  try {
    const { success, error } = await authStore.updateUserProfile({
      full_name: fullName.value,
      website: website.value,
      bio: bio.value
    })
    
    if (success) {
      successMessage.value = 'Profile updated successfully'
      await loadProfile() // Reload profile
    } else {
      errorMessage.value = error || 'Failed to update profile'
    }
  } catch (err: any) {
    console.error('Failed to save profile:', err)
    errorMessage.value = 'Failed to save profile'
  } finally {
    isSaving.value = false
  }
}

// Load profile on component mount
onMounted(() => {
  loadProfile()
})
</script>

<template>
  <div class="container mx-auto max-w-4xl p-4">
    <div class="mb-8">
      <h1 class="text-2xl font-bold">Your Profile</h1>
      <p class="text-muted-foreground">Manage your account information</p>
    </div>
    
    <div v-if="isLoading" class="flex justify-center py-8">
      <div class="animate-spin text-primary">●</div>
    </div>
    
    <div v-else class="grid gap-6 md:grid-cols-[1fr_2fr]">
      <!-- User info card -->
      <div class="rounded-lg border bg-card p-6 shadow-sm">
        <div class="flex flex-col items-center space-y-4">
          <div class="h-24 w-24 rounded-full bg-muted flex items-center justify-center">
            <User class="h-12 w-12 text-muted-foreground" />
          </div>
          
          <div class="text-center">
            <h2 class="text-xl font-semibold">{{ fullName || 'User' }}</h2>
            <p class="text-sm text-muted-foreground flex items-center justify-center">
              <Mail class="mr-1 h-3 w-3" />
              {{ authStore.user?.email }}
            </p>
          </div>
          
          <div class="w-full pt-4 border-t">
            <p class="text-sm text-muted-foreground">
              <span class="font-medium">Member since:</span> 
              {{ new Date(authStore.user?.created_at || Date.now()).toLocaleDateString() }}
            </p>
          </div>
        </div>
      </div>
      
      <!-- Edit profile form -->
      <div class="rounded-lg border bg-card p-6 shadow-sm">
        <form @submit.prevent="saveProfile" class="space-y-4">
          <div class="space-y-2">
            <label for="fullName" class="text-sm font-medium">Full Name</label>
            <input
              id="fullName"
              v-model="fullName"
              type="text"
              class="w-full rounded-md border bg-background px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
            />
          </div>
          
          <div class="space-y-2">
            <label for="website" class="text-sm font-medium">Website</label>
            <input
              id="website"
              v-model="website"
              type="url"
              class="w-full rounded-md border bg-background px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
            />
          </div>
          
          <div class="space-y-2">
            <label for="bio" class="text-sm font-medium">Bio</label>
            <textarea
              id="bio"
              v-model="bio"
              rows="4"
              class="w-full rounded-md border bg-background px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
            ></textarea>
          </div>
          
          <div v-if="successMessage" class="rounded-md bg-green-50 p-3 text-sm text-green-600 dark:bg-green-900/20 dark:text-green-400">
            {{ successMessage }}
          </div>
          
          <div v-if="errorMessage" class="rounded-md bg-destructive/15 p-3 text-sm text-destructive">
            {{ errorMessage }}
          </div>
          
          <button
            type="submit"
            class="flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90 focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2 disabled:opacity-50"
            :disabled="isSaving"
          >
            <Save v-if="!isSaving" class="mr-2 h-4 w-4" />
            <span v-if="isSaving" class="mr-2 h-4 w-4 animate-spin">●</span>
            {{ isSaving ? 'Saving...' : 'Save Changes' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template> 