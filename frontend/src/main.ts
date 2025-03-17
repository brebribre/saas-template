import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import router from './router'
import { useAuthStore } from './stores/auth'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)

// Initialize auth store early
const authStore = useAuthStore()
authStore.initialize().catch(err => {
  console.error('Failed to initialize auth store:', err)
})

app.mount('#app')
