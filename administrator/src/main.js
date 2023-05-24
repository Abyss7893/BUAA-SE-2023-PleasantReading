import { createApp } from 'vue'
import App from './App.vue'
import router from './route/index'
import ElementPlus from 'element-plus'
const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount('#app')

