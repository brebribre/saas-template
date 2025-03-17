<script setup lang="ts">
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  navigationMenuTriggerStyle,
} from '@/components/ui/navigation-menu'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { LogIn, UserPlus, User } from 'lucide-vue-next'

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

const components: { title: string, href: string, description: string }[] = [
  {
    title: 'Alert Dialog',
    href: '/docs/components/alert-dialog',
    description:
      'A modal dialog that interrupts the user with important content and expects a response.',
  },
  {
    title: 'Hover Card',
    href: '/docs/components/hover-card',
    description:
      'For sighted users to preview content available behind a link.',
  },
  {
    title: 'Progress',
    href: '/docs/components/progress',
    description:
      'Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.',
  },
  {
    title: 'Scroll-area',
    href: '/docs/components/scroll-area',
    description: 'Visually or semantically separates content.',
  },
  {
    title: 'Tabs',
    href: '/docs/components/tabs',
    description:
      'A set of layered sections of content—known as tab panels—that are displayed one at a time.',
  },
  {
    title: 'Tooltip',
    href: '/docs/components/tooltip',
    description:
      'A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.',
  },
]
</script>

<template>
  <div class="w-full py-4 px-6 flex items-center justify-between">
    <NavigationMenu>
      <NavigationMenuList>
        <NavigationMenuItem>
          <NavigationMenuTrigger>Getting started</NavigationMenuTrigger>
          <NavigationMenuContent>
            <ul class="grid gap-3 p-6 md:w-[400px] lg:w-[500px] lg:grid-cols-[minmax(0,.75fr)_minmax(0,1fr)]">
              <li class="row-span-3">
                <NavigationMenuLink as-child>
                  <a
                    class="flex h-full w-full select-none flex-col justify-end rounded-md bg-gradient-to-b from-muted/50 to-muted p-6 no-underline outline-none focus:shadow-md"
                    href="/"
                  >
                    <img src="https://www.reka-ui.com/logo.svg" class="h-6 w-6">
                    <div class="mb-2 mt-4 text-lg font-medium">
                      shadcn/ui
                    </div>
                    <p class="text-sm leading-tight text-muted-foreground">
                      Beautifully designed components built with Radix UI and
                      Tailwind CSS.
                    </p>
                  </a>
                </NavigationMenuLink>
              </li>

              <li>
                <NavigationMenuLink as-child>
                  <a
                    href="/docs/introduction"
                    class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground"
                  >
                    <div class="text-sm font-medium leading-none">Introduction</div>
                    <p class="line-clamp-2 text-sm leading-snug text-muted-foreground">
                      Re-usable components built using Radix UI and Tailwind CSS.
                    </p>
                  </a>
                </NavigationMenuLink>
              </li>
              <li>
                <NavigationMenuLink as-child>
                  <a
                    href="/docs/installation"
                    class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground"
                  >
                    <div class="text-sm font-medium leading-none">Installation</div>
                    <p class="line-clamp-2 text-sm leading-snug text-muted-foreground">
                      How to install dependencies and structure your app.
                    </p>
                  </a>
                </NavigationMenuLink>
              </li>
              <li>
                <NavigationMenuLink as-child>
                  <a
                    href="/docs/typography"
                    class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground"
                  >
                    <div class="text-sm font-medium leading-none">Typography</div>
                    <p class="line-clamp-2 text-sm leading-snug text-muted-foreground">
                      Styles for headings, paragraphs, lists...etc
                    </p>
                  </a>
                </NavigationMenuLink>
              </li>
            </ul>
          </NavigationMenuContent>
        </NavigationMenuItem>
        <NavigationMenuItem>
          <NavigationMenuTrigger>Components</NavigationMenuTrigger>
          <NavigationMenuContent>
            <ul class="grid w-[400px] gap-3 p-4 md:w-[500px] md:grid-cols-2 lg:w-[600px] ">
              <li v-for="component in components" :key="component.title">
                <NavigationMenuLink as-child>
                  <a
                    :href="component.href"
                    class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground"
                  >
                    <div class="text-sm font-medium leading-none">{{ component.title }}</div>
                    <p class="line-clamp-2 text-sm leading-snug text-muted-foreground">
                      {{ component.description }}
                    </p>
                  </a>
                </NavigationMenuLink>
              </li>
            </ul>
          </NavigationMenuContent>
        </NavigationMenuItem>
        <NavigationMenuItem>
          <NavigationMenuLink href="/docs/introduction" :class="navigationMenuTriggerStyle()">
            Documentation
          </NavigationMenuLink>
        </NavigationMenuItem>
      </NavigationMenuList>
    </NavigationMenu>

    <!-- Auth buttons -->
    <div class="flex items-center space-x-4">
      <div v-if="authStore.isAuthenticated" class="flex items-center space-x-4">
        <div class="flex items-center space-x-2">
          <div class="w-8 h-8 rounded-full bg-gray-200 dark:bg-gray-700 flex items-center justify-center">
            <User class="w-4 h-4" />
          </div>
          <span class="text-sm hidden md:inline">{{ authStore.user?.email }}</span>
        </div>
        <button 
          @click="navigateToDashboard" 
          class="px-4 py-2 rounded-md bg-primary text-primary-foreground hover:bg-primary/90 flex items-center"
        >
          <LogIn class="w-4 h-4 mr-2" />
          <span>Dashboard</span>
        </button>
      </div>
      <div v-else class="flex items-center space-x-4">
        <button 
          @click="navigateToLogin" 
          class="px-4 py-2 rounded-md bg-primary text-primary-foreground hover:bg-primary/90 flex items-center"
        >
          <LogIn class="w-4 h-4 mr-2" />
          <span>Login</span>
        </button>
        <button 
          @click="navigateToRegister" 
          class="px-4 py-2 rounded-md bg-secondary text-secondary-foreground hover:bg-secondary/90 flex items-center"
        >
          <UserPlus class="w-4 h-4 mr-2" />
          <span>Register</span>
        </button>
      </div>
    </div>
  </div>
</template>