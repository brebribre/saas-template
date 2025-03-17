<script setup lang="ts">
import {
  Home,
  Inbox,
  User,
  LogOut,
  Mail,
  UserCircle
} from 'lucide-vue-next'
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarFooter
} from '@/components/ui/sidebar'
import { useRouter } from 'vue-router'
import { onMounted, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

// Define the type for menu items
interface MenuItem {
  title: string
  route: string
  icon: any
  requiresAuth?: boolean
}

// Menu items with proper routes
const items: MenuItem[] = [
  {
    title: 'Dashboard',
    route: '/dashboard',
    icon: Home
  },
  {
    title: 'Inbox',
    route: '/inbox',
    icon: Inbox,
    requiresAuth: true
  },
]

const filteredItems = computed(() => {
  return items.filter(item => !item.requiresAuth || authStore.isAuthenticated)
})

const navigateTo = (route: string) => {
  router.push(route)
}

const handleSignIn = async () => {
  router.push('/login')
}

const handleSignUp = async () => {
  router.push('/register')
}

const handleSignOut = async () => {
  const { success } = await authStore.signOut()
  if (success) {
    router.push('/')
  }
}

// We don't need to initialize auth here since it's done in main.ts
// onMounted(() => {
//   authStore.initialize()
// })
</script>

<template>
  <Sidebar>
    <SidebarContent>
      <SidebarGroup>
        <SidebarGroupLabel>Application</SidebarGroupLabel>
        <SidebarGroupContent>
          <SidebarMenu>
            <SidebarMenuItem v-for="item in filteredItems" :key="item.title">
              <SidebarMenuButton asChild @click="navigateTo(item.route)">
                <div class="flex items-center cursor-pointer">
                  <component :is="item.icon" class="mr-2" />
                  <span>{{ item.title }}</span>
                </div>
              </SidebarMenuButton>
            </SidebarMenuItem>
          </SidebarMenu>
        </SidebarGroupContent>
      </SidebarGroup>
    </SidebarContent>
    
    <!-- User profile area at the bottom -->
    <SidebarFooter>
      <div class="p-4 border-t">
        <div v-if="authStore.isAuthenticated" class="space-y-3">
          <div 
            class="flex items-center justify-between cursor-pointer hover:bg-muted/50 p-2 rounded-md transition-colors"
            @click="navigateTo('/profile')"
          >
            <div class="flex items-center">
              <div class="w-8 h-8 rounded-full bg-gray-200 dark:bg-gray-700 flex items-center justify-center mr-2">
                <User class="w-4 h-4" />
              </div>
              <div>
                <p class="text-xs font-medium">{{ authStore.user?.email }}</p>
                <p class="text-xs text-gray-500 dark:text-gray-400">
                  {{ authStore.user?.user_metadata?.full_name || 'User' }}
                </p>
              </div>
            </div>
          </div>
          
          <button 
            @click="handleSignOut" 
            class="w-full py-1 flex items-center justify-center rounded-md border border-gray-200 dark:border-gray-700 hover:bg-muted/50 transition-colors"
          >
            <LogOut class="w-4 h-4 mr-2" />
            <span class="text-sm">Sign Out</span>
          </button>
        </div>
        
        <div v-else class="space-y-2">
          <button 
            @click="handleSignIn" 
            class="w-full py-1 flex items-center justify-center py-2 px-4 rounded-md bg-primary text-primary-foreground hover:bg-primary/90"
          >
            <Mail class="w-4 h-4 mr-2" />
            <span class="text-sm">Sign In</span>
          </button>
          
          <button 
            @click="handleSignUp" 
            class="w-full py-1 flex items-center justify-center py-2 px-4 rounded-md bg-secondary text-secondary-foreground hover:bg-secondary/90"
          >
            <User class="w-4 h-4 mr-2" />
            <span class="text-sm">Sign Up</span>
          </button>
        </div>
      </div>
    </SidebarFooter>
  </Sidebar>
</template>
